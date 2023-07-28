from aiogram.filters import BaseFilter
from aiogram.types import Message


class CheckBasketLimitInput(BaseFilter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: Message) -> bool | dict[str, float]:
        input_message = message.text
        if ',' in input_message:
            input_message = input_message.replace(',', '.')
        try:
            result = float(input_message)
            return {"user_input": result}
        except ValueError:
            return False
