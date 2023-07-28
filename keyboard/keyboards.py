from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboard.utils_kb import create_inline_kb_from_buttons
from lexicon.text_buttons import BUTTON_TEXT


# buttons
back_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["back"], callback_data=BUTTON_TEXT["en"]["back"])
cancel_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["cancel"], callback_data=BUTTON_TEXT["en"]["cancel"])
change_basket_limit_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["change_basket_limit"],
                                               callback_data=BUTTON_TEXT["en"]["change_basket_limit"])
done_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["done"], callback_data=BUTTON_TEXT["en"]["done"])
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
set_up_mode_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["set_up_bot_mode"],
                                       callback_data=BUTTON_TEXT["en"]["set_up_bot_mode"])
silent_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["silent"], callback_data=BUTTON_TEXT["en"]["silent"])
main_menu_btn = InlineKeyboardButton(text=BUTTON_TEXT["en"]["main_menu"], callback_data=BUTTON_TEXT["en"]["main_menu"])

# keyboards
start_markup = create_inline_kb_from_buttons(3, [settings_btn, purchase_start_btn, help_btn])

back_markup = create_inline_kb_from_buttons(1, [back_btn])

settings_markup = create_inline_kb_from_buttons(3, [set_up_basket_btn, set_up_mode_btn, done_btn])

set_up_mode_markup = create_inline_kb_from_buttons(2, [normal_btn, silent_btn])

purchase_markup = create_inline_kb_from_buttons(3, [info_btn, purchase_end_btn,
                                                    silent_btn])

end_purchase_markup = create_inline_kb_from_buttons(2, [main_menu_btn, purchase_start_btn, settings_btn, help_btn])

echo_markup = create_inline_kb_from_buttons(4, [main_menu_btn, settings_btn, purchase_start_btn, help_btn])
