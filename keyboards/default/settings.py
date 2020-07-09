from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

settings_uz_button = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="📄 Xizmatlarni boshqarish"),
     ],
     [
        KeyboardButton(text="🌍 Tilni o'zgaritirish"),
        KeyboardButton(text="🏠 Bosh sahifaga")
     ]
    ],
    resize_keyboard=True
)

settings_ru_button = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="📄 Управление услугами"),
     ],
     [
        KeyboardButton(text="🌍 Изменить язык"),
        KeyboardButton(text="🏠 На главную")
     ]
    ],
    resize_keyboard=True
)

change_lang_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇷🇺 Русский")
        ],
        [
            KeyboardButton(text="🇺🇿 O'zbek")
        ],
        [
            KeyboardButton(text="⬅️ Ortga"),
            KeyboardButton(text="🏠 Bosh sahifaga")
        ]
    ]
)

change_lang_ru_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇷🇺 Русский")
        ],
        [
            KeyboardButton(text="🇺🇿 O'zbek")
        ],
        [
            KeyboardButton(text="⬅️ Назад"),
            KeyboardButton(text="🏠 На главную")
        ]
    ]
)