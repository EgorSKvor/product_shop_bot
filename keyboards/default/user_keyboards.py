from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/item')
        ],
        [
            KeyboardButton(text='/help'),
            KeyboardButton(text='/menu')
        ],
        [
            KeyboardButton(text='Отправить номер телефона',
                           request_contact=True),
        ]
    ],
    resize_keyboard=True
)
