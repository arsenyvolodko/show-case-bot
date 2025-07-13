import asyncio
import logging
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

API_DIR = Path(__file__).parent

load_dotenv(API_DIR / ".env")

BOT_TOKEN = os.environ.get("BOT_TOKEN")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

id1 = "25c823ec-a107-49c8-8832-41c18a8e7538"
id2 = "4276c23d-a0cf-4068-9c5a-72221a1434da"


@dp.message(CommandStart(deep_link=True))
async def start_handler(message: Message, command):
    content_id = command.args
    logger.info(f"User {message.from_user.id} used /start with content_id={content_id}")

    if content_id == id1:
        await message.answer(f"Тут контент для метки с id {id2}")
        await message.delete()
    elif content_id == id2:
        await message.answer(f"Тут контент для метки с id {id1}")
        await message.delete()


async def main():
    logger.info("Starting bot polling...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped.")
