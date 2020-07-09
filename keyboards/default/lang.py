from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language_button = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="🇷🇺 Русский"),
        KeyboardButton(text="🇺🇿 O'zbek")

     ],
    ],
    resize_keyboard=True
)


basic_cancel_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Назад"),
            KeyboardButton(text="🏠 На главную")
        ]
    ]
)


basic_cancel_button_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Ortga"),
            KeyboardButton(text="🏠 Bosh sahifaga")
        ]
    ]
)

service_cancel_button_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌ Bekor qilish")
        ]
    ]
)


service_cancel_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌ Отменить")
        ]
    ]
)

service_continue_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➡️ Продолжить")
        ]
    ]
)

service_continue_button_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➡️ Davom eting")
        ]
    ]
)