from aiogram.types import InlineKeyboardMarkup

from keyboard.en_keyboards import (en_start_markup, en_back_markup, en_settings_markup, en_set_up_mode_markup,
                                   en_purchase_markup, en_end_purchase_markup, en_echo_markup)
from keyboard.ru_keyboards import (ru_start_markup, ru_back_markup, ru_settings_markup, ru_set_up_mode_markup,
                                   ru_purchase_markup, ru_end_purchase_markup, ru_echo_markup)


# Functions return in-line keyboard from demand language
def start_markup(language: str) -> InlineKeyboardMarkup:
    match language:
        case "ru":
            return ru_start_markup
        case "en":
            return en_start_markup


def back_markup(language: str) -> InlineKeyboardMarkup:
    match language:
        case "ru":
            return ru_back_markup
        case "en":
            return en_back_markup


def settings_markup(language: str) -> InlineKeyboardMarkup:
    match language:
        case "ru":
            return ru_settings_markup
        case "en":
            return en_settings_markup


def set_up_mode_markup(language: str) -> InlineKeyboardMarkup:
    match language:
        case "ru":
            return ru_set_up_mode_markup
        case "en":
            return en_set_up_mode_markup


def purchase_markup(language: str) -> InlineKeyboardMarkup:
    match language:
        case "ru":
            return ru_purchase_markup
        case "en":
            return en_purchase_markup


def end_purchase_markup(language: str) -> InlineKeyboardMarkup:
    match language:
        case "ru":
            return ru_end_purchase_markup
        case "en":
            return en_end_purchase_markup


def echo_markup(language: str) -> InlineKeyboardMarkup:
    match language:
        case "ru":
            return ru_echo_markup
        case "en":
            return en_echo_markup