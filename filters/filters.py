from aiogram.filters import BaseFilter
from aiogram.types import Message


class CheckBasketLimitInput(BaseFilter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: Message) -> bool:
        input_message = message.text
        if ',' in input_message:
            input_message = input_message.replace(',', '.')
        try:
            result = float(input_message)
            return True
        except ValueError:
            return False
