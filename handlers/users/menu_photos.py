from aiogram.types import CallbackQuery, ContentTypes,Message
from loader import dp
from aiogram import types
from keyboards.inline.menu_photo import menu


@dp.message_handler(content_types=types.ContentType.PHOTO,is_admin=True)
async def get_file_id_p(message: types.Message):
    await message.delete()
    await message.answer_photo(message.photo[-1].file_id,reply_markup=menu)
    




@dp.callback_query_handler(in_list=['0','1','2','3'])
async def change(call:CallbackQuery):
    with open("photo_ID.txt","r") as file:
        a=file.read().split()
    a[int(call.data)]=call.message.photo[-1].file_id
    with open("photo_ID.txt","w") as file:
        file.write(" ".join(a))
    with open(f"photos/{call.data}.jpg","wb")as f:
        b=await dp.bot.download_file_by_id(call.message.photo[-1].file_id)
        f.write(b.getbuffer())
    await call.message.delete()
    

    