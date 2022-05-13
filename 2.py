import telebot
from telebot import types
import random

bot = telebot.TeleBot('5317431364:AAFutQPwIC0FBZd-ihIeFR0XPDAUVpsU3ww')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Выкинуть рандом')

    markup.add(item1)
    bot.send_message(message.chat.id,'Здравствуй, {0.first_name}!\nНажми чтобы получить число от 1 до 1000🎲 ' . format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def randomizer(message):
    if message.text == 'Выкинуть рандом':
        bot.send_message(message.chat.id, 'Ваше случайное число: {}'.format(random.randint(1, 1000)))

bot.polling(none_stop=True)



