import telebot
from telebot import types
import random

bot = telebot.TeleBot('5335062275:AAH_nUbdJt79KDTb7FWNiBSuH15i-kUkeXE')

first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton(text='Дать совет🤡', callback_data="0")
    item2 = types.InlineKeyboardButton(text='Настроение😍,', callback_data="1")
    item3 = types.InlineKeyboardButton(text='Как одеться сегодня?🌤🌩', callback_data="2")
    item4 = types.InlineKeyboardButton(text='Случайное число❓', callback_data="3")
    item5 = types.InlineKeyboardButton(text='Знак зодиака🔮', callback_data="4")

    markup.add(item1, item2,item3,item4, item5)

    bot.send_message(message.from_user.id, text= 'Привет, {0.first_name}\nЯ твой бот советчик😏\nЧто посоветовать тебе сегодня?'.format(message.from_user), reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == '3':
            bot.send_message(call.message.chat.id, " Твое число " + str(random.randint(0, 100)))


bot.polling(none_stop=True, interval=0)
