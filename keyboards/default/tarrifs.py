from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tarrifs_ru_button = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="📱 Мобильные тарифы")
        ],
        [
            KeyboardButton(text="🌏 Интернет тарифы")
        ],
        [
            KeyboardButton(text="🏠 На главную")
        ]
     ],

    resize_keyboard=True
)

tarrifs_uz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Mobil tariflar")
        ],
        [
            KeyboardButton(text="🌏 Internet tariflar")
        ],
        [
            KeyboardButton(text="🏠 Bosh sahifaga")
        ]
     ],
    resize_keyboard=True
)

mobile_uz_button = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="📋 GSM tariflar")
        ],
        [
            KeyboardButton(text="📋 CDMA tariflar")
        ],
        [
            KeyboardButton(text="⬅️ Ortga"),
            KeyboardButton(text="🏠 Bosh sahifaga")
        ]
     ],

    resize_keyboard=True
)

mobile_ru_button = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="📋 GSM тарифы")
        ],
        [
            KeyboardButton(text="📋 CDMA тарифы")
        ],
        [
            KeyboardButton(text="⬅️ Назад"),
            KeyboardButton(text="🏠 На главную")
        ]
     ],

    resize_keyboard=True
)

internet_ru_button = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="Unlim")
        ],
        [
            KeyboardButton(text="RUN")
        ],
         [
             KeyboardButton(text="Active new")
         ],
         [
             KeyboardButton(text="Start")
         ],
        [
            KeyboardButton(text="⬅️ Назад"),
            KeyboardButton(text="🏠 На главную")
        ],
     ],

    resize_keyboard=True
)

internet_uz_button = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="Unlim")
        ],
        [
            KeyboardButton(text="RUN")
        ],
         [
             KeyboardButton(text="Active new")
         ],
         [
             KeyboardButton(text="Start")
         ],
        [
            KeyboardButton(text="⬅️ Ortga"),
            KeyboardButton(text="🏠 Bosh sahifaga")
        ],
     ],
    resize_keyboard=True
)

mobile_gsm_ru_button = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="ТП: Street")
        ],
        [
            KeyboardButton(text="ТП: Street Upgrade")
        ],
         [
             KeyboardButton(text="ТП: Onlime")
         ],
         [
             KeyboardButton(text="ТП: Flash")
         ],
         [
             KeyboardButton(text="ТП: Flash Upgrade")
         ],
         [
             KeyboardButton(text="ТП: Royal")
         ],
         [
             KeyboardButton(text="ТП: Деловой")
         ],
         [
           KeyboardButton(text="ТП: Просто 10")
         ],
        [
            KeyboardButton(text="⬅️ Назад"),
            KeyboardButton(text="🏠 На главную")
        ],

    ],
    resize_keyboard=True
)


mobile_gsm_uz_button = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="TR: Street")
        ],
        [
            KeyboardButton(text="TR: Street Upgrade")
        ],
         [
             KeyboardButton(text="TR: Onlime")
         ],
         [
             KeyboardButton(text="TR: Flash")
         ],
         [
             KeyboardButton(text="TR: Flash Upgrade")
         ],
         [
             KeyboardButton(text="TR: Royal")
         ],
         [
             KeyboardButton(text="TR: Ishbilarmon")
         ],
         [
           KeyboardButton(text="TR: Oddiy 10")
         ],
        [
            KeyboardButton(text="⬅️ Ortga"),
            KeyboardButton(text="🏠 Bosh sahifaga")
        ],
     ],
    resize_keyboard=True
)

mobile_cdma_uz_button = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="TR: Oddiy")
        ],
        [
            KeyboardButton(text="TR: Optimal")
        ],
         [
             KeyboardButton(text="TR: Ajoyib")
         ],
         [
             KeyboardButton(text="TR: Obod")
         ],
         [
             KeyboardButton(text="TR: Oddiy +")
         ],
         [
             KeyboardButton(text="TR: Optimal +")
         ],
         [
             KeyboardButton(text="TR: Ajotib +")
         ],
         [
            KeyboardButton(text="⬅️ Ortga"),
            KeyboardButton(text="🏠 Bosh sahifaga")
        ],

    ],
    resize_keyboard=True
)

mobile_cdma_ru_button = ReplyKeyboardMarkup(
    keyboard=[

            [
                KeyboardButton(text="ТП: Простой")
            ],
            [
                KeyboardButton(text="ТП: Оптимальный")
            ],
            [
                KeyboardButton(text="ТП: Превосходный")
            ],
            [
                KeyboardButton(text="ТП: Обод")
            ],
            [
                KeyboardButton(text="ТП: Простой +")
            ],
            [
                KeyboardButton(text="ТП: Оптимальный +")
            ],
            [
                KeyboardButton(text="ТП: Превосходный +")
            ],
            [
                KeyboardButton(text="⬅️ Назад"),
                KeyboardButton(text="🏠 На главную")
            ],

        ],
    resize_keyboard=True
)

