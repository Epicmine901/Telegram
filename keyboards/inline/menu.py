from aiogram.types import InlineKeyboardMarkup as In_Button,InlineKeyboardButton as BT

menu = {
    "Menu":In_Button(
        inline_keyboard=[
                [BT(text="📇BIO",callback_data="BIO"),BT(text="🔗Link",callback_data="Link")],
                [BT(text="🧾Rezyume",callback_data="Rezyume"),BT(text="📞Kontakt",url="https://t.me/obozorboyev_bot")]
            ]
        ),
    "BIO":In_Button(
        inline_keyboard=[
                [BT(text="🔙",callback_data="Menu")],
            ]
        ),
    "Link":In_Button(
        inline_keyboard=[
                [BT(text="🔗GitHub",url="https://github.com/otajonbozorboyev"),BT(text="🔗Telegram",url="https://t.me/otajonbozorboyev")],
                [BT(text="🔗LinkedIn",url="https://www.linkedin.com/in/otajonbozorboyev/"),BT(text="🔗LeetCode",url="https://leetcode.com/otajonbozorboyev571/")],
                [BT(text="🔙",callback_data="Menu")]
            ]
        ),    
    "Rezyume":In_Button(
        inline_keyboard=[
                [BT(text="🧾Download",url="https://drive.google.com/file/d/1HPCI2UAjqvElNceKinhvrDsRf0M4oaT8/view?usp=sharing")],
                [BT(text="🔙",callback_data="Menu")]
            ]
        )
}
