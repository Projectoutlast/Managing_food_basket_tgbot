from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message

from lexicon.text_commands import COMMAND_TEXT


router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def cmd_start(message: Message):
    await message.answer(text=COMMAND_TEXT['en']['start'])


@router.message(Command(commands='help'))
async def cmd_help(message: Message):
    await message.answer(text=COMMAND_TEXT['en']['help'])


@router.message(Command(commands='settings'))
async def cmd_settings(message: Message):
    await message.answer(text=COMMAND_TEXT['en']['settings'])
