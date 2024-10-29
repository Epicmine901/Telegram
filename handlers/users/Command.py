from aiogram.types import Message,ContentType,CallbackQuery,InputFile
from loader import db,dp,languages
from keyboards.inline.Menu import til
from utils.db_api.Tables import html_Table


@dp.message_handler(is_admin=True,content_types=ContentType.PHOTO)
async def get_file_id_p(message: Message):
    await message.reply(message.photo[-1].file_id)
    
@dp.message_handler(commands=['SQL'],is_admin=True)
async def sql(msg:Message):
    #try:
    await msg.answer(db.SQL_Command(" ".join(msg.text.split()[1:])))
    #except:await msg.answer("Error")

@dp.message_handler(is_admin=True,commands=['update_language'])
async def update_language(msg: Message):
    for i in ['RU','UZ','EN']:
        a=await msg.answer(f"Updating {i} language...")
        db.execute(f"DELETE FROM {i}",commit=True,log=False)
        await a.delete()
        db.execute(f"INSERT INTO {i} VALUES {languages(i)}",commit=True,log=False)
        await msg.answer(f"Updated {i} language!")
        
@dp.message_handler(commands=['language'])
async def language(msg: Message):
    await msg.answer(db.GetLang(db.getUserLang(msg.from_id),"TEXT:Choise_language"),reply_markup=til)
@dp.callback_query_handler(in_list=['Language'])
async def language(call:CallbackQuery):
    await call.message.answer(db.GetLang(db.getUserLang(call.from_user.id),"TEXT:Choise_language"),reply_markup=til)
    
@dp.callback_query_handler(in_list=['UZ','EN','RU'])
async def change_language(call: CallbackQuery):
    db.execute(f"UPDATE Users SET Language = '{call.data}' WHERE User_ID = {call.from_user.id}",commit=True)
    await call.message.delete()
    await call.answer(db.GetLang(db.getUserLang(call.from_user.id),"TEXT:Changed_language"),show_alert=False)
    
@dp.message_handler(commands=['Tables'],is_admin=True)
async def Tables(msg:Message):
    html_Table().HTML()
    await msg.answer_document(InputFile("data/index.html"))