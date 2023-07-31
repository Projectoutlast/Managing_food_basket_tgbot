from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message

from data_base.base import session
from data_base.models import CustomerBasketSetting, CustomerSetting
from filters.filters import CheckBasketLimitInput
from keyboard.hybrid_language_kb import (end_purchase_markup, purchase_markup, back_markup, echo_markup,
                                         settings_markup, set_up_mode_markup, start_markup)
from lexicon.text_buttons import BUTTON_TEXT
from lexicon.text_commands import COMMAND_TEXT
from logic.enums import BotMode
from states.states import FSMCustomer
from utils.utils import convert_str_float_to_float, check_mode, get_user_language


router = Router()


# SETTINGS HANDLERS
@router.callback_query(F.data == BUTTON_TEXT["en"]["settings"])
@router.callback_query(F.data == BUTTON_TEXT["ru"]["settings"])
async def settings(callback: CallbackQuery, state: FSMContext):
    user_language = get_user_language(callback)
    await callback.message.edit_text(text=COMMAND_TEXT[user_language]["settings"],
                                     reply_markup=settings_markup(user_language))
    await state.set_state(FSMCustomer.settings)


@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["en"]["set_up_basket_limit"])
@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["ru"]["set_up_basket_limit"])
async def basket_limit_input(callback: CallbackQuery, state: FSMContext):
    user_language = get_user_language(callback)
    await callback.message.edit_text(text=COMMAND_TEXT[user_language]["set_up_basket_limit"])
    await state.set_state(FSMCustomer.set_up_basket_limit)


@router.message(StateFilter(FSMCustomer.set_up_basket_limit), CheckBasketLimitInput())
async def set_up_basket_limit(message: Message, state: FSMContext):
    input_price = convert_str_float_to_float(message)
    basket_limit = session.query(CustomerSetting).filter(CustomerSetting.customer_id == message.from_user.id).first()
    basket_limit.basket_limit = input_price
    session.commit()
    user_language = get_user_language(message)
    await message.answer(text=f'{COMMAND_TEXT[user_language]["set_up_basket_limit_done"]}\n\n'
                              f'{COMMAND_TEXT[user_language]["settings"]}', reply_markup=settings_markup(user_language))
    await state.set_state(FSMCustomer.settings)


@router.message(StateFilter(FSMCustomer.set_up_basket_limit))
async def echo_set_up_basket_limit_message(message: Message):
    user_language = get_user_language(message)
    await message.answer(text=f"{COMMAND_TEXT[user_language]['dont_know']}\n"
                              f"{COMMAND_TEXT[user_language]['enter_price']}")


@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["en"]["set_up_bot_mode"])
@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["ru"]["set_up_bot_mode"])
async def basket_limit_input(callback: CallbackQuery, state: FSMContext):
    user_language = get_user_language(callback)
    await callback.message.edit_text(text=COMMAND_TEXT[user_language]["set_up_bot_mode"],
                                     reply_markup=set_up_mode_markup(user_language))
    await state.set_state(FSMCustomer.set_up_bot_mode)


@router.callback_query(StateFilter(FSMCustomer.set_up_bot_mode), F.data == BUTTON_TEXT["en"]["normal"])
@router.callback_query(StateFilter(FSMCustomer.set_up_bot_mode), F.data == BUTTON_TEXT["ru"]["normal"])
async def set_up_bot_mode(callback: CallbackQuery, state: FSMContext):
    set_bot_mode = session.query(CustomerSetting).filter(CustomerSetting.customer_id == callback.from_user.id).first()
    set_bot_mode.bot_mode = BotMode.NORMAL
    session.commit()
    user_language = get_user_language(callback)
    await callback.message.edit_text(text=f'{COMMAND_TEXT[user_language]["set_up_bot_mode_done"]}\n'
                                          f'{COMMAND_TEXT[user_language]["settings"]}',
                                     reply_markup=settings_markup(user_language))
    await state.set_state(FSMCustomer.settings)


@router.callback_query(StateFilter(FSMCustomer.set_up_bot_mode), F.data == BUTTON_TEXT["en"]["silent"])
@router.callback_query(StateFilter(FSMCustomer.set_up_bot_mode), F.data == BUTTON_TEXT["ru"]["silent"])
async def set_up_bot_mode(callback: CallbackQuery, state: FSMContext):
    set_bot_mode = session.query(CustomerSetting).filter(CustomerSetting.customer_id == callback.from_user.id).first()
    set_bot_mode.bot_mode = BotMode.SILENT
    session.commit()
    user_language = get_user_language(callback)
    await callback.message.edit_text(text=f'{COMMAND_TEXT[user_language]["set_up_bot_mode_done"]}\n'
                                          f'{COMMAND_TEXT[user_language]["settings"]}',
                                     reply_markup=settings_markup(user_language))
    await state.set_state(FSMCustomer.settings)


@router.message(StateFilter(FSMCustomer.set_up_bot_mode))
async def echo_set_up_bot_mode_message(message: Message):
    user_language = get_user_language(message)
    await message.edit_text(text=COMMAND_TEXT[user_language]["echo_message"],
                            reply_markup=set_up_mode_markup(user_language))


@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["en"]["done"])
@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["ru"]["done"])
async def complete_settings_process(callback: CallbackQuery, state: FSMContext):
    user_language = get_user_language(callback)
    await callback.message.edit_text(text=f'{COMMAND_TEXT[user_language]["settings_was_set"]}\n'
                                          f'{COMMAND_TEXT[user_language]["start"]}',
                                     reply_markup=start_markup(user_language))
    await state.set_state(default_state)


@router.message(StateFilter(FSMCustomer.settings))
async def echo_settings_message(message: Message):
    user_language = get_user_language(message)
    await message.edit_text(text=COMMAND_TEXT[user_language]["echo_message"],
                            reply_markup=settings_markup(user_language))


# PURCHASE HANDLERS
@router.callback_query(StateFilter(default_state), F.data == BUTTON_TEXT["en"]["purchase_start"])
@router.callback_query(StateFilter(default_state), F.data == BUTTON_TEXT["ru"]["purchase_start"])
async def start_purchasing_process(callback: CallbackQuery, state: FSMContext):
    total_amount_basket = session.query(CustomerBasketSetting).filter(
        CustomerBasketSetting.customer_id == callback.from_user.id).first()
    total_amount_basket.current_sum = 0
    set_up_limit_of_basket = session.query(CustomerSetting).filter(
        CustomerSetting.customer_id == callback.from_user.id).first()
    session.commit()
    user_language = get_user_language(callback)
    await callback.message.edit_text(text=f'{COMMAND_TEXT[user_language]["purchase_start"]}\n\n'
                                          f'{COMMAND_TEXT[user_language]["current_limit_of_basket"]} '
                                          f'{set_up_limit_of_basket.basket_limit if set_up_limit_of_basket else 0}\n\n'
                                          f'{COMMAND_TEXT[user_language]["enter_price"]}',
                                     reply_markup=purchase_markup(user_language))
    await state.set_state(FSMCustomer.purchases)


@router.message(StateFilter(FSMCustomer.purchases), CheckBasketLimitInput())
async def enter_price_purchasing_process(message: Message):
    user_language = get_user_language(message)
    user_mode = check_mode(message)
    input_price = convert_str_float_to_float(message)

    total_amount_basket = session.query(CustomerBasketSetting).filter(
        CustomerBasketSetting.customer_id == message.from_user.id).first()
    total_amount_basket.current_sum = total_amount_basket.current_sum + input_price
    session.commit()

    match user_mode:
        case BotMode.NORMAL:
            current_limit_of_basket = session.query(CustomerSetting).filter(
                CustomerSetting.customer_id == message.from_user.id).first()
            until_set_limit = current_limit_of_basket.basket_limit - total_amount_basket.current_sum
            await message.answer(text=f'{COMMAND_TEXT[user_language]["done"]}\n\n'
                                      f'{COMMAND_TEXT[user_language]["total_amount_basket"]} '
                                      f'{total_amount_basket.current_sum}\n'
                                      f'{COMMAND_TEXT[user_language]["current_limit_of_basket"]} '
                                      f'{current_limit_of_basket.basket_limit if current_limit_of_basket else 0}\n'
                                      f'{COMMAND_TEXT[user_language]["until_set_limit" if until_set_limit > 0 else "exceeding_limit"]} '
                                      f'{until_set_limit}\n\n'
                                      f'{COMMAND_TEXT[user_language]["enter_price_short"]}',
                                 reply_markup=purchase_markup(user_language))
        case BotMode.SILENT:
            await message.answer(text=f'{COMMAND_TEXT[user_language]["done"]}\n\n'
                                      f'{COMMAND_TEXT[user_language]["enter_price_short"]}',
                                 reply_markup=purchase_markup(user_language))


