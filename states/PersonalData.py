from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData(StatesGroup):
    fullname = State()
    Rezyume = State()
    
class Link(StatesGroup):
    Corse = State()
    fullname = State()
    phone_number = State()