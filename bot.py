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
        "📅 Сегодня\n\n"
        "✈️ EUROCONTROL:\n"
        "✔ Трафик стабильный\n"
        "❗ Германия: -12% частоты\n\n"
        "🛫 Hermes:\n"
        "✔ Массовых сбоев нет\n"
        "❗ Небольшие задержки UK\n\n"
        "📊 Отмены:\n"
        "• Точечные, без системы\n\n"
        "📌 Вывод:\n"
        "🟡 Рынок стабильный, но под давлением"
    )
    elif message.text == "📈 Неделя":
        bot.send_message(
        message.chat.id,
        "📈 Неделя\n\n"
        "✈️ Авиакомпании:\n"
        "Lufthansa:\n"
        "✔ Без значимых изменений\n\n"
        "KLM:\n"
        "✔ Стабильно\n\n"
        "easyJet:\n"
        "✔ Увеличение рейсов UK\n\n"
        "Wizz Air:\n"
        "❗ Снижение частот по Восточной Европе\n\n"
        "Jet2 / TUI:\n"
        "✔ Сезонный рост\n\n"
        "📊 Тренд:\n"
        "🟡 Смешанный (рост UK, слабость ЕС)\n\n"
        "📌 Вывод:\n"
        "Рынок держится за счёт UK, континентальная Европа слабеет"
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
