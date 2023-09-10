import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import questions, commands


load_dotenv()
TOKEN = os.getenv("TOKEN")


async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(commands.command_router, questions.question_router)
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
