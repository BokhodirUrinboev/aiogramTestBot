from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

usefull_uz_button = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="📟 USSD komandalar")
     ],
     [
        KeyboardButton(text="👤 Shaxsiy kabinet")
     ],
     [
        KeyboardButton(text="✉️ Murojaat yuborish")
     ],
     [
        KeyboardButton(text="ℹ️IMEI-kod bo'yicha ma'lumot")
     ],
     [
        KeyboardButton(text="🏢 Kompaniya haqida")
     ],
     [
        KeyboardButton(text="🏠 Bosh sahifaga")
     ]

    ],
    resize_keyboard=True
)

usefull_ru_button = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="📟 USSD команды")
     ],
     [
        KeyboardButton(text="👤 Личный кабинет")
     ],
     [
        KeyboardButton(text="✉️ Отправить обращение")
     ],
     [
        KeyboardButton(text="ℹ️Информация по IMEI-коду")
     ],
     [
        KeyboardButton(text="🏢 О Компании")
     ],
     [
        KeyboardButton(text="🏠 На главную")
     ]

    ],
    resize_keyboard=True
)

ussd_command_ru_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="GSM Тарифы"),
            KeyboardButton(text="GSM Интернет")
        ],
        [
            KeyboardButton(text="GSM SMS"),
            KeyboardButton(text="GSM Минуты")
        ],
        [
            KeyboardButton(text="⬅️ Назад"),
            KeyboardButton(text="🏠 На главную")
        ]
    ]
)

ussd_command_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="GSM Tariflar"),
            KeyboardButton(text="GSM Internet")
        ],
        [
            KeyboardButton(text="GSM SMS"),
            KeyboardButton(text="GSM Minut")
        ],
        [
            KeyboardButton(text="⬅️ Ortga"),
            KeyboardButton(text="🏠 Bosh sahifaga")
        ]
    ]
)

gsm_internet_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Oylik internet")
        ],
        [
            KeyboardButton(text="Kunlik internet")
        ],
        [
            KeyboardButton(text="Internet non-stop")
        ],
        [
            KeyboardButton(text="⬅️ Ortga"),
            KeyboardButton(text="🏠 Bosh sahifaga")
        ]
    ]
)

gsm_internet_ru_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Месячный интернет")
        ],
        [
            KeyboardButton(text="Ежедневный интернет")
        ],
        [
            KeyboardButton(text="Интернет нон-стоп")
        ],
        [
            KeyboardButton(text="⬅️ Назад"),
            KeyboardButton(text="🏠 На главную")
        ]
    ]
)