from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

packages_uz_button = ReplyKeyboardMarkup(
    keyboard=[
     [
         KeyboardButton(text="🌐 Internet paketlar"),
     ],
     [
        KeyboardButton(text="📞 Qonqg`iroq uchun paketlar")
     ],
     [
        KeyboardButton(text="✉️Sms paketlar")
     ],
     [
         KeyboardButton(text="🏠 Bosh sahifaga")
     ]
    ],
    resize_keyboard=True
)

packages_ru_button = ReplyKeyboardMarkup(
    keyboard=[
     [
         KeyboardButton(text="🌐 Интернет пакеты"),
     ],
     [
        KeyboardButton(text="📞 Пакеты минут")
     ],
     [
        KeyboardButton(text="✉️Sms пакеты")
     ],
     [

         KeyboardButton(text="🏠 На главную")
     ]
    ],
    resize_keyboard=True
)

internet_packages_ru_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Месячные Интернет пакеты")
        ],
        [
            KeyboardButton(text="Ежедневные Интернет пакеты")
        ],
        [
            KeyboardButton(text="Пакеты для TAS-IX")
        ],
        [
            KeyboardButton(text="Интернет нон-стоп пакеты")
        ],
        [
            KeyboardButton(text="⬅️ Назад"),
            KeyboardButton(text="🏠 На главную")
        ]
    ]
)

internet_packages_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Oylik internet paketlar")
        ],
        [
            KeyboardButton(text="Kunlik internet paketlar")
        ],
        [
            KeyboardButton(text="TAS-IX uchun paketlar")
        ],
        [
            KeyboardButton(text="Internet non-stop paketlar")
        ],
        [
            KeyboardButton(text="⬅️ Ortga"),
            KeyboardButton(text="🏠 Bosh sahifaga")
        ]
    ]
)