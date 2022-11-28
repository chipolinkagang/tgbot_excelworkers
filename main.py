# при /start сообщение "Вы в главном меню." и кнопка "Добавить работника"
# при нажатии на кнопку: сообщение "Введите ФИО работника"
# далее обработка ответа и вывод xlsx
import json

import telebot
import states
from database import db_con

from markups import markup
from recycle import excel

with open("C:\\Users\\kiril\\PycharmProjects\\testbotjob_project\\config.json", 'r',
          encoding='utf-8') as f:  # открыли файл
    options = json.load(f)  # загнали все из файла в переменную

api_key = options["tg_api"]  # apy key

bot = telebot.TeleBot(api_key, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Вы в главном меню.', reply_markup=markup)
    states.state.false_add()


@bot.message_handler()
def echo_all(message):
    if message.text == "Добавить работника":
        bot.send_message(message.chat.id, 'Введите ФИО работника', reply_markup=markup)
        states.state.true_add()
    elif states.state.get_add():
        print(db_con.insert_table(message.text))
        five_last = db_con.get_5last_users()
        excel.create5_excel(five_last)
        f = open("demo.xlsx", "rb")
        bot.send_document(message.chat.id, f)

        states.state.false_add()
    else:
        bot.send_message(message.chat.id, 'Начните заново: /start', reply_markup=markup)
        states.state.false_add()



bot.infinity_polling()
