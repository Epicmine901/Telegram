from aiogram.types import InlineKeyboardMarkup as In_Button,InlineKeyboardButton as BT, InputFile
from loader import db,dp
def menus(key=None,lang=None):
    if key == "Loby":
        return In_Button(
        inline_keyboard=[
                [BT(db.GetLang(lang,"keyboard:Menu"),callback_data="Menu")],
                [BT(db.GetLang(lang,"🌍Language"),callback_data="Language")],
            ]
        )
    if key == "Menu":
        return In_Button(
        inline_keyboard=[
            [BT(db.GetLang(lang,"keyboard:Xodimlar"), callback_data="Xodimlar"),BT(db.GetLang(lang,"keyboard:Kurslar"), callback_data="Kurslar")],
            [BT(db.GetLang(lang,"keyboard:About"), callback_data="About"),BT(db.GetLang(lang,"keyboard:Vakansiya"), callback_data="Vakansiya")],
            [BT(db.GetLang(lang,"keyboard:boglanish"), url="https://t.me/obozorboyev_bot")],
            [BT(db.GetLang(lang,"keyboard:settings"),callback_data="settings")],
            #[BT(db.GetLang(lang,"🌍Language"),callback_data="Language")],
            #[BT(db.GetLang(lang,"keyboard:ortga"), callback_data="Loby")],  
            ]  
        )
    if key == "Xodimlar":
        return In_Button(
        inline_keyboard=oson(list(map(lambda x:[{"text":x[1],"callback_data":f"Xodimlar {x[0]}"}],db.Get("Xodimlar"))))+[[BT(db.GetLang(lang,"keyboard:ortga"), callback_data="Menu")]]
        )
    if key == "Kurslar":
        return In_Button(
        inline_keyboard=oson(list(map(lambda x: [{"text":x[1],"callback_data":f"Kurslar {x[0]}"}],db.Get("Kurslar"))))+[[BT(db.GetLang(lang,"keyboard:ortga"), callback_data="Menu")]]
        )
    if key == "About":
        return In_Button(
        inline_keyboard=[
                [BT(db.GetLang(lang,"keyboard:boglanish"), url="https://t.me/obozorboyev_bot"),BT(db.GetLang(lang,"keyboard:ortga"),callback_data="Menu")]
            ]
        )
    if key == "settings":
        return In_Button(
        inline_keyboard=[
                [BT(db.GetLang(lang,"keyboard:taklif"),callback_data="Claim Taklif"),BT(db.GetLang(lang,"keyboard:shikoyat"),callback_data="Claim Jaloba")],
                [BT(db.GetLang(lang,"🌍Language"),callback_data="Language")],
                [BT(db.GetLang(lang,"keyboard:ortga"), callback_data="Menu")],
            ]
        )

    return ['Loby','Menu','Xodimlar','About','Kurslar',"settings"]

def Caption(str,lang):
    return db.GetLang(lang,f"caption:{str}").replace("<br>",'\n')
    
    

def Photos(key):
    photo={}
    for x in db.Get("PHOTO"):
        photo[x[0]]=x[1]
    return photo[key]
def profil(Link,name,yozilish=None,id=None,is_admin=None,lang=None):
    return In_Button(
        inline_keyboard=[
                [BT(db.GetLang(lang,"keyboard:boglanish"),url=Link)]+([BT(db.GetLang(lang,"keyboard:yozilish"),callback_data=f"Link {yozilish}")]if yozilish else []),
                [BT(db.GetLang(lang,"keyboard:ortga"), callback_data=name)],
                #[BT("DELETE",callback_data=f"DEL {name} {id}")] if is_admin else [],
            ]
        )
def delete(name,id,lang):
    return In_Button(
        inline_keyboard=[
                [BT(db.GetLang(lang,"keyboard:False"),callback_data=f"{name} {id}"),BT(db.GetLang(lang,"keyboard:True"),callback_data=f"DELTRUE {name} {id}")]
            ]
        )

def oson(x:list):
    a=[]
    temp={}
    for i in x:
        if "dev" in i[0]['text'].lower():
            if temp:
                a.append([temp])
            a.append(i)
            temp = {}
        elif temp:
            a.append([temp,i[0]])
            temp = {}
        else:
            temp = i[0]
    if temp:
        a.append([temp])
    return a

reset = In_Button(
    inline_keyboard=[
        [BT("🔙", callback_data="RESET")]
        ]
    )
back = In_Button(
    inline_keyboard=[
        [BT("🔙", callback_data="Menu")]
        ]
    )

til = In_Button(
    inline_keyboard=[
        [BT(text="O'zbek",callback_data="UZ")],
        [BT(text="Руский",callback_data="RU")],
        [BT(text="English",callback_data="EN")],
        ]
    )

def answer(id):
    return In_Button(
        inline_keyboard=[
            [BT(text=f"Answer", callback_data=f"Answer {id}")]
            ]
    )