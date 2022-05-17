import telebot
from telebot import types


bot = telebot.TeleBot('5199940647:AAFE6Qqwl0gRPq4zYpA7KvXYxrt8WdYhgCE')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup()
    menu1 = types.KeyboardButton('Курс Доллара')
    menu2 = types.KeyboardButton('Мое Эхо!')
    menu3 = types.KeyboardButton('Выкинуть рандом')
    menu4 = types.KeyboardButton('Дать совет')

    markup.add(menu1, menu2, menu3, menu4)

    bot.send_message(message.from_user.id, 'Привет дорогой друг\nО чем поведать тебе сегодня?', reply_markup= markup)






bot.message_handler(content_types=['text'])
def  echo_all(message):
    bot.send_message(message.from_user.id, message.text)
    if __name__ == '__main__':
        return message



bot.polling(none_stop=True)

