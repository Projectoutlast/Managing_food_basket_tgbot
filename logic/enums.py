from enum import Enum


class BotMode(Enum):
    SILENT: str = 'silent'
    NORMAL: str = 'normal'


class BotLanguage(Enum):
    RU: str = 'ru'
    EN: str = 'en'
