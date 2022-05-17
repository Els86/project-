import telebot
from telebot import types
import random

bot = telebot.TeleBot('5396920612:AAFGCNMiwMB8CmWgKGrTnAD8oRQ5kuTXlVA')

first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]
Sovetnik =  ['Послушайте любимую музыку.', 'Приготовьте что-нибудь вкусное.', 'Побалуйте себя и закажите любимую еду на дом.', 'Почитайте книгу.', 'Спойте любимую песню. Но только зажигательно.', 'Посмотрите хороший фильм.', 'Выпейте вкусный чай, кофе или другой напиток.', 'Поиграйте в видео- или онлайн-игру.', 'Прогуляйтесь по району или сходите в парк.' ]

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton(text='Дать совет🤡', callback_data="0")
    item2 = types.InlineKeyboardButton(text='Кот Настроение😍,', callback_data="1")
    #item3 = types.InlineKeyboardButton(text='Как одеться сегодня?🌤🌩', callback_data="2")
    item4 = types.InlineKeyboardButton(text='Случайное число❓', callback_data="3")
    item5 = types.InlineKeyboardButton(text='Знак зодиака🔮', callback_data="4")

    markup.add(item1, item2, item4, item5)

    bot.send_message(message.from_user.id, text= 'Привет, {0.first_name}\nЯ твой бот советчик😏\nО чем рассказать?'.format(message.from_user), reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

#ПОГОДА

#КОТ НАСТРОЕНИЕ
    if call.message:
        if call.data == "1":
            markup = types.InlineKeyboardMarkup()
            item18 = types.InlineKeyboardButton(text='Хорошее😍', callback_data='nastr1')
            item19 = types.InlineKeyboardButton(text='Отличное🥰', callback_data='nastr2')
            item20 = types.InlineKeyboardButton(text='Нормальное😅', callback_data='nastr3')
            item21 = types.InlineKeyboardButton(text='Плохое🙄', callback_data='nastr4')
            item22 = types.InlineKeyboardButton(text='Злое😡', callback_data='nastr5')
            markup.add(item18, item19, item20, item21, item22)

            bot.send_message(call.message.chat.id, text='Настроение😍', reply_markup=markup)

        if call.data == 'nastr1':
            bot.send_photo(call.message.chat.id, 'https://sun9-56.userapi.com/s/v1/ig2/QqVj87kTsCyrExrWqi6IisLJmdBjYww6DGTRZSoOgQs4z0qS-uhiB-szG7CP_ArGYkGDCodwEmLmRtbLvwVOrDlt.jpg?size=1266x1688&quality=96&type=album')
        if call.data == 'nastr2':
            bot.send_photo(call.message.chat.id,'https://sun9-83.userapi.com/s/v1/ig2/wWJoFan-Otc3RMF-AawFTpX06SIPw1ZAXRJUmCwyhILFWlioJEUZPkBo1SytwWk7Molmfe9OMv9iP_x4Q7AUnp9_.jpg?size=1266x1688&quality=96&type=album')
        if call.data == 'nastr3':
            bot.send_photo(call.message.chat.id, 'https://sun9-46.userapi.com/s/v1/ig2;;;/5_PQzCLoBG5HsBRUYZRlVNKG4zzpZh7s9PqJYp_WJEQiAtmVahgFmlD_9nIckRSWN1lOSOuoXAki5hImCoAbwncx.jpg?size=1104x1472&quality=96&type=album')
        if call.data == 'nastr4':
            bot.send_photo(call.message.chat.id,'https://sun9-9.userapi.com/s/v1/ig2/LNN0UjL4mLT7k7EngloE8idOo5XyCRhjJb8Wpccj6Wbiu3jVzkoyXn6VyCPmhF8tW23OoPlr1X7Q5tqqZ80P5_XD.jpg?size=1266x1688&quality=96&type=album')
        if call.data == 'nastr5':
            bot.send_photo(call.message.chat.id, 'https://sun9-70.userapi.com/s/v1/ig2/2yKqDeWhGuZ3oYFM-UWwLQzf_RY8TPgbW-uVSAAl9f4RDoiAdULwdp8OlTHW9y3AbTHbUg7Tc9E9xCvhbBcs1a0x.jpg?size=1266x1688&quality=96&type=album')
#РАНДОМ
    if call.data == '3':
            bot.send_message(call.message.chat.id, " Твое число " + str(random.randint(0, 100)))

#ЗНАКИ ЗОДИАКА
    if call.data == "4":
            markup = types.InlineKeyboardMarkup()
            item6 = types.InlineKeyboardButton(text='Овен♈', callback_data='zodiac')
            item7 = types.InlineKeyboardButton(text='Телец♉', callback_data='zodiac')
            item8 = types.InlineKeyboardButton(text='Близнецы♊', callback_data='zodiac')
            item9 = types.InlineKeyboardButton(text='Рак♋', callback_data='zodiac')
            item10 = types.InlineKeyboardButton(text='Лев♌', callback_data='zodiac')
            item11 = types.InlineKeyboardButton(text='Дева♍', callback_data='zodiac')
            item12 = types.InlineKeyboardButton(text='Весы♎', callback_data='zodiac')
            item13 = types.InlineKeyboardButton(text='Скорпион♏', callback_data='zodiac')
            item14 = types.InlineKeyboardButton(text='Стрелец♐', callback_data='zodiac')
            item15 = types.InlineKeyboardButton(text='Козерог♑', callback_data='zodiac')
            item16 = types.InlineKeyboardButton(text='Водолей♒', callback_data='zodiac')
            item17 = types.InlineKeyboardButton(text='Рыбы♓', callback_data='zodiac')

            markup.add(item6, item7, item8, item9, item10,item11,item12, item13, item14, item15, item16,item17)

            bot.send_message(call.message.chat.id,text='Знак зодиака🔮', reply_markup=markup)

    if call.data == "zodiac":
            msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
            bot.send_message(call.message.chat.id, msg)

#СОВЕТЧИК
    if call.data == '0':
            sovet = random.choice(Sovetnik)
            bot.send_message(call.message.chat.id, sovet)

bot.polling(none_stop=True, interval=0)
