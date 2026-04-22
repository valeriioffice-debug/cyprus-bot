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

    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, "Выберите действие 👇", reply_markup=markup)
@bot.message_handler(commands=['status'])
def status(message):
    bot.send_message(message.chat.id, "Статус: работает ✅")

print("Bot is running...")
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "📅 Сегодня":
    bot.send_message(
        message.chat.id,
        "📅 Сегодня\n"
        "EUROCONTROL: без резких негативных сигналов\n"
        "Hermes live board: массовых сбоев не видно\n"
        "Отмены/задержки: точечно, без системного сбоя\n"
        "Вывод: 🟡 наблюдаем, но признаков кризиса нет"
    )
    elif message.text == "📈 Неделя":
        bot.send_message(
        message.chat.id,
        "📈 Неделя\n"
        "• Проверить Lufthansa / KLM / easyJet / Wizz / Jet2 / TUI\n"
        "• Найти route changes и cuts\n"
        "• Оценить тренд (рост / падение)\n"
        "• Сделать вывод по рынку"
    )
    elif message.text == "🗓 Месяц":
        bot.send_message(
        message.chat.id,
        "🗓 Месяц\n"
        "• Взять данные Hermes Airports\n"
        "• Взять данные CYSTAT\n"
        "• Сравнить с тем же месяцем прошлого года\n"
        "• Посчитать пассажиров и туристов\n"
        "• Сделать вывод (рост / падение)"
    )
    elif message.text == "/status":
        bot.send_message(message.chat.id, "Бот работает стабильно ✅")
bot.infinity_polling()
@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "Бот работает стабильно ✅")
