from aiogram.types import InlineKeyboardMarkup as In_Button,InlineKeyboardButton as BT

menu = In_Button(
    inline_keyboard=[
            [BT(text="Menu",callback_data=0),BT(text="BIO",callback_data=1)],
            [BT(text="Link",callback_data=2),BT(text="Rezyume",callback_data=3)],    
        ]
    )
