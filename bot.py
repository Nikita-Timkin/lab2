import telebot
from telebot import types
import random

token = '6157998467:AAGcC3gMN-2mk8khfh8uMQPHfr74VnBRDWY'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Получить мотивационную картинку")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Привет. Я бот, отправляющий мотивационные картинки. Чтобы получить картинку, нажмите на кнопку.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    motivational_pictures = ['https://static-cse.canva.com/blob/169922/RUmotiv9.a8ab03c6.png',
                             'https://static-cse.canva.com/blob/169914/RUmotiv1.png',
                             'https://i.pinimg.com/736x/62/82/9a/62829adadad4684843e0cb124f11e45c.jpg',
                             'https://i.pinimg.com/originals/dc/5b/f1/dc5bf1b0bf87d2cf009a1b9a2f883a00.png',
                             'https://static-cse.canva.com/blob/169946/RUmotiv34.png']

    if (message.text == "Получить мотивационную картинку"):
        bot.send_photo(message.chat.id, random.choice(motivational_pictures))

bot.polling(none_stop=True)