import logging
import os

from aiogram import Bot, Dispatcher

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.environ["TOKEN"])
dis = Dispatcher()
