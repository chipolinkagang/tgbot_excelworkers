from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
add_worker = types.KeyboardButton('Добавить работника')
markup.add(add_worker)