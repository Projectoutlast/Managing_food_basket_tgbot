from aiogram.types import InlineKeyboardButton

from keyboard.utils_kb import create_inline_kb_from_buttons
from lexicon.text_buttons import BUTTON_TEXT


# RUSSIAN BUTTONS
ru_back_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["back"], callback_data=BUTTON_TEXT["ru"]["back"])
ru_cancel_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["cancel"], callback_data=BUTTON_TEXT["ru"]["cancel"])
ru_change_basket_limit_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["change_basket_limit"],
                                                  callback_data=BUTTON_TEXT["ru"]["change_basket_limit"])
ru_done_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["done"], callback_data=BUTTON_TEXT["ru"]["done"])
ru_help_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["help"], callback_data=BUTTON_TEXT["ru"]["help"])
ru_info_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["info"], callback_data=BUTTON_TEXT["ru"]["info"])
ru_normal_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["normal"], callback_data=BUTTON_TEXT["ru"]["normal"])
ru_purchase_end_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["purchase_end"],
                                           callback_data=BUTTON_TEXT["ru"]["purchase_end"])
ru_purchase_start_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["purchase_start"],
                                             callback_data=BUTTON_TEXT["ru"]["purchase_start"])
ru_settings_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["settings"], callback_data=BUTTON_TEXT["ru"]["settings"])
ru_set_up_basket_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["set_up_basket_limit"],
                                            callback_data=BUTTON_TEXT["ru"]["set_up_basket_limit"])
ru_set_up_mode_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["set_up_bot_mode"],
                                          callback_data=BUTTON_TEXT["ru"]["set_up_bot_mode"])
ru_silent_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["silent"], callback_data=BUTTON_TEXT["ru"]["silent"])
ru_main_menu_btn = InlineKeyboardButton(text=BUTTON_TEXT["ru"]["main_menu"],
                                        callback_data=BUTTON_TEXT["ru"]["main_menu"])


# RUSSIAN KEYBOARDS
ru_start_markup = create_inline_kb_from_buttons(3, [ru_settings_btn, ru_purchase_start_btn, ru_help_btn])
ru_back_markup = create_inline_kb_from_buttons(1, [ru_back_btn])
ru_settings_markup = create_inline_kb_from_buttons(3, [ru_set_up_basket_btn, ru_set_up_mode_btn, ru_done_btn])
ru_set_up_mode_markup = create_inline_kb_from_buttons(2, [ru_normal_btn, ru_silent_btn])
ru_purchase_markup = create_inline_kb_from_buttons(3, [ru_info_btn, ru_purchase_end_btn, ru_silent_btn])
ru_end_purchase_markup = create_inline_kb_from_buttons(2, [ru_main_menu_btn, ru_purchase_start_btn, ru_settings_btn,
                                                           ru_help_btn])
ru_echo_markup = create_inline_kb_from_buttons(4, [ru_main_menu_btn, ru_settings_btn, ru_purchase_start_btn,
                                                   ru_help_btn])
