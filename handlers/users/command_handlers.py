from loader import dp
from keyboards import commands_default_keyboard, get_item_inline_keyboard, navigation_items_callback
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, InputFile, InputMediaPhoto
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


@dp.message_handler(text=['Список товаров'])
@dp.message_handler(commands=['item'])
async def answer_menu_command(message: types.Message):
    first_item_info = db.select_items_info(id=1)
    first_item_info = first_item_info[0]
    _, name, count, photo_path = first_item_info
    item_text = f'Название товара : {name}' \
                f'\nКоличество товара : {count}'
    photo = InputFile(path_or_bytesio=photo_path)
    await message.answer_photo(photo=photo,
                               caption=item_text,
                               reply_markup=get_item_inline_keyboard())


@dp.callback_query_handler(navigation_items_callback.filter(for_data='items'))
async def see_new_item(call: types.CallbackQuery):
    current_item_id = int(call.data.split(':')[-1])
    first_item_info = db.select_items_info(id=current_item_id)
    first_item_info = first_item_info[0]
    _, name, count, photo_path = first_item_info
    item_text = f'Название товара: {name}'\
                f'\nКоличество товара: {count}'
    photo = InputFile(path_or_bytesio=photo_path)
    await bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                       caption=item_text),
                                 chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 reply_markup=get_item_inline_keyboard(id=current_item_id))


@dp.message_handler(commands='help')
async def answer_help_command(message: types.Message):
    await message.answer(text='Мне нечем помочь')

