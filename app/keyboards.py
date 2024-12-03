from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Каталог'), KeyboardButton(text='Корзина')],
        [KeyboardButton(text='Контакты')],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберете пункт меню.'
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='twitch', url='https://twitch.tv')],
        [InlineKeyboardButton(text='youtube', url='https://youtube.com')],
        [InlineKeyboardButton(text='Каталог', callback_data='catalog')]
    ]
)