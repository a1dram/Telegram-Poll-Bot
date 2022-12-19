import time
from datetime import datetime
import schedule
import asyncio
import aioschedule
import logging
import datetime
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN = "5648224518:AAG7Anqgd1LmsTaf3Z8NTx7ByuSQ8CfLOVs"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def choose_your_dinner():
    date = datetime.today().isoweekday()

    if date != 6 and date != 7:
        await bot.send_poll('-1001522185836', 'Присутствие на работе', ['Работаю', 'Больничный', 'Отпуск, отгул'],
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
