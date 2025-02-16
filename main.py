import asyncio
import logging
import os
import nest_asyncio
from g4f.client import Client
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


@dis.message()
async def handle_message(message: Message):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": f"Hi! Check my text on grammar and punctuation mistakes: \"{message.text}\""},
            {"role": "system",
             "content": "Answer with this template and only like this: \"Corrected words:\n\nRules you should read:\", If you did not find mistakes, say it."}
        ]
    )
    await message.answer(response.choices[0].message.content)


async def main():
    await dis.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
