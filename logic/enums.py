from enum import Enum


class BotMode(Enum):
    silent: str = 'silent'
    normal: str = 'normal'


class BotLanguage(Enum):
    ru: str = 'ru'
    en: str = 'en'
