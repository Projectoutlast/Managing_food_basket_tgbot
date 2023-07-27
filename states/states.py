from aiogram.filters.state import State, StatesGroup


class FSMCustomer(StatesGroup):
    settings: State = State()
    set_up_basket_limit: State = State()
    set_up_bot_mode: State = State()
    purchases: State = State()
