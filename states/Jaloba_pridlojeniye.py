from aiogram.dispatcher.filters.state import StatesGroup, State

class claiming(StatesGroup):
    name = State()
    claim = State()
