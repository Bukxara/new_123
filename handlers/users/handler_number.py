from aiogram import types
from loader import dp

@dp.message_handler(text = "1")
async def number_handler(message: types.Message):
	await message.reply("The number 1 is chosen")