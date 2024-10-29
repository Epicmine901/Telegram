from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import db,dp
from keyboards.inline.Menu import menus,Caption,Photos,oson
from utils.db_api.Tables import html_Table
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.delete()
    if not db.execute(f"SELECT * FROM Users WHERE User_ID = {message.from_id}",fetchone=True,log=False):
        db.execute("INSERT INTO Users(User,User_ID, Language) VALUES(?,?,?)",(message.from_user.full_name,message.from_id, 'UZ'),commit=True)
        print("New user")
    lang = db.getUserLang(message.from_id)
    await message.answer_photo(Photos("Loby"),Caption("Loby",lang),reply_markup=menus("Loby",lang))