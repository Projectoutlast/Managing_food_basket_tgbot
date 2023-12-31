import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import config
from data_base.base import engine
from data_base.models import *
from handlers import command_handlers, callback_handlers


logger = logging.getLogger(__name__)


async def main():
    Base.metadata.create_all(engine)
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting bot')

    bot = Bot(token=config.TG_BOT.TOKEN, parse_mode='Markdown')
    dp = Dispatcher()

    dp.include_router(command_handlers.router)
    dp.include_router(callback_handlers.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
