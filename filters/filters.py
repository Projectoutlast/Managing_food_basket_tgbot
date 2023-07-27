from aiogram.filters import BaseFilter
from aiogram.types import Message


class CheckBasketLimitInput(BaseFilter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: Message) -> bool | dict[str, float]:
        try:
            result = float(message.text)
            return {"basket_limit": result}
        except ValueError:
            return False
