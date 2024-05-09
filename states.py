from aiogram.dispatcher.filters.state import State, StatesGroup

class RegisterUserState(StatesGroup):
    name = State()
    yosh = State()
    adres = State()
    telefon = State()