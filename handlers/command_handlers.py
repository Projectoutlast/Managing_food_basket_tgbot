from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from data_base.base import session
from data_base.models import Customer, CustomerFSM, CustomerBasketSetting, CustomerSetting
from keyboard.hybrid_language_kb import back_markup, start_markup
from lexicon.text_commands import COMMAND_TEXT
from utils.utils import get_user_language

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    user_is_exist = session.query(Customer).filter(Customer.user_id_telegram == message.from_user.id).first()
    if not user_is_exist:
        new_customer = Customer(user_id_telegram=message.from_user.id,
                                first_name=message.from_user.first_name,
                                user_name=message.from_user.last_name)
        customer_settings = CustomerSetting(customer_id=new_customer.user_id_telegram,
                                            bot_language=message.from_user.language_code)
        customer_state = CustomerFSM(customer_id=new_customer.user_id_telegram)
        customer_basket_settings = CustomerBasketSetting(customer_id=new_customer.user_id_telegram)

        session.add_all([new_customer, customer_settings, customer_state, customer_basket_settings])
        session.commit()
    user_language = get_user_language(message)
    await message.answer(text=COMMAND_TEXT[user_language]['start'], reply_markup=start_markup(user_language))


@router.message(Command(commands='help'))
async def cmd_help(message: Message):
    user_language = get_user_language(message)
    await message.answer(text=COMMAND_TEXT[user_language]['help'], reply_markup=back_markup(user_language))


@router.message(Command(commands='ru'))
async def switch_ru_language(message: Message):
    user_language = session.query(CustomerSetting).filter(CustomerSetting.customer_id == message.from_user.id).first()
    user_language.bot_language = "ru"
    session.commit()
    user_language = get_user_language(message)
    await message.answer(text=f'{COMMAND_TEXT[user_language]["switch_ru"]}\n'
                              f'{COMMAND_TEXT[user_language]["start"]}', reply_markup=start_markup(user_language))


@router.message(Command(commands='en'))
async def switch_en_language(message: Message):
    user_language = session.query(CustomerSetting).filter(CustomerSetting.customer_id == message.from_user.id).first()
    user_language.bot_language = "en"
    session.commit()
    user_language = get_user_language(message)
    await message.answer(text=f'{COMMAND_TEXT[user_language]["switch_en"]}\n'
                              f'{COMMAND_TEXT[user_language]["start"]}', reply_markup=start_markup(user_language))
