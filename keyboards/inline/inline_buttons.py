from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


usefull_send_message_ru = InlineKeyboardMarkup(
    inline_keyboard=
    [
       [
           InlineKeyboardButton(text="Перейти на сайт", callback_data="send_message", url="https://uztelecom.uz/ru/obratnaya-svyaz")
       ]
    ]
)

usefull_send_message_uz = InlineKeyboardMarkup(
    inline_keyboard=
    [
       [
           InlineKeyboardButton(text="Saytga o`tish", callback_data="send_message", url="https://uztelecom.uz/uz/qayta-aloqa")
       ]
    ]
)

usefull_cabinate_uz = InlineKeyboardMarkup(
    inline_keyboard=
    [
       [
           InlineKeyboardButton(text="Mobil aloqa", callback_data="cabinate", url="https://cabinet.uztelecom.uz/ps/scc/login.php?P_USER_LANG_ID=4")
       ],
       [
           InlineKeyboardButton(text="Internet", callback_data="cabinate", url="https://cabinet.uztelecom.uz/ps/scc/login.php?P_USER_LANG_ID=4")
       ]
    ]
)


usefull_cabinate_ru = InlineKeyboardMarkup(
    inline_keyboard=
    [
       [
           InlineKeyboardButton(text="Мобильная связь", callback_data="cabinate", url="https://cabinet.uztelecom.uz/ps/scc/login.php")
       ],
       [
           InlineKeyboardButton(text="Интернет", callback_data="cabinate", url="https://cabinet.uztelecom.uz/ps/scc/login.php")
       ]
    ]
)


add_service_ru = InlineKeyboardMarkup(
    inline_keyboard=
    [
       [
           InlineKeyboardButton(text="Мобильная связь", callback_data="mobile_add")
       ],
       [
           InlineKeyboardButton(text="Интернет", callback_data="internet_add")
       ]
    ]
)


add_service_uz = InlineKeyboardMarkup(
    inline_keyboard=
    [
       [
           InlineKeyboardButton(text="Mobil aloqa", callback_data="mobile_add")
       ],
       [
           InlineKeyboardButton(text="Internet", callback_data="internet_add")
       ]
    ]
)