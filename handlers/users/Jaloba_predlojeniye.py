from aiogram.types import CallbackQuery,Message
from aiogram.dispatcher import FSMContext
from states.Jaloba_pridlojeniye import claiming
from loader import dp,db
from keyboards.inline.Menu import menus,Caption,Photos
from data.config import ADMINS
from time import sleep
@dp.callback_query_handler(_0_in_list=['Claim'])
async def claim(call:CallbackQuery,state:FSMContext):
    await call.message.delete()
    await claiming.name.set()
    name = call.data.split()[1]
    await state.update_data(
        {'name': name}
        )
    await claiming.claim.set()
    await call.message.answer(f"{name}ni yozing")
    
@dp.message_handler(state=claiming.claim)
async def claim(msg:Message,state:FSMContext):
    await state.update_data(
        {'claim': msg.text}
        )
    data = await state.get_data()
    name = data.get('name')
    claim = data.get('claim')
    await msg.answer(f"{name} Qabul qilindi")
    a  = f"<b>{name}</b>\n"
    a += f"Malumot:\n{claim}"
    for i in ADMINS:
        await dp.bot.send_message(i, a)
    await state.finish()
    sleep(3)
    lang = db.getUserLang(msg.from_id)
    await msg.answer_photo(Photos("Menu"),Caption("Menu",lang),reply_markup=menus("Menu",lang))




