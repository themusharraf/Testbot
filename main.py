import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from button import catalog

dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(5611541842, "Bot ishga tushdi!")


async def shutdown__answer(bot: Bot):
    await bot.send_message(5611541842, "Bot ishga to'xtadi!")


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f"O'zbekiston poytaxi qayer ? ", reply_markup=catalog)


@dp.callback_query(F.data == "a")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("Siz to'g'ri topdingiz ✅!", )


@dp.callback_query(F.data == "b" or F.data == "c" or F.data == "d")
async def check_button(callback: CallbackQuery):
    await callback.message.answer("Siz no'g'ri topdingiz ❗️!", )


async def main():
    await dp.start_polling(bot)
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown__answer)


if __name__ == "__main__":
    bot = Bot(token="6768144687:AAFHY5y4o4Uyjr7aeNKZD78kA9jNpNuYKyY")
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
