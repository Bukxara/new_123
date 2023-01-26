from aiogram import types

from loader import dp

from googletrans import Translator

from keyboards.inline.inlinekeyboards import languages

from aiogram.dispatcher.filters import Text


translator = Translator()
# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    langs = await languages()
    global word
    word = message.text
    await message.answer("Qaysi tilni tanlaysiz", reply_markup = langs)

@dp.callback_query_handler(Text(startswith = "languages_"))
async def language_choice(call: types.CallbackQuery):
    idx = call.data.index("_")
    tarjima = translator.translate(word, dest = call.data[idx+1:])
    await call.message.answer(tarjima.text)
