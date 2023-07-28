from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message

from filters.filters import CheckBasketLimitInput
from keyboard.keyboards import (end_purchase_markup, purchase_markup, back_markup, echo_markup,
                                settings_markup, set_up_mode_markup, start_markup)
from lexicon.text_buttons import BUTTON_TEXT
from lexicon.text_commands import COMMAND_TEXT
from states.states import FSMCustomer


router = Router()


# SETTINGS HANDLERS
@router.callback_query(F.data == BUTTON_TEXT["en"]["settings"])
async def settings(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=COMMAND_TEXT["en"]["settings"], reply_markup=settings_markup)
    await state.set_state(FSMCustomer.settings)


@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["en"]["set_up_basket_limit"])
async def basket_limit_input(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=COMMAND_TEXT["en"]["set_up_basket_limit"])
    await state.set_state(FSMCustomer.set_up_basket_limit)


@router.message(StateFilter(FSMCustomer.set_up_basket_limit), CheckBasketLimitInput())
async def set_up_basket_limit(message: Message, state: FSMContext, user_input: dict[str, float]):
    await message.answer(text=f'{COMMAND_TEXT["en"]["set_up_basket_limit_done"]}\n\n'
                              f'{COMMAND_TEXT["en"]["settings"]}', reply_markup=settings_markup)
    await state.set_state(FSMCustomer.settings)


@router.message(StateFilter(FSMCustomer.set_up_basket_limit))
async def echo_set_up_basket_limit_message(message: Message):
    await message.answer(text="I don't know what you mean\n"
                              f"{COMMAND_TEXT['en']['enter_price']}")


@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["en"]["set_up_bot_mode"])
async def basket_limit_input(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=COMMAND_TEXT["en"]["set_up_bot_mode"], reply_markup=set_up_mode_markup)
    await state.set_state(FSMCustomer.set_up_bot_mode)


@router.callback_query(StateFilter(FSMCustomer.set_up_bot_mode), F.data == BUTTON_TEXT["en"]["normal"])
async def set_up_bot_mode(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=f'{COMMAND_TEXT["en"]["set_up_bot_mode_done"]}\n'
                                          f'{COMMAND_TEXT["en"]["settings"]}',
                                     reply_markup=settings_markup)
    await state.set_state(FSMCustomer.settings)


@router.callback_query(StateFilter(FSMCustomer.set_up_bot_mode), F.data == BUTTON_TEXT["en"]["silent"])
async def set_up_bot_mode(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=f'{COMMAND_TEXT["en"]["set_up_bot_mode_done"]}\n'
                                          f'{COMMAND_TEXT["en"]["settings"]}',
                                     reply_markup=settings_markup)
    await state.set_state(FSMCustomer.settings)


@router.message(StateFilter(FSMCustomer.set_up_bot_mode))
async def echo_set_up_bot_mode_message(message: Message):
    await message.answer(text=COMMAND_TEXT["en"]["echo_message"], reply_markup=set_up_mode_markup)


@router.callback_query(StateFilter(FSMCustomer.settings), F.data == BUTTON_TEXT["en"]["done"])
async def complete_settings_process(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Settings were set up\n'
                                       f'{COMMAND_TEXT["en"]["start"]}',
                                  reply_markup=start_markup)
    await state.set_state(default_state)


@router.message(StateFilter(FSMCustomer.settings))
async def echo_settings_message(message: Message):
    await message.answer(text=COMMAND_TEXT["en"]["echo_message"], reply_markup=settings_markup)


# PURCHASE HANDLERS
@router.callback_query(StateFilter(default_state), F.data == BUTTON_TEXT["en"]["purchase_start"])
async def start_purchasing_process(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=f'{COMMAND_TEXT["en"]["purchase_start"]}\n\n'
                                       f'{COMMAND_TEXT["en"]["current_limit_of_basket"]} {10}\n'
                                       f'{COMMAND_TEXT["en"]["enter_price"]}',
                                  reply_markup=purchase_markup)
    await state.set_state(FSMCustomer.purchases)


@router.message(StateFilter(FSMCustomer.purchases), CheckBasketLimitInput())
async def enter_price_purchasing_process(message: Message, user_input: dict[str, float]):
    await message.answer(text=f'{COMMAND_TEXT["en"]["done"]}\n\n'
                              f'{COMMAND_TEXT["en"]["total_amount_basket"]}\n'
                              f'{COMMAND_TEXT["en"]["current_limit_of_basket"]}\n'
                              f'{COMMAND_TEXT["en"]["until_set_limit"]}\n\n'
                              f'{COMMAND_TEXT["en"]["enter_price_short"]}',
                         reply_markup=purchase_markup)


@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["en"]["info"])
async def info_current_basket(callback: CallbackQuery):
    await callback.message.answer(text=f'{COMMAND_TEXT["en"]["total_amount_basket"]}\n\n'
                                       f'{COMMAND_TEXT["en"]["current_limit_of_basket"]} {10}\n'
                                       f'{COMMAND_TEXT["en"]["enter_price"]}',
                                  reply_markup=purchase_markup)


@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["en"]["purchase_end"])
async def end_purchasing_mode(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=f'{COMMAND_TEXT["en"]["total_amount_basket"]}\n'
                                       f'{COMMAND_TEXT["en"]["current_limit_of_basket"]}\n'
                                       f'{COMMAND_TEXT["en"]["until_set_limit"]}',
                                  reply_markup=end_purchase_markup)
    await state.set_state(default_state)


@router.message(StateFilter(FSMCustomer.purchases))
async def echo_purchase_message(message: Message):
    await message.answer(text=COMMAND_TEXT["en"]["echo_message"], reply_markup=purchase_markup)


@router.callback_query(StateFilter(FSMCustomer.purchases), F.data == BUTTON_TEXT["en"]["silent"])
async def set_bot_mode_purchasing_process(callback: CallbackQuery):
    await callback.message.edit_text(text=f'{COMMAND_TEXT["en"]["set_up_bot_mode_done"]}\n'
                                          f'{COMMAND_TEXT["en"]["enter_price"]}', reply_markup=purchase_markup)


# MAIN
@router.callback_query(F.data == BUTTON_TEXT["en"]["main_menu"])
async def return_to_main_menu(callback: CallbackQuery):
    await callback.message.answer(text=COMMAND_TEXT['en']['start'], reply_markup=start_markup)


@router.callback_query(F.data == BUTTON_TEXT["en"]["help"])
async def help_callback(callback: CallbackQuery):
    await callback.message.answer(text=COMMAND_TEXT['en']['help'],
                                  reply_markup=back_markup)


@router.callback_query(F.data == BUTTON_TEXT["en"]["back"])
async def back_callback(callback: CallbackQuery):
    await callback.message.answer(text=COMMAND_TEXT['en']['start'], reply_markup=start_markup)


@router.callback_query(F.data == BUTTON_TEXT["en"]["cancel"])
async def cancel_and_return_to_main_menu(callback: CallbackQuery):
    await callback.message.edit_text(text=COMMAND_TEXT['en']['start'], reply_markup=start_markup)


@router.message(StateFilter(default_state))
async def echo_message(message: Message):
    await message.answer(text=COMMAND_TEXT["en"]["echo_message"],
                         reply_markup=echo_markup)
