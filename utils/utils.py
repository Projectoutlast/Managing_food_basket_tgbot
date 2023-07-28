from aiogram.types import CallbackQuery, Message

from data_base.base import session
from data_base.models import CustomerSetting


def upd_language(entity: Message | CallbackQuery) -> str:

    """
    Func gets update and checks what language user use
    :param entity
    :return str
    """
    return entity.from_user.language_code


def db_language(data: Message | CallbackQuery | None = None) -> str | None:

    """
    Get information about set up customer's language from CustomerSetting table
    :return: str
    """

    entity = session.query(CustomerSetting).filter(CustomerSetting.customer_id == data.from_user.id).first()
    return entity.bot_language


def convert_str_float_to_float(message: Message) -> float:

    """
    Convert incoming str float to float
    :param message:
    :return float:
    """

    input_message = message.text
    if ',' in input_message:
        input_message = input_message.replace(',', '.')
    result = float(input_message)

    return round(result, 2)
