from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboard.utils_kb import create_inline_kb_from_buttons
from lexicon.text_buttons import BUTTON_TEXT


# ENGLISH BUTTONS
en_back_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["back"], callback_data=BUTTON_TEXT["en"]["back"])
en_cancel_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["cancel"], callback_data=BUTTON_TEXT["en"]["cancel"])
en_change_basket_limit_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["change_basket_limit"],
                                                  callback_data=BUTTON_TEXT["en"]["change_basket_limit"])
en_done_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["done"], callback_data=BUTTON_TEXT["en"]["done"])
en_help_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["help"], callback_data=BUTTON_TEXT["en"]["help"])
en_info_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["info"], callback_data=BUTTON_TEXT["en"]["info"])
en_normal_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["normal"], callback_data=BUTTON_TEXT["en"]["normal"])
en_purchase_end_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["purchase_end"],
                                           callback_data=BUTTON_TEXT["en"]["purchase_end"])
en_purchase_start_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["purchase_start"],
                                             callback_data=BUTTON_TEXT["en"]["purchase_start"])
en_settings_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["settings"], callback_data=BUTTON_TEXT["en"]["settings"])
en_set_up_basket_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["set_up_basket_limit"],
                                            callback_data=BUTTON_TEXT["en"]["set_up_basket_limit"])
en_set_up_mode_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["set_up_bot_mode"],
                                          callback_data=BUTTON_TEXT["en"]["set_up_bot_mode"])
en_silent_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["silent"], callback_data=BUTTON_TEXT["en"]["silent"])
en_main_menu_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["main_menu"],
                                        callback_data=BUTTON_TEXT["en"]["main_menu"])


# ENGLISH KEYBOARDS
en_start_markup = create_inline_kb_from_buttons(3, [en_settings_btn, en_purchase_start_btn, en_help_btn])
en_back_markup = create_inline_kb_from_buttons(1, [en_back_btn])
en_settings_markup = create_inline_kb_from_buttons(3, [en_set_up_basket_btn, en_set_up_mode_btn, en_done_btn])
en_set_up_mode_markup = create_inline_kb_from_buttons(2, [en_normal_btn, en_silent_btn])
en_purchase_markup = create_inline_kb_from_buttons(3, [en_info_btn, en_purchase_end_btn, en_silent_btn])
en_end_purchase_markup = create_inline_kb_from_buttons(2, [en_main_menu_btn, en_purchase_start_btn, en_settings_btn,
                                                           en_help_btn])
en_echo_markup = create_inline_kb_from_buttons(4, [en_main_menu_btn, en_settings_btn, en_purchase_start_btn,
                                                   en_help_btn])
