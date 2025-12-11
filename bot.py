
import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот успешно работает!")

bot.polling()

import telebot
from telebot import types

TOKEN = "8386565804:AAGHtvRocF3V6RpofnbRve94lVndIo03GVo"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("📝 Подать объявление")
    btn2 = types.KeyboardButton("📂 Категории")
    btn3 = types.KeyboardButton("📘 Правила")
    btn4 = types.KeyboardButton("👤 Поддержка")

    markup.add(btn1)
    markup.add(btn2, btn3)
    markup.add(btn4)

    bot.send_message(
        message.chat.id,
        "Добро пожаловать в *Workclub09*! 👋\nВыберите действие ниже:",
        parse_mode="Markdown",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text == "📘 Правила")
def rules(message):
    bot.send_message(message.chat.id, "Здесь будут правила канала.")


@bot.message_handler(func=lambda message: message.text == "📂 Категории")
def categories(message):
    bot.send_message(message.chat.id, "Здесь будут категории объявлений.")


@bot.message_handler(func=lambda message: message.text == "👤 Поддержка")
def support(message):
    bot.send_message(message.chat.id, "Связаться с админом: @username")  # замени на свой логин


@bot.message_handler(func=lambda message: message.text == "📝 Подать объявление")
def ad_create(message):
    bot.send_message(message.chat.id, "Начинаем создание объявления!")


bot.infinity_polling()
