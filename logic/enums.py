import enum
from sqlalchemy import Enum


class BotMode(enum.Enum):
    SILENT: str = 'silent'
    NORMAL: str = 'normal'


class FSMCustomerEnum(enum.Enum):
    DEFAULT_STATE: str = 'default_state'
    SETTINGS: str = 'settings'
    SET_UP_BASKET_LIMIT: str = 'set_up_basket_limit'
    SET_UP_BOT_MODE: str = 'set_up_bot_mode'
    PURCHASES: str = 'purchases'
