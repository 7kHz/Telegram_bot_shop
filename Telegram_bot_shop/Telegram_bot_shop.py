import asyncio

from aiogram import Bot, Dispatcher, types
import logging
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message()
async def start(message: types.Message):
    if message.text == "/start":
        await message.answer("Бот работает! 🔑 (aiogram v3.x)\nПривет Макс!!!")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

