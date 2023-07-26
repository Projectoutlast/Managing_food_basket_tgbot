COMMAND_TEXT = {
    'ru': {
        'start': "Привет!\n"
                 "Я простой помощник для ваших покупок в супермаркете. "
                 "Надеюсь, вы слышали о кассах самообслуживания в супермаркетах со сканерами."
                 "Моя возможность предназначена для подсчета текущей суммы в корзине при покупке в супермаркете.\n"
                 "Меня просто использовать:\n"
                 "1) Настройте параметры (не обязательно)\n"
                 "2) Нажмите кнопку 'Начать покупку' и пришлите мне цену.\n"
                 "Я посчитаю вашу текущую сумму корзины и, если вы хотите ее настроить, "
                 "рассчитаю лимит вашей корзины (сколько осталось до или на сколько превышен установленный лимит). "
                 "Когда вы нажимаете кнопку «Завершить покупку», я отправляю вам информацию о ваших "
                 "общих покупках (выводимая информация зависит от ваших настроек).\n"
                 "Если вы хотите узнать о настройке режима бота, лимита корзины и языка меню, "
                 "погрузитесь в мою справочную книгу, используя команду /help.",

        'help': "Здесь вы можете узнать немного больше обо мне.\n\n"
                "Лимит корзины\n"
                "Если вы установите лимит своей корзины в настройках, то я могу рассчитать текущий лимит корзины "
                "и до установленного лимита/превышения установленного лимита. Кроме того, я отправлю вам уведомление, "
                "когда вы превысите лимит установленной корзины.\n\n"
                "Режимы бота\n"
                "У меня два режима работы.\n"
                "Обычный режим: когда вы отправляете мне цену в процессе покупки, я каждый раз присылаю вам ответное "
                "сообщение с некоторой информацией (общая сумма корзины (все время), текущий лимит корзины "
                "(если это указано) и до установки лимит или превышение установленного лимита "
                "(если указан текущий лимит корзины).\n"
                "Тихий режим: когда вы присылаете мне цену в процессе покупки, я не отвечаю, но могу выслать "
                "вам информацию по запросу - кнопка 'Информация'. Информация та же, что и в обычном режиме. "
                "Когда вы завершите процесс покупки, я отправлю вам общее сообщение в обоих режимах.\n\n"
                "Язык меню\n"
                "В основном, я могу определить, какой язык настроен в вашем приложении Telegram "
                "(эта информация хранится внутри ваших отправленных сообщений), и использовать язык на основе "
                "этой информации. Но иногда могут быть ошибки, и если они есть, вы можете просто отправить мне одну "
                "из следующих команд:\n"
                "/en - установить английский язык"
                "/ru - установить русский язык",

        'settings': "Добро пожаловать в настройки!\n\n"
                    "Настройте лимит продуктовой корзины и режим бота, используя встроенные кнопки ниже.\n"
                    "Для отмены процесса настройки нажмите кнопку «Отмена» ниже или отправьте мне команду /cancel.",

        'set_up_basket_limit': "Установить лимит продуктовой корзины\n\n"
                               "Введите номер без пробела.\n"
                               "Примеры «1», «1.00», «1.36», «1,00», «1,36»",

        'set_up_basket_limit_done': "Лимит корзины установлен.",

        'invalid_input_basket_limit': "Введено неверное значение.\n\n"
                                      "Ввод должен содержать только цифры, без пробелов или каких-либо символов, "
                                      "как показано в примере\n"
                                      "«1», «1.00», «1.36», «1,00», «1,36»",

        'set_up_bot_mode': "Выберите режим бота, нажав одну из кнопок ниже.\n\n"
                           "Если вам нужна дополнительная информация о режимах бота, отправьте мне команду /help.",

        'set_up_bot_mode_done': "Режим бота установлен.",

        'purchase_start': "Процесс покупки запущен.",

        'current_limit_of_basket': "Текущий лимит корзины",

        'total_amount_basket': "Общая сумма корзины",

        'until_set_limit': "До установленного лимита",

        'exceeding_limit': "Превышение установленного лимита",

        'purchase_end': "Процесс покупки завершен.",

        'silent_mode_on': "Был установлен беззвучный режим.",

        'normal_mode_on': "Установлен нормальный режим",
    },
    'en': {
        'start': "Hello!\nI'm simple helper for your purchases in a supermarket.\n"
                 "I hope you heard about self-checkout in supermarkets with scanners. "
                 "My capability is intended to help count the current amount in the basket when you are "
                 "purchasing in a supermarket. It's simple to use me:\n"
                 "1) Set up settings (not required)\n"
                 "2) Push the 'Start purchasing' button and send me the price.\n"
                 "I will count your current basket amount and, if you wish to set it up, "
                 "calculate your basket limit (how many until the ceiling or exceeding the established limit). "
                 "When you push the 'End purchasing' button, "
                 "I send you information about your total purchases "
                 "(the output information depends on your settings).\n"
                 "If you want to know about setting up bot mode, basket limit, and menu language, "
                 "then dive into my helpbook using the /help command.",

        'help': "Here, you can learn a little bit more about me.\n\n"
                "Basket limit\n"
                "If you set up your basket limit in settings, then I can calculate the current "
                "basket limit and until set limit/exceeding the established limit. "
                "Also, I will send you a notification when you exceeding your set-up basket limit.\n\n"
                "Bot modes\n"
                "I have two modes of work.\n"
                "Normal mode: when you send me the price during the purchase process, "
                "I will send you a reply message with some information each time (total amount of basket (all time), "
                "current basket limit (if this is pointed out), and until set limit or exceeding the established limit "
                "(if the current basket limit is pointed out).\n"
                "Silent mode: when you send me the price during the purchase process, "
                "I don't reply, but I can send you information by demand - the 'Info' button. "
                "The information is the same as in normal mode. When you end the purchasing process, "
                "I send you a total message in both modes.\n\n "
                "Menu language\n"
                "Mainly, I can distinguish what language is set up in your Telegram app "
                "(this information is stored inside your sent messages) and use language based on this information. "
                "But sometimes there can be mistakes, and if there are, "
                "you can just send me one of the next commands:\n"
                "/en - set up english language"
                "/ru - установить русский язык",

        'settings': "Welcome to settings!\n\n"
                    "Set up your food basket limit and bot mode using in-line buttons below.\n"
                    "For cancel settings process push the «Cancel» button below or send me /cancel command.",

        'set_up_basket_limit': "Set up food basket limit\n\n"
                               "Enter number without space.\n"
                               "Examples «1», «1.00», «1.36», «1,00», «1,36»",

        'set_up_basket_limit_done': "Basket limit was set.",

        'invalid_input_basket_limit': "Invalid value entered.\n\n"
                                      "Enter must contain only digits, without spaces or any character as shown "
                                      "in the example\n"
                                      "«1», «1.00», «1.36», «1,00», «1,36»",

        'set_up_bot_mode': "Choose bot mode pushed one of buttons below.\n\n"
                           "If you need more information about bot modes send me /help command.",

        'set_up_bot_mode_done': "Bot mode was set.",

        'purchase_start': "Purchasing process is started.",

        'current_limit_of_basket': "Current limit of basket",

        'total_amount_basket': "Total amount basket",

        'until_set_limit': "Until set limit",

        'exceeding_limit': "Exceeding the established limit",

        'purchase_end': "Purchasing process is ended.",

        'silent_mode_on': "Silent mode was set.",

        'normal_mode_on': "Normal mode was set",
    },
}
