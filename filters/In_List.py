from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery

class ListFilter(BoundFilter):
    key = "in_list"
    def __init__(self,in_list):
        self.in_list = in_list
    async def check(self,call:CallbackQuery):
        return call.data in self.in_list
    
class NotListFilter(BoundFilter):
    key = "not_in_list"
    def __init__(self,not_in_list):
        self.not_in_list = not_in_list
    async def check(self,call:CallbackQuery):
        return call.data not in self.not_in_list

class _0_indexListFilter(BoundFilter):
    key = "_0_in_list"
    def __init__(self,_0_in_list):
        self._0_in_list = _0_in_list
    async def check(self,call:CallbackQuery):
        return call.data.split()[0] in self._0_in_list
