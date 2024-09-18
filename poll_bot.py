import time
import asyncio
import aioschedule
import logging
import datetime

from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN = "BOT'S TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def choose_your_dinner():
    date = datetime.today().isoweekday()

    if date not in [6, 7]:
        await bot.send_poll('GROUP CHAT ID', 'Presence at work', ['Working', 'On sick leave', 'Vacation'],
                            is_anonymous=False, is_closed=False)


async def scheduler():
    aioschedule.every().day.at('09:00').do(choose_your_dinner)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dp):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
