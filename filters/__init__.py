from aiogram import Dispatcher

from loader import dp
from .Output import GetData,GetTXT
from .In_List import ListFilter
from .IS_ADMIN import AdminFilter
if __name__ == "filters":
    dp.filters_factory.bind(GetData)
    dp.filters_factory.bind(GetTXT)
    dp.filters_factory.bind(ListFilter)
    dp.filters_factory.bind(AdminFilter)
    pass
