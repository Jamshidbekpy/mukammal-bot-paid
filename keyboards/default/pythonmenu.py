from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [  # 1-qator
            KeyboardButton(text="00 - Kirish"),
        ],
        [  # 2-qator
            KeyboardButton(text="01 - Funksiyalar"),
            KeyboardButton(text="02 - Operatorlar"),
        ],
        [  # 3-qator
            KeyboardButton(text="03 - Modul"),
            KeyboardButton(text="04 - Shartlar"),
        ],
        [  # 4-qator
            KeyboardButton(text="Bosh menu"),
        ],
    ],
    resize_keyboard=True
)
