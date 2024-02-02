from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Toshkent', callback_data='a'),
     InlineKeyboardButton(text='Buxoro ', callback_data='b')],
    [InlineKeyboardButton(text='Sirdaryo', callback_data='c'),
     InlineKeyboardButton(text='Jizzax', callback_data='d')],

])
