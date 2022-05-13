# Подключаем модуль случайных чисел
import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('токен')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Заготовки для трёх предложений
first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]
# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        keyboard.add(key_ryby)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac":
        # Формируем гороскоп
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)






#       keyboard = types.InlineKeyboardMarkup()
#     key_sovet = types.InlineKeyboardButton(text='Дать совет🤡')
#     keyboard.add(key_sovet)
#     keyboard = types.InlineKeyboardMarkup()
#     key_nastr = types.InlineKeyboardButton(text='Настроение😍')
#     keyboard.add(key_nastr)
#     keyboard = types.InlineKeyboardMarkup()
#     key_pogoda = types.InlineKeyboardButton(text='Как одеться сегодня?🌤🌩')
#     keyboard.add(key_pogoda)
#     keyboard = types.InlineKeyboardMarkup()
#     key_chislo = types.InlineKeyboardButton(text='Случайное число❓')
#     keyboard.add(key_chislo)
#     keyboard = types.InlineKeyboardMarkup()
#     key_znak = types.InlineKeyboardButton(text='Знак зодиака🔮')
#     keyboard.add(key_znak)
#
#
#
#
#
#
#
#
#
#
#     (  markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

        #zodiac1 = types.KeyboardButton('Овен♈',callback_data='zodiac')
        #zodiac2 = types.KeyboardButton('Телец♉',callback_data='zodiac')
        #zodiac3 = types.KeyboardButton('Близнецы♊',callback_data='zodiac')
        #zodiac4 = types.KeyboardButton('Рак♋',callback_data='zodiac')
        #zodiac5 = types.KeyboardButton('Лев♌',callback_data='zodiac')
        #zodiac6 = types.KeyboardButton('Дева♍',callback_data='zodiac')
        #zodiac7 = types.KeyboardButton('Весы♎',callback_data='zodiac')
        #zodiac8 = types.KeyboardButton('Скорпион♏',callback_data='zodiac')
        #zodiac9 = types.KeyboardButton('Стрелец♐', callback_data='zodiac')
        #zodiac10 = types.KeyboardButton('Козерог♑', callback_data='zodiac')
        #zodiac11 = types.KeyboardButton('Водолей♒', callback_data='zodiac')
        #zodiac12 = types.KeyboardButton('Рыбы♓', callback_data='zodiac')

        #markup.add(zodiac1, zodiac2, zodiac3, zodiac4, zodiac5, zodiac6, zodiac7, zodiac8, zodiac9, zodiac10, zodiac11,zodiac12))







        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='Овен♈', callback_data='zodiac')
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец♉', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы♊', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак♋', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев♌', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева♍', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы♎', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион♏', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец♐', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог♑', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей♒', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Рыбы♓', callback_data='zodiac')
        keyboard.add(key_ryby)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'zodiac':
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)




  #if message.text == 'Дать совет🤡':
        #bot.send_message(message.chat.id, "")
        #if message.text == 'Настроение😍':
        #bot.send_message(message.chat.id, "")
        #if message.text == 'Как одеться сегодня?🌤🌩':
        #bot.send_message(message.chat.id, "")
# if message.text == 'Знак зодиака🔮':