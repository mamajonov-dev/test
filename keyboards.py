from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def asosiymenubutton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text='Royxatdan otish'),

    )
    return markup

def orqagabutton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text='Orqaga'),

    )

    return markup