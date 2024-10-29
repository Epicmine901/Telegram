from aiogram import executor
from loader import dp,db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)
    try:
        db.create_Kurslar()
    except:None
    try:
        db.create_Xodimlar()
    except:None
    try:
        db.create_main()
    except:None
    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,timeout=1)
