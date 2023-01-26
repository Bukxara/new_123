from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.replykeyboardmarkup import numbers
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    markup = await numbers()
    await message.answer(f"Salom, {message.from_user.full_name}! So'z kiriting.")
