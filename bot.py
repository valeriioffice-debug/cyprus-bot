import telebot
from telebot import types
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("📊 Статус")
    btn2 = types.KeyboardButton("ℹ️ О боте")

    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, "Выберите действие 👇", reply_markup=markup)

@bot.message_handler(commands=['status'])
def status(message):
    bot.send_message(message.chat.id, "Статус: работает ✅")

print("Bot is running...")
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "📊 Статус":
        bot.send_message(message.chat.id, "Бот работает стабильно ✅")

    elif message.text == "ℹ️ О боте":
        bot.send_message(message.chat.id, "Бот для контроля туристов на Кипре 🇨🇾")
bot.infinity_polling()
@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "Бот работает стабильно ✅")
