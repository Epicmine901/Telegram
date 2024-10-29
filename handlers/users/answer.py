from aiogram.types import CallbackQuery,Message
from loader import dp,db
from states.answer import Answer
from aiogram.dispatcher import FSMContext
@dp.callback_query_handler(_0_in_list=['Answer'])
async def answer(call:CallbackQuery,state: FSMContext):
    data = db.execute(f"SELECT * FROM Users WHERE user_id = '{call.data.split()[1]}'",fetchone=True)
    await call.message.answer(f"{data[0]} Userga javob yozing")
    await state.update_data({'ID': call.data.split()[1]})
    await Answer.msg.set()
    
@dp.message_handler(state=Answer.msg)
async def answer_msg(message: Message, state: FSMContext):
    data = await state.get_data()
    ID = data.get('ID')
    msg = message.text
    await dp.bot.send_message(ID,f"Admin sizga javob berdi:\n{msg}")
    await message.answer("Sobsheniye yuborildi")
    await state.finish()