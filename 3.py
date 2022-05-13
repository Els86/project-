import telebot
from telebot import types

bot = telebot.TeleBot('5335062275:AAH_nUbdJt79KDTb7FWNiBSuH15i-kUkeXE')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Хорошее😍')
    item2 = types.KeyboardButton('Отличное🥰')
    item3 = types.KeyboardButton('Нормальное😅')
    item4 = types.KeyboardButton('Злое😡')
    item5 = types.KeyboardButton('Плохое🙄')
    item6 = types.KeyboardButton('Голодная🤤')

    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id,'Здравствуй, {0.first_name}!\nЯ твой бот настроение!!!\nКакое настроение у тебя сегодня?\nВыбери в Меню'. format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Хорошее😍':
        bot.send_photo(message.chat.id, "https://sun9-56.userapi.com/s/v1/ig2/QqVj87kTsCyrExrWqi6IisLJmdBjYww6DGTRZSoOgQs4z0qS-uhiB-szG7CP_ArGYkGDCodwEmLmRtbLvwVOrDlt.jpg?size=1266x1688&quality=96&type=album")
    elif message.text == 'Отличное🥰':
        bot.send_photo(message.chat.id, "https://sun9-83.userapi.com/s/v1/ig2/wWJoFan-Otc3RMF-AawFTpX06SIPw1ZAXRJUmCwyhILFWlioJEUZPkBo1SytwWk7Molmfe9OMv9iP_x4Q7AUnp9_.jpg?size=1266x1688&quality=96&type=album")
    elif message.text == 'Нормальное😅':
        bot.send_photo(message.chat.id, "https://sun9-46.userapi.com/s/v1/ig2;;;/5_PQzCLoBG5HsBRUYZRlVNKG4zzpZh7s9PqJYp_WJEQiAtmVahgFmlD_9nIckRSWN1lOSOuoXAki5hImCoAbwncx.jpg?size=1104x1472&quality=96&type=album")
    elif message.text == 'Злое😡':
        bot.send_photo(message.chat.id, "https://sun9-70.userapi.com/s/v1/ig2/2yKqDeWhGuZ3oYFM-UWwLQzf_RY8TPgbW-uVSAAl9f4RDoiAdULwdp8OlTHW9y3AbTHbUg7Tc9E9xCvhbBcs1a0x.jpg?size=1266x1688&quality=96&type=album")
    elif message.text == 'Плохое🙄':
        bot.send_photo(message.chat.id, "https://sun9-9.userapi.com/s/v1/ig2/LNN0UjL4mLT7k7EngloE8idOo5XyCRhjJb8Wpccj6Wbiu3jVzkoyXn6VyCPmhF8tW23OoPlr1X7Q5tqqZ80P5_XD.jpg?size=1266x1688&quality=96&type=album")
    elif message.text == 'Голодная🤤':
        bot.send_photo(message.chat.id,"https://sun9-80.userapi.com/s/v1/ig2/IwGhmBQmQlq9-n06AfqbUpx8Z8xoFrcmNXsfO6PbBHCcvCVXrE37JNUIA4dYuZJRMkXYs_BAPjZn3tCYakCTNnzu.jpg?size=1104x1472&quality=95&type=album")
bot.polling(none_stop=True)
