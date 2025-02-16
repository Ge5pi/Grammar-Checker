import logging
import os
import nest_asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.environ["TOKEN"])
dis = Dispatcher()

nest_asyncio.apply()


@dis.message(CommandStart())
async def start(message: Message):
    text = f"Hi! I am a bot to check your grammar and punctuation. Send me your message and I will edit it."
    await message.answer(text, parse_mode="Markdown")
