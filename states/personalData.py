from aiogram.fsm.state import State, StatesGroup

class PersonalData(StatesGroup):
    fullname = State()
    email = State()
    phone = State()
