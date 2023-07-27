from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message
from aiogram.utils.formatting import Text

from filters.filters import CheckBasketLimitInput
from keyboard.keyboards import settings_markup, set_up_mode_markup, start_markup
from lexicon.text_buttons import BUTTON_TEXT
from lexicon.text_commands import COMMAND_TEXT
from states.states import FSMCustomer


router = Router()


@router.callback_query(F.data == BUTTON_TEXT["en"]["settings"])
async def settings(callback: CallbackQuery):
    await callback.message.edit_text(text=COMMAND_TEXT["en"]["settings"],
                                     reply_markup=settings_markup)


@router.callback_query(F.text(text=[BUTTON_TEXT["en"]["set_up_basket_limit"]]))
async def basket_limit_input(callback: CallbackQuery):
    await callback.message.edit_text(text=COMMAND_TEXT["en"]["set_up_basket_limit"])


@router.message(CheckBasketLimitInput())
async def set_up_basket_limit(message: Message, basket_limit: dict[str, float]):
    await message.edit_text(text=f'{COMMAND_TEXT["en"]["set_up_basket_limit_done"]}\n\n'
                                 f'{COMMAND_TEXT["en"]["set_up_bot_mode"]}',
                            reply_markup=set_up_mode_markup)


@router.callback_query(F.text(text=[BUTTON_TEXT["en"]["normal"], BUTTON_TEXT["en"]["silent"]]))
async def set_up_bot_mode(callback: CallbackQuery):
    await callback.message.edit_text(text=f'{COMMAND_TEXT["en"]["set_up_bot_mode_done"]}\n'
                                          f'{COMMAND_TEXT["en"]["start"]}',
                                     reply_markup=start_markup)
