from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from keyboards.inline.Menu import menus, Caption, Photos, reset, back ,answer
from loader import dp,db
from data.config import ADMINS
from states.PersonalData import PersonalData,Link
from time import sleep

@dp.callback_query_handler(in_list=['Vakansiya'])
async def enter_test(call:types.CallbackQuery):
    await call.message.answer("To'liq ismingizni kiriting")
    await PersonalData.fullname.set()
    
@dp.callback_query_handler(_0_in_list=['Link'])
async def enter_test(call:types.CallbackQuery, state: FSMContext):
    await call.message.answer("To'liq ismingizni kiriting")
    await Link.Corse.set()
    await state.update_data(
        {'Corse': " ".join(call.data.split()[1:])}
        )
    await Link.fullname.set()
    
@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    FIO = message.text
    await state.update_data(
        {'FIO': FIO}
        )
    await message.answer("Rezyumeingizni bering")
    await PersonalData.Rezyume.set()
        
@dp.message_handler(state=PersonalData.Rezyume,content_types=types.ContentTypes.DOCUMENT)
async def answer_fullname(message: types.Message, state: FSMContext):
    name = message.document.file_name
    if True:
        await state.update_data(
            {'File': message.document.file_id}
            )
        # Ma'lumotlarni qayta o'qiymiz:
        data = await state.get_data()
        FIO = data.get('FIO')
        File = data.get('File')
        msg = "Rezyume Qabul qilindi:\n"
        msg += f"Ismingiz - {FIO}\n"
        msg += f"File - {name}\n"
        await message.answer(msg,reply_markup=back)
        for i in ADMINS:
            await dp.bot.send_document(i,message.document.file_id, caption=msg, reply_markup=answer(message.from_id))
        await state.finish()
        await state.reset_state(with_data = False)
        sleep(3)
        lang = db.getUserLang(message.from_id)
        await message.answer_photo(Photos("Menu"),Caption("Menu",lang),reply_markup=menus("Menu",lang))
        
@dp.message_handler(state=Link.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    FIO = message.text
    await state.update_data(
        {'FIO': FIO}
        )
    await message.answer("Telefon raqmingizni kiriting")
    await Link.phone_number.set()
    
@dp.message_handler(state=Link.phone_number)
async def answer_fullname(message: types.Message, state: FSMContext):
    number = message.text
    await state.update_data(
        {'number': number}
        )
    data = await state.get_data()
    FIO = data.get('FIO')
    number = data.get('number')
    Corse = data.get('Corse')
    msg = "Zapros qabul qilindi:\n"
    msg += f"Kurs {Corse}\n"
    msg += f"Ismingiz - {FIO}\n"
    msg += f"File - {number}\n"
    await message.answer(msg)
    for i in ADMINS:
        await dp.bot.send_message(i, msg, reply_markup=answer(message.from_id))
    await state.finish()
    await state.reset_state(with_data = False)
    sleep(3)
    lang = db.getUserLang(message.from_id)
    await message.answer_photo(Photos("Menu"),Caption("Menu",lang),reply_markup=menus("Menu",lang))