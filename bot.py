import telebot
from telebot import types
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("📅 Сегодня")
btn2 = types.KeyboardButton("📈 Неделя")
btn3 = types.KeyboardButton("🗓 Месяц")


    bot.send_message(message.chat.id, "Выберите действие 👇", reply_markup=markup)

@bot.message_handler(commands=['status'])
def status(message):
    bot.send_message(message.chat.id, "Статус: работает ✅")

print("Bot is running...")
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "📅 Сегодня":
        bot.send_message(message.chat.id, "Сегодня: оперативный мониторинг рейсов и сигналов по Кипру в разработке.")
    elif message.text == "📈 Неделя":
        bot.send_message(message.chat.id, "Неделя: обзор изменений у авиакомпаний в разработке.")
    elif message.text == "🗓 Месяц":
        bot.send_message(message.chat.id, "Месяц: сравнение Hermes + CYSTAT с прошлым годом в разработке.")
    elif message.text == "/status":
        bot.send_message(message.chat.id, "Бот работает стабильно ✅")
bot.infinity_polling()
@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "Бот работает стабильно ✅")
