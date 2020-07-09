from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_uz_button = ReplyKeyboardMarkup(
    keyboard=[
     [
         KeyboardButton(text="➕ Hizmat qo'shish"),

     ],
     [
        KeyboardButton(text="💼 Paketlar"),
        KeyboardButton(text="📋 Tariflar")


     ],
     [
        KeyboardButton(text="📌 Foydali"),
        KeyboardButton(text="📥 Sozlamalar")

     ],
    ],
    resize_keyboard=True
)

menu_ru_button = ReplyKeyboardMarkup(
    keyboard=[
     [
         KeyboardButton(text="➕ Добавить услугу")

     ],
     [
        KeyboardButton(text="💼 Пакеты"),
        KeyboardButton(text="📋 Тарифы")

     ],
     [
        KeyboardButton(text="📌 Полезное"),
        KeyboardButton(text="📥 Настройки")

     ],
    ],
    resize_keyboard=True
)

menu_reg_uz_button = ReplyKeyboardMarkup(
    keyboard=[
     [
         KeyboardButton(text="💼 Paketlar"),
         KeyboardButton(text="🔗 Xizmatlar"),
         KeyboardButton(text="💰 Hisobingiz")

     ],
     [
        KeyboardButton(text="📋 Tariflar"),
        KeyboardButton(text="➕ Hizmat qo'shish")

     ],
     [
        KeyboardButton(text="📌 Foydali"),
        KeyboardButton(text="📥 Sozlamalar")

     ],
    ],
    resize_keyboard=True
)


menu_reg_ru_button = ReplyKeyboardMarkup(
    keyboard=[
     [
         KeyboardButton(text="💼 Пакеты"),
         KeyboardButton(text="🔗 Услуги"),
         KeyboardButton(text="💰 Баланс")

     ],
     [
        KeyboardButton(text="📋 Тарифы"),
        KeyboardButton(text="➕ Добавить услугу")

     ],
     [
        KeyboardButton(text="📌 Полезное"),
        KeyboardButton(text="📥 Настройки")

     ],
    ],
    resize_keyboard=True
)