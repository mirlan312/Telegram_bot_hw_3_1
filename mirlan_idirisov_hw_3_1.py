from aiogram import types
from aiogram.utils import executor

from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import logging

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(f'Hello {message.from_user.full_name}!')

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Все файлы компьютера записываются на?'
    answer = [
        'А) Винчестер', 'Б) Модулятор', 'В) Флоппи - диск', 'Г) Генератор'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Дробовик по другому',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = 'Как включить на клавиатуре все заглавные буквы?'
    answers = [
        'А) Alt + Ctrl', 'Б) Caps Lock', 'В) Shift + Ctrl', 'Г) Shift + Ctrl + Alt'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='AБВ',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):


    photo = open('media/image.jpg', "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        is_anonymous=False,
        type='quiz',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )

@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)