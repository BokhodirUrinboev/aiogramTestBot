from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

services_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Limitsiz ovoz")
        ],
        [
            KeyboardButton(text="Qo`llab yubor")
        ],
        [
            KeyboardButton(text="Tungi internet")
        ],
        [
            KeyboardButton(text="🏠 Bosh sahifaga")
        ]
    ]
)

services_ru_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Голос безлимит")
        ],
        [
            KeyboardButton(text="Выручай")
        ],
        [
            KeyboardButton(text="Ночной интернет")
        ],
        [
            KeyboardButton(text="🏠 На главную")
        ]
    ]
)