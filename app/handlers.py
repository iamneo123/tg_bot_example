import asyncio
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.enums import ChatAction

import app.keyboards as kb
import app.builder as builder

router = Router()

#ответ на комманды пользователя
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await asyncio.sleep(2)
    await message.reply('Привет!')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f'{message.from_user.first_name}, вам нужна помощь?');

@router.message(Command('reply_keyboard'))
async def cmd_reply_keyboard(message: Message):
    await message.answer('replay keyboard', reply_markup=kb.reply_keyboard)

@router.message(Command('inline_keyboard'))
async def cmd_inline_keyboard(message: Message):
    await message.answer('inline keyboard', reply_markup=kb.inline_keyboard)

#ответ на сообщение пользователя
@router.message(F.text == 'привет')
async def echo(message: Message):
    await message.answer(f'Привет, твой id: {message.from_user.id}')

@router.message(F.photo)
async def echo(message: Message):
    photo_id = message.photo[-1].file_id
    await message.answer(photo_id)
    await message.answer_photo(photo=photo_id)

@router.message(F.animation)
async def echo(message: Message):
    await message.answer_animation(animation=message.animation.file_id)


@router.callback_query(F.data == 'catalog')
async def cmd_catalog(callback: CallbackQuery):
    await callback.answer('Каталог')
    await callback.message.answer('Вы открыли каталог', reply_markup=builder.categories())
    #await callback.message.answer('Вы открыли каталог', reply_markup=builder.brands())