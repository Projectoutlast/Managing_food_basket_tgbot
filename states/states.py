from aiogram.filters.state import State, StatesGroup


class FSMCustomer(StatesGroup):
    settings: StatesGroup = State()
    purchases: StatesGroup = State()
