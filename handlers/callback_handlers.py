from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message

from data_base.base import session
from data_base.models import CustomerBasketSetting, CustomerSetting
from filters.filters import CheckBasketLimitInput
from keyboard.keyboards import (end_purchase_markup, purchase_markup, back_markup, echo_markup,
                                settings_markup, set_up_mode_markup, start_markup)
from lexicon.text_buttons import BUTTON_TEXT
from lexicon.text_commands import COMMAND_TEXT
from logic.enums import BotMode
from states.states import FSMCustomer
from utils.utils import convert_str_float_to_float, upd_language


router = Router()


# SETTINGS HANDLERS
@router.callback_query(F.data == BUTTON_TEXT["ru"]["settings"])
@router.callback_query(F.data == BUTTON_TEXT["en"]["settings"])
async def settings(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=COMMAND_TEXT[upd_language(callback)]["settings"],
                                     reply_markup=settings_markup)
    await state.set_state(FSMCustomer.settings)


@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["ru"]["set_up_basket_limit"])
@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["en"]["set_up_basket_limit"])
async def basket_limit_input(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=COMMAND_TEXT[upd_language(callback)]["set_up_basket_limit"])
    await state.set_state(FSMCustomer.set_up_basket_limit)


@router.message(StateFilter(FSMCustomer.set_up_basket_limit), CheckBasketLimitInput())
async def set_up_basket_limit(message: Message, state: FSMContext):
    input_price = convert_str_float_to_float(message)
    basket_limit = session.query(CustomerSetting).filter(CustomerSetting.customer_id == message.from_user.id).first()
    basket_limit.basket_limit = input_price
    session.commit()
    await message.answer(text=f'{COMMAND_TEXT[upd_language(message)]["set_up_basket_limit_done"]}\n\n'
                              f'{COMMAND_TEXT[upd_language(message)]["settings"]}', reply_markup=settings_markup)
    await state.set_state(FSMCustomer.settings)


@router.message(StateFilter(FSMCustomer.set_up_basket_limit))
async def echo_set_up_basket_limit_message(message: Message):
    await message.answer(text="I don't know what you mean\n"
                              f"{COMMAND_TEXT[upd_language(message)]['enter_price']}")


@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["ru"]["set_up_bot_mode"])
@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["en"]["set_up_bot_mode"])
async def basket_limit_input(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=COMMAND_TEXT[upd_language(callback)]["set_up_bot_mode"],
                                     reply_markup=set_up_mode_markup)
    await state.set_state(FSMCustomer.set_up_bot_mode)


@router.callback_query(StateFilter(FSMCustomer.set_up_bot_mode), F.data == BUTTON_TEXT["ru"]["normal"])
@router.callback_query(StateFilter(FSMCustomer.set_up_bot_mode), F.data == BUTTON_TEXT["en"]["normal"])
async def set_up_bot_mode(callback: CallbackQuery, state: FSMContext):
    set_bot_mode = session.query(CustomerSetting).filter(CustomerSetting.customer_id == callback.from_user.id).first()
    set_bot_mode.bot_mode = BotMode.NORMAL
    session.commit()
    await callback.message.edit_text(text=f'{COMMAND_TEXT[upd_language(callback)]["set_up_bot_mode_done"]}\n'
                                          f'{COMMAND_TEXT[upd_language(callback)]["settings"]}',
                                     reply_markup=settings_markup)
    await state.set_state(FSMCustomer.settings)


@router.callback_query(StateFilter(FSMCustomer.set_up_bot_mode), F.data == BUTTON_TEXT["ru"]["silent"])
@router.callback_query(StateFilter(FSMCustomer.set_up_bot_mode), F.data == BUTTON_TEXT["en"]["silent"])
async def set_up_bot_mode(callback: CallbackQuery, state: FSMContext):
    set_bot_mode = session.query(CustomerSetting).filter(CustomerSetting.customer_id == callback.from_user.id).first()
    set_bot_mode.bot_mode = BotMode.SILENT
    session.commit()
    await callback.message.edit_text(text=f'{COMMAND_TEXT[upd_language(callback)]["set_up_bot_mode_done"]}\n'
                                          f'{COMMAND_TEXT[upd_language(callback)]["settings"]}',
                                     reply_markup=settings_markup)
    await state.set_state(FSMCustomer.settings)


