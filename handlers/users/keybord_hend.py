from ast import Import
from aiogram.types import Message,CallbackQuery
from loader import db,dp
from keyboards.inline.Menu import menus,Caption,Photos,profil,delete
from data.config import ADMINS
from deep_translator import GoogleTranslator

@dp.callback_query_handler(in_list=menus())
async def menu_handler(call: CallbackQuery):
    lang = db.getUserLang(call.from_user.id)
    await call.message.answer_photo(Photos(call.data),Caption(call.data,lang),reply_markup=menus(call.data,lang))
    await call.message.delete()
    
@dp.callback_query_handler(_0_in_list=['Xodimlar',"Kurslar","DEL","DELTRUE"])
async def kurs_hodim(call: CallbackQuery):
    lang = db.getUserLang(call.from_user.id)
    admin=str(call.from_user.id) in ADMINS
    Type=call.data.split()
    if Type[0]== 'Xodimlar':
        data = db.Find(Type[0],Type[1])
        if lang != "UZ":
            caption=GoogleTranslator(source='uz', target=lang.lower()).translate(text=data[4].replace("<br>","\n").replace("<b>","not=<b>"))
            caption=caption.replace("not=<b>","<b>")
        else:
            caption=data[4].replace("<br>","\n")
        
        await call.message.answer_photo(data[3],caption,reply_markup=profil(data[5],Type[0],None,data[0],admin,lang))
        
    if Type[0]== "Kurslar":
        data = db.Find(Type[0],Type[1])
        if lang != "UZ":
            caption=GoogleTranslator(source='uz', target=lang.lower()).translate(text=data[3].replace("<br>","\n").replace("<b>","not=<b>"))
            caption=caption.replace("not=<b>","<b>")
        else:
            caption=data[3].replace("<br>","\n")
        try:
            await call.message.answer_photo(data[2],caption,reply_markup=profil(data[-1],Type[0],data[1],data[0],admin,lang))
        except:
            await call.message.answer_video(data[2],caption,reply_markup=profil(data[-1],Type[0],data[1],data[0],admin,lang))
        
    if Type[0]== "DEL":
        data = db.Find(Type[1],Type[2])
        await call.message.answer(f"{data[1]} Ochirasizmi",reply_markup=delete(Type[1],Type[2],lang))
        
    if Type[0]== "DELTRUE":
        db.delete(Type[1],Type[2])
        await call.message.answer_photo(Photos[Type[1]],Caption(Type[1],lang),reply_markup=menus(Type[1],lang))
    await call.message.delete()
    

