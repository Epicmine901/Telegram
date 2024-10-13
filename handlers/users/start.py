from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.menu import menu
from loader import dp
from data.config import photos

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    with open("photo_ID.txt","r") as file:
        a=file.read().split()
    try:
        await message.answer_photo(a[0],reply_markup=menu["Menu"])
    except:
        b=await message.answer_photo(photos["Menu"],reply_markup=menu["Menu"])
        a[0]=b.photo[-1].file_id
        print("Menu file id replaced")
    with open("photo_ID.txt","w") as file:
        file.write(" ".join(a))
    
