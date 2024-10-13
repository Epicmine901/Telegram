from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery

class ListFilter(BoundFilter):
    key = "in_list"
    def __init__(self,in_list):
        self.in_list = in_list
    async def check(self,call:CallbackQuery):
        return call.data in self.in_list