@router.message(StateFilter(FSMCustomer.set_up_bot_mode))
async def echo_set_up_bot_mode_message(message: Message):
    await message.answer(text=COMMAND_TEXT[upd_language(message)]["echo_message"], reply_markup=set_up_mode_markup)


@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["ru"]["done"])
@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["en"]["done"])
async def complete_settings_process(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Settings were set up\n'
                                       f'{COMMAND_TEXT[upd_language(callback)]["start"]}',
                                  reply_markup=start_markup)
    await state.set_state(default_state)


@router.message(StateFilter(FSMCustomer.settings))
async def echo_settings_message(message: Message):
    await message.answer(text=COMMAND_TEXT[upd_language(message)]["echo_message"], reply_markup=settings_markup)


# PURCHASE HANDLERS
@router.callback_query(StateFilter(default_state), F.data == BUTTON_TEXT["ru"]["purchase_start"])
@router.callback_query(StateFilter(default_state), F.data == BUTTON_TEXT["en"]["purchase_start"])
async def start_purchasing_process(callback: CallbackQuery, state: FSMContext):
    total_amount_basket = session.query(CustomerBasketSetting).filter(
        CustomerBasketSetting.customer_id == callback.from_user.id).first()
    total_amount_basket.current_sum = 0
    set_up_limit_of_basket = session.query(CustomerSetting).filter(
        CustomerSetting.customer_id == callback.from_user.id).first()
    session.commit()
    await callback.message.answer(text=f'{COMMAND_TEXT[upd_language(callback)]["purchase_start"]}\n\n'
                                       f'{COMMAND_TEXT[upd_language(callback)]["current_limit_of_basket"]} '
                                       f'{set_up_limit_of_basket.basket_limit if set_up_limit_of_basket else 0}\n\n'
                                       f'{COMMAND_TEXT[upd_language(callback)]["enter_price"]}',
                                  reply_markup=purchase_markup)
    await state.set_state(FSMCustomer.purchases)


@router.message(StateFilter(FSMCustomer.purchases), CheckBasketLimitInput())
async def enter_price_purchasing_process(message: Message):
    input_price = convert_str_float_to_float(message)
    current_limit_of_basket = session.query(CustomerSetting).filter(
        CustomerSetting.customer_id == message.from_user.id).first()
    total_amount_basket = session.query(CustomerBasketSetting).filter(
        CustomerBasketSetting.customer_id == message.from_user.id).first()
    total_amount_basket.current_sum = total_amount_basket.current_sum + input_price
    until_set_limit = current_limit_of_basket.basket_limit - total_amount_basket.current_sum
    session.commit()
    await message.answer(text=f'{COMMAND_TEXT[upd_language(message)]["done"]}\n\n'
                              f'{COMMAND_TEXT[upd_language(message)]["total_amount_basket"]} '
                              f'{total_amount_basket.current_sum}\n'
                              f'{COMMAND_TEXT[upd_language(message)]["current_limit_of_basket"]} '
                              f'{current_limit_of_basket.basket_limit if current_limit_of_basket else 0}\n'
                              f'{COMMAND_TEXT[upd_language(message)]["until_set_limit" if until_set_limit > 0 else "exceeding_limit"]} '
                              f'{until_set_limit}\n\n'
                              f'{COMMAND_TEXT[upd_language(message)]["enter_price_short"]}',
                         reply_markup=purchase_markup)


@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["ru"]["info"])
@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["en"]["info"])
async def info_current_basket(callback: CallbackQuery):
    total_amount_basket = session.query(CustomerBasketSetting).filter(
        CustomerBasketSetting.customer_id == callback.from_user.id).first()
    current_limit_of_basket = session.query(CustomerSetting).filter(
        CustomerSetting.customer_id == callback.from_user.id).first()
    until_set_limit = current_limit_of_basket.basket_limit - total_amount_basket.current_sum
    await callback.message.answer(
        text=f'{COMMAND_TEXT[upd_language(callback)]["total_amount_basket"]} '
             f'{total_amount_basket.current_sum if total_amount_basket else 0}\n\n'
             f'{COMMAND_TEXT[upd_language(callback)]["current_limit_of_basket"]} '
             f'{current_limit_of_basket.basket_limit if current_limit_of_basket else 0}\n'
             f'{COMMAND_TEXT[upd_language(callback)]["until_set_limit" if until_set_limit > 0 else "exceeding_limit"]} '
             f'{until_set_limit}\n\n'
             f'{COMMAND_TEXT[upd_language(callback)]["enter_price"]}',
        reply_markup=purchase_markup)