@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["en"]["info"])
@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["ru"]["info"])
async def info_current_basket(callback: CallbackQuery):
    user_language = get_user_language(callback)
    total_amount_basket = session.query(CustomerBasketSetting).filter(
        CustomerBasketSetting.customer_id == callback.from_user.id).first()
    current_limit_of_basket = session.query(CustomerSetting).filter(
        CustomerSetting.customer_id == callback.from_user.id).first()
    until_set_limit = current_limit_of_basket.basket_limit - total_amount_basket.current_sum
    await callback.message.edit_text(
        text=f'{COMMAND_TEXT[user_language]["total_amount_basket"]} '
             f'{total_amount_basket.current_sum if total_amount_basket else 0}\n\n'
             f'{COMMAND_TEXT[user_language]["current_limit_of_basket"]} '
             f'{current_limit_of_basket.basket_limit if current_limit_of_basket else 0}\n'
             f'{COMMAND_TEXT[user_language]["until_set_limit" if until_set_limit > 0 else "exceeding_limit"]} '
             f'{until_set_limit}\n\n'
             f'{COMMAND_TEXT[user_language]["enter_price"]}',
        reply_markup=purchase_markup(user_language))


@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["en"]["purchase_end"])
@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["ru"]["purchase_end"])
async def end_purchasing_mode(callback: CallbackQuery, state: FSMContext):
    user_language = get_user_language(callback)
    total_amount_basket = session.query(CustomerBasketSetting).filter(
        CustomerBasketSetting.customer_id == callback.from_user.id).first()
    current_limit_of_basket = session.query(CustomerSetting).filter(
        CustomerSetting.customer_id == callback.from_user.id).first()
    until_set_limit = current_limit_of_basket.basket_limit - total_amount_basket.current_sum
    await callback.message.edit_text(
        text=f'{COMMAND_TEXT[user_language]["total_amount_basket"]} '
             f'{total_amount_basket.current_sum if total_amount_basket else 0}\n\n'
             f'{COMMAND_TEXT[user_language]["current_limit_of_basket"]} '
             f'{current_limit_of_basket.basket_limit if current_limit_of_basket else 0}\n'
             f'{COMMAND_TEXT[user_language]["until_set_limit" if until_set_limit < 0 else "exceeding_limit"]} '
             f'{until_set_limit}\n\n',
        reply_markup=end_purchase_markup(user_language))
    await state.set_state(default_state)


@router.message(StateFilter(FSMCustomer.purchases))
async def echo_purchase_message(message: Message):
    user_language = get_user_language(message)
    await message.answer(text=COMMAND_TEXT[user_language]["echo_message"], reply_markup=purchase_markup(user_language))


@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["en"]["silent"])
@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["ru"]["silent"])
async def set_bot_mode_purchasing_process(callback: CallbackQuery):
    user_language = get_user_language(callback)
    set_bot_mode = session.query(CustomerSetting).filter(CustomerSetting.customer_id == callback.from_user.id).first()
    set_bot_mode.bot_mode = BotMode.SILENT
    session.commit()
    await callback.message.edit_text(text=f'{COMMAND_TEXT[user_language]["set_up_bot_mode_done"]}\n\n'
                                          f'{COMMAND_TEXT[user_language]["enter_price"]}',
                                     reply_markup=purchase_markup(user_language))


# MAIN
@router.callback_query(F.data == BUTTON_TEXT["en"]["main_menu"])
@router.callback_query(F.data == BUTTON_TEXT["ru"]["main_menu"])
async def return_to_main_menu(callback: CallbackQuery):
    user_language = get_user_language(callback)
    await callback.message.edit_text(text=COMMAND_TEXT[user_language]['start'],
                                     reply_markup=start_markup(user_language))


@router.callback_query(F.data == BUTTON_TEXT["en"]["help"])
@router.callback_query(F.data == BUTTON_TEXT["ru"]["help"])
async def help_callback(callback: CallbackQuery):
    user_language = get_user_language(callback)
    await callback.message.edit_text(text=COMMAND_TEXT[user_language]['help'], reply_markup=back_markup(user_language))


@router.callback_query(F.data == BUTTON_TEXT["en"]["back"])
@router.callback_query(F.data == BUTTON_TEXT["ru"]["back"])
async def back_callback(callback: CallbackQuery):
    user_language = get_user_language(callback)
    await callback.message.edit_text(text=COMMAND_TEXT[user_language]['start'],
                                     reply_markup=start_markup(user_language))


@router.callback_query(F.data == BUTTON_TEXT["en"]["cancel"])
@router.callback_query(F.data == BUTTON_TEXT["ru"]["cancel"])
async def cancel_and_return_to_main_menu(callback: CallbackQuery):
    user_language = get_user_language(callback)
    await callback.message.edit_text(text=COMMAND_TEXT[user_language]['start'],
                                     reply_markup=start_markup(user_language))


@router.message(StateFilter(default_state))
async def echo_message(message: Message):
    user_language = get_user_language(message)
    await message.answer(text=COMMAND_TEXT[user_language]["echo_message"], reply_markup=echo_markup(user_language))
