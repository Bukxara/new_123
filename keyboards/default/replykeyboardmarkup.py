from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def numbers():
	buttons = ReplyKeyboardMarkup(row_width = 3, resize_keyboard = True)
	for i in range(1, 10):
		buttons.insert(
			KeyboardButton(text = i))
	return buttons