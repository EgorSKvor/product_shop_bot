from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inlines.callback_data import navigation_items_callback
from loader import db


def get_item_inline_keyboard(id: int = 1) -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup()
    left_id = id - 1
    right_id = id + 1
    if id == 1:
        btm = InlineKeyboardButton(text='>>>',
                                   callback_data=navigation_items_callback.new(
                                       for_data='items',
                                       id=right_id)
                                   )
        item_inline_keyboard.add(btm)
    elif id == db.get_items_count():
        btm = InlineKeyboardButton(text='<<<',
                                   callback_data=navigation_items_callback.new(
                                       for_data='items',
                                       id=left_id)
                                   )
        item_inline_keyboard.add(btm)
    else:
        btm_left = InlineKeyboardButton(text='<<<',
                                        callback_data=navigation_items_callback.new(
                                            for_data='items',
                                            id=left_id)
                                        )
        btm_right = InlineKeyboardButton(text='>>>',
                                         callback_data=navigation_items_callback.new(
                                             for_data='items',
                                             id=right_id)
                                         )
        item_inline_keyboard.row(btm_left, btm_right)
    return item_inline_keyboard
