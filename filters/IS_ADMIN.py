from data.config import ADMINS
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types.message import Message
from aiogram.types import CallbackQuery
class AdminFilter(BoundFilter):
    key = "is_admin"
    def __init__(self,is_admin):
        self.is_admin = is_admin
    async def check(self,msg:Message):
        if str(msg.from_id) in ADMINS:
            return self.is_admin
        else:
            await msg.delete()
            return not self.is_admin
