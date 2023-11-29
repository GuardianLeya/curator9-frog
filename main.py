import telebot
from telebot import types
import random

bot = telebot.TeleBot("6468336716:AAHnwfAxTIlgEck2qZ3XC87dmYSITv_5WhM")

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    random_sender = types.KeyboardButton("Рандомное число")
    markup.add(random_sender)
    bot.send_message(message.chat.id, '<b>Запускаю рандом!</b>', parse_mode='html',
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def first_number_step(message):
    if message.text == 'Рандомное число':
        msg = bot.send_message(message.chat.id, 'Начало диапазона')
        bot.register_next_step_handler(msg, second_number_step)
    else:
        bot.send_message(message.chat.id, 'Мне кажется, ты не прав)')

def second_number_step(message):
    global NUM_first
    NUM_first = int(message.text)
    msg = bot.send_message(message.chat.id, 'Введите конец диапазона')
    bot.register_next_step_handler(msg, result_number_step)

def result_number_step(message):
    global NUM_second
    NUM_second = int(message.text)
    result(message)
def result(message):
    bot.send_message(message.chat.id, 'Твое счастливое число:  ' + str(random.randint(NUM_first, NUM_second)))

bot.polling(none_stop=True)
