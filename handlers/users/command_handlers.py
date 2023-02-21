from loader import dp
from keyboards import commands_default_keyboard
from aiogram import types
from loader import db, bot


@dp.message_handler(text=['Привет', 'Начать'])
@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    await message.answer(text='Привет!'
                         f'\nРад тебя видеть!',
                         reply_markup=commands_default_keyboard)


@dp.message_handler(content_types='contact')
async def answer_contact_command(message: types.Message):
    if message.contact.user_id == message.from_user.id:
        await message.answer(text='Регистрация прошла успешно')
        db.add_user(int(message.from_user.id), str(message.contact.phone_number))
    else:
        await message.answer('Увы')


@dp.message_handler(commands='help')
@dp.message_handler(text=['Помощь', 'помощь'])
async def answer_help_command(message: types.Message):
    await message.answer(text='/start - приветствие'
                              '\n/item - ассортимент'
                              '\n/help - доступные команды')

