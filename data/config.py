from environs import Env
from aiogram.types import InputFile

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")

photos={
    "Menu":InputFile(path_or_bytesio=env.str("photo1")),
    "BIO":InputFile(path_or_bytesio=env.str("photo2")),
    "Link":InputFile(path_or_bytesio=env.str("photo3")),
    "Rezyume":InputFile(path_or_bytesio=env.str("photo4"))
}


