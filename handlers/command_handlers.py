from aiogram import Router, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message

from keyboard.keyboards import back_markup, settings_markup, start_markup
from lexicon.text_buttons import BUTTON_TEXT
from lexicon.text_commands import COMMAND_TEXT


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=COMMAND_TEXT['en']['start'], reply_markup=start_markup)


@router.message(Command(commands='help'))
async def cmd_help(message: Message):
    await message.answer(text=COMMAND_TEXT['en']['help'], reply_markup=back_markup)


@router.message(Command(commands='ru'))
async def switch_ru_language(message: Message):
    await message.answer(text=f'{COMMAND_TEXT["ru"]["switch_ru"]}\n'
                              f'{COMMAND_TEXT["ru"]["start"]}', reply_markup=start_markup)


@router.message(Command(commands='en'))
async def switch_en_language(message: Message):
    await message.answer(text=f'{COMMAND_TEXT["en"]["switch_en"]}\n'
                              f'{COMMAND_TEXT["en"]["start"]}', reply_markup=start_markup)
