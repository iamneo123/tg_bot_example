from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

data = ('Nike', 'Adidas', 'Reebok')

def brands():
    keyboard = ReplyKeyboardBuilder()
    for brand in data:
        keyboard.add(KeyboardButton(text=brand))
    return keyboard.adjust(1).as_markup()

categories_list = ('Телефоны', 'Планшеты', 'Телевизоры')

def categories():
    keyboard = InlineKeyboardBuilder()
    for category in categories_list:
        keyboard.add(InlineKeyboardButton(text=category, url='https://twitch.tv'))
    return keyboard.adjust(1).as_markup()