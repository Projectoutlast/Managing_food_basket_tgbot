from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.text_buttons import BUTTON_TEXT


# buttons
back_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["back"], callback_data=BUTTON_TEXT["en"]["back"])
cancel_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["cancel"], callback_data=BUTTON_TEXT["en"]["cancel"])
change_basket_limit_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["change_basket_limit"],
                                               callback_data=BUTTON_TEXT["en"]["change_basket_limit"])
help_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["help"], callback_data=BUTTON_TEXT["en"]["help"])
info_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["info"], callback_data=BUTTON_TEXT["en"]["info"])
normal_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["normal"], callback_data=BUTTON_TEXT["en"]["normal"])
purchase_end_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["purchase_end"],
                                        callback_data=BUTTON_TEXT["en"]["purchase_end"])
purchase_start_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["purchase_start"],
                                          callback_data=BUTTON_TEXT["en"]["purchase_start"])
settings_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["settings"], callback_data=BUTTON_TEXT["en"]["settings"])
set_up_basket_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["set_up_basket_limit"],
                                         callback_data=BUTTON_TEXT["en"]["set_up_basket_limit"])
set_up_mode_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["set_up_mode"],
                                       callback_data=BUTTON_TEXT["en"]["set_up_mode"])
silent_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["silent"], callback_data=BUTTON_TEXT["en"]["silent"])

# keyboards
start_kb = [[settings_btn, purchase_start_btn, help_btn]]
start_markup = InlineKeyboardMarkup(inline_keyboard=start_kb)

back_markup = InlineKeyboardMarkup(inline_keyboard=[[back_btn]])

settings_kb = [[set_up_basket_btn, set_up_mode_btn, cancel_btn]]
settings_markup = InlineKeyboardMarkup(inline_keyboard=settings_kb)

set_up_mode_kb = [[normal_btn, silent_btn]]
set_up_mode_markup = InlineKeyboardMarkup(inline_keyboard=set_up_mode_kb)
