from loader import dp
from aiogram import types


@dp.message_handler(text='Огурец')
async def answer_start_command(message: types.Message):
    await message.answer(text='Yes sir')