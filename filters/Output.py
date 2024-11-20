from data.config import ADMINS
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types.message import Message
from aiogram.types import CallbackQuery


class GetTXT(BoundFilter):
    key = 'get_txt'
    def __init__(self,get_txt):
        self.get_txt = get_txt
    async def check(self, message: Message):
        print(f"\x1b[32m[👤USER]:\x1b[0m{message.from_user.full_name},\x1b[32m[🆔]:\x1b[0m{message.from_user.id}",end=",")
        print(f"\x1b[32m[Text]:\x1b[31m\x1b[42m{message.text}\x1b[0m")
        return self.get_txt
    
class GetData(BoundFilter):
    key = 'get_Data'
    def __init__(self,get_Data):
        self.get_Data = get_Data
    async def check(self, call: CallbackQuery):
        print(f"\x1b[32m[👤USER]:\x1b[0m{call.from_user.full_name},\x1b[32m[🆔]:\x1b[0m{call.from_user.id}",end=",")
        print(f"\x1b[32m[DATA]:\x1b[31m\x1b[42m{call.data}\x1b[0m")
        return self.get_Data
