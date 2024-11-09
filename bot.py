import asyncio
import random
import logging
from random import randint
from selectors import SelectSelector

from Tools.scripts.mailerdaemon import emparse_list_from
from aiogram import Bot, Dispatcher,types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import FSInputFile

logging.basicConfig(level=logging.INFO)
TOKEN='7626978590:AAGT57_uqQLQd_b259FPg59BuES5MZGP0oo'
bot = Bot(token=TOKEN)
dp =Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text= 'шутка'))
    builder.add(types.KeyboardButton(text = 'погода'))
    builder.add(types.KeyboardButton(text = 'еще шутка'))
    builder.add(types.KeyboardButton(text = 'мемчик'))
    builder.add(types.KeyboardButton(text = 'реши пример'))
    builder.add(types.KeyboardButton(text = 'казино!!!'))
    await message.answer(
        'чего изволишь?',
        reply_markup=builder.as_markup(resize_keyboard =True),
    )


@dp.message(F.text =='погода')
async def get_photo(message: types.Message):
    url ='1.png'
    image = FSInputFile(url)
    await message.answer_photo(photo = image, caption ='погода')


@dp.message(F.text =='шутка')
async def get_photo(message: types.Message):
    url ='10.png'
    image = FSInputFile(url)
    await message.answer_photo(photo = image, caption ='шутка дня')


@dp.message(F.text =='еще шутка')
async def get_photo(message: types.Message):
    url ='11.png'
    image = FSInputFile(url)
    await message.answer_photo(photo = image, caption ='шутка дня')

@dp.message(F.text =='мемчик')
async def get_photo(message: types.Message):
    url ='20.png'
    image = FSInputFile(url)
    await message.answer_photo(photo = image, caption ='мем')


@dp.message(F.text == 'Привет')
async def fun_hello(message: types.Message):
    await message.answer('здаров!')


@dp.message(F.text == 'реши пример')
async def fun_math(message: types.Message):
    await message.answer('2+2')

@dp.message(F.text == '4')
async def fun_math(message: types.Message):
    await message.answer('верно')


@dp.message(F.text != '4')
async def fun_math(message: types.Message):
    await message.answer('неправильно')






async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


