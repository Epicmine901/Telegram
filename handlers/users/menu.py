from aiogram.types import CallbackQuery,Message

from keyboards.inline.menu import menu
from loader import dp
from data.config import photos

load={
    "Menu":0,
    "BIO":1,
    "Link":2,
    "Rezyume":3
    }
txt={"Menu":"","BIO":"","Link":"","Rezyume":""}
txt["BIO"] = "<b>Ismi-sharifi: </b>Otajon Bozorboyev\n"   
txt["BIO"] += "<b>Tug'ilgan yili va joyi:</b> 8-yanvar 1999-yil Jizzax viloyati, Jizzax shahri.\n"
txt["BIO"] += "<b>Ta'limi:</b> Toshkent temir yo'l transport kasb-hunar kolleji Buxgalteriya hisobi va audit (2015-2018);\n"
txt["BIO"] += "<b>Ish tajribasi: </b>Jizzax temir yo'l masofasi xodimlar bo'limi ish o'rganuvchisi (2018-2019);\n"
txt["BIO"] += "Jizzax temir yo'l masofasi xodimlar bo'limi nazoratchisi (2019-2023);\n"
txt["BIO"] += "Astro Education o'quv markazi dasturlash kursi mentori (2023-hozirgacha)\n"
txt["BIO"] += "<b>Texnik ko'nikmalari: \n</b>"
txt["BIO"] += "C, Python, Django, Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot, Adobe Photoshop, Web Scraping, Parsing, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n\n"
txt["BIO"] += "<b>Tillar: \n</b>"
txt["BIO"] += "O'zbek tili (Ona tili);\n"
txt["BIO"] += "Ingliz tili (B2);\n"
txt["BIO"] += "Arab tili (O'qiy olish)."
@dp.callback_query_handler(in_list=menu)
async def menu_handler(call:CallbackQuery):
    #await call.message.delete()
    with open("photo_ID.txt","r") as file:
        a=file.read().split()
    try:
        await call.message.answer_photo(a[load[call.data]],caption=txt[call.data],reply_markup=menu[call.data])
    except:
        b=await call.message.answer_photo(photos[call.data],reply_markup=menu[call.data])
        a[load[call.data]]=b.photo[-1].file_id
        print(f"{call.data} file id replaced")
    await call.message.delete()
    with open("photo_ID.txt","w") as file:
        file.write(" ".join(a))
        


@dp.message_handler(is_admin=True,commands=['reload'])
async def reload_command(msg:Message):
    with open("photo_ID.txt","r") as file:
        file
    with open("photo_ID.txt","w") as file:
        for i in photos.values():
            a = await msg.answer_photo(i)
            file.write(f"{a.photo[-1].file_id} ")
            await a.delete()
    print("Reloaded")