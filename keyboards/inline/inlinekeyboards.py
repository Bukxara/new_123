from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language = {
	"ru": "Русский",
	"en": "English"
}

async def languages():
	buttons = InlineKeyboardMarkup(row_width = 2)
	for key, val in language.items():
		buttons.insert(
			InlineKeyboardButton(text = val, callback_data = f"languages_{key}"))
	return buttons