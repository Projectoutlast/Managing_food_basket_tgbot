from aiogram.types import CallbackQuery, Message

from data_base.base import session
from data_base.models import CustomerSetting

from logic.enums import BotMode


def get_user_language(data: Message | CallbackQuery | None = None) -> str | None:

    """
    Get information about set up customer's language from CustomerSetting table
    """

    entity = session.query(CustomerSetting).filter(CustomerSetting.customer_id == data.from_user.id).first()
    return entity.bot_language if entity else "ru"


def convert_str_float_to_float(message: Message) -> float:

    """
    Convert incoming str float to float
    """

    input_message = message.text
    if ',' in input_message:
        input_message = input_message.replace(',', '.')
    result = float(input_message)

    return round(result, 2)


def check_mode(data: Message | CallbackQuery) -> BotMode:

    """
    Func check customer's settings bot mode
    """

    user_mode = session.query(CustomerSetting).filter(CustomerSetting.customer_id == data.from_user.id).first()
    return user_mode.bot_mode
