from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

@dp.callback_query_handler(get_Data=False)
@dp.message_handler(CommandHelp(),get_txt=True)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    await message.answer("\n".join(text))