@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["ru"]["purchase_end"])
@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["en"]["purchase_end"])
async def end_purchasing_mode(callback: CallbackQuery, state: FSMContext):
    total_amount_basket = session.query(CustomerBasketSetting).filter(
        CustomerBasketSetting.customer_id == callback.from_user.id).first()
    current_limit_of_basket = session.query(CustomerSetting).filter(
        CustomerSetting.customer_id == callback.from_user.id).first()
    until_set_limit = current_limit_of_basket.basket_limit - total_amount_basket.current_sum
    await callback.message.answer(
        text=f'{COMMAND_TEXT[upd_language(callback)]["total_amount_basket"]} '
             f'{total_amount_basket.current_sum if total_amount_basket else 0}\n\n'
             f'{COMMAND_TEXT[upd_language(callback)]["current_limit_of_basket"]} '
             f'{current_limit_of_basket.basket_limit if current_limit_of_basket else 0}\n'
             f'{COMMAND_TEXT[upd_language(callback)]["until_set_limit" if until_set_limit < 0 else "exceeding_limit"]} '
             f'{until_set_limit}\n\n',
        reply_markup=end_purchase_markup)
    await state.set_state(default_state)


@router.message(StateFilter(FSMCustomer.purchases))
async def echo_purchase_message(message: Message):
    await message.answer(text=COMMAND_TEXT[upd_language(message)]["echo_message"], reply_markup=purchase_markup)


@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["ru"]["silent"])
@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["en"]["silent"])
async def set_bot_mode_purchasing_process(callback: CallbackQuery):
    set_bot_mode = session.query(CustomerSetting).filter(CustomerSetting.customer_id == callback.from_user.id).first()
    set_bot_mode.bot_mode = BotMode.SILENT
    session.commit()
    await callback.message.edit_text(text=f'{COMMAND_TEXT[upd_language(callback)]["set_up_bot_mode_done"]}\n\n'
                                          f'{COMMAND_TEXT[upd_language(callback)]["enter_price"]}',
                                     reply_markup=purchase_markup)


# MAIN
@router.callback_query(F.data == BUTTON_TEXT["ru"]["main_menu"])
@router.callback_query(F.data == BUTTON_TEXT["en"]["main_menu"])
async def return_to_main_menu(callback: CallbackQuery):
    await callback.message.answer(text=COMMAND_TEXT[upd_language(callback)]['start'], reply_markup=start_markup)


@router.callback_query(F.data == BUTTON_TEXT["ru"]["help"])
@router.callback_query(F.data == BUTTON_TEXT["en"]["help"])
async def help_callback(callback: CallbackQuery):
    await callback.message.answer(text=COMMAND_TEXT[upd_language(callback)]['help'], reply_markup=back_markup)


@router.callback_query(F.data == BUTTON_TEXT["ru"]["back"])
@router.callback_query(F.data == BUTTON_TEXT["en"]["back"])
async def back_callback(callback: CallbackQuery):
    await callback.message.answer(text=COMMAND_TEXT[upd_language(callback)]['start'], reply_markup=start_markup)


@router.callback_query(F.data == BUTTON_TEXT["ru"]["cancel"])
@router.callback_query(F.data == BUTTON_TEXT["en"]["cancel"])
async def cancel_and_return_to_main_menu(callback: CallbackQuery):
    await callback.message.edit_text(text=COMMAND_TEXT[upd_language(callback)]['start'], reply_markup=start_markup)


@router.message(StateFilter(default_state))
async def echo_message(message: Message):
    await message.answer(text=COMMAND_TEXT[upd_language(message)]["echo_message"], reply_markup=echo_markup)
