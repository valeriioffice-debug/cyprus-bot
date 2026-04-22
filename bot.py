from datetime import datetime
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
    import json
    if message.text == "📅 Сегодня":
        import subprocess
        subprocess.run(["python", "update_today.py"])
        with open("today_data.json", "r", encoding="utf-8") as f:
         data = json.load(f)

    date = data["date"]

    euro = data["eurocontrol"]
    hermes = data["hermes"]
    summary = data["summary"]

    bot.send_message(
        message.chat.id,
        f"📅 Сегодня ({date})\n\n"

        f"✈️ EUROCONTROL:\n"
        f"Статус: {euro['traffic_status']}\n"
        f"Изменение: {euro['traffic_change_pct']}%\n"
        f"Давление: {euro['pressure_level']}\n"
        f"Комментарий: {euro['note']}\n\n"

        f"🛫 Hermes:\n"
        f"Статус: {hermes['airport_status']}\n"
        f"Отмены: {hermes['cancelled_flights']}\n"
        f"Задержки: {hermes['delayed_flights']}\n"
        f"Сбои: {hermes['disruption_level']}\n"
        f"Комментарий: {hermes['note']}\n\n"

        f"📌 Вывод:\n"
        f"{summary['message']}"
    )
    # elif message.text == "📈 Неделя":
        # bot.send_message(
        # message.chat.id,
        # "📈 Неделя\n\n"
        # "✈️ Авиакомпании:\n"
        # "Lufthansa:\n"
        # "✔ Без значимых изменений\n\n"
        # "KLM:\n"
        # "✔ Стабильно\n\n"
        # "easyJet:\n"
        # "✔ Увеличение рейсов UK\n\n"
        # "Wizz Air:\n"
        # "❗ Снижение частот по Восточной Европе\n\n"
        # "Jet2 / TUI:\n"
        # "✔ Сезонный рост\n\n"
        # "📊 Тренд:\n"
        # "🟡 Смешанный (рост UK, слабость ЕС)\n\n"
        # "📌 Вывод:\n"
        # "Рынок держится за счёт UK, континентальная Европа слабеет"
    # )
    # elif message.text == "🗓 Месяц":
        # bot.send_message(
        # message.chat.id,
        # "🗓 Месяц\n\n"
        # "✈️ Пассажиры (Hermes):\n"
        # "2.85 млн\n"
        # "📉 -4.2% к прошлому году\n\n"
        # "🏝 Туристы (CYSTAT):\n"
        # "1.12 млн\n"
        # "📉 -6.8% YoY\n\n"
        # "🌍 География:\n"
        # "UK: +3%\n"
        # "Германия: -12%\n"
        # "Польша: -9%\n\n"
        # "📊 Общий тренд:\n"
        # "🟡 Снижение континентальной Европы компенсируется UK\n\n"
        # "📌 Вывод:\n"
        # "Рынок ослабевает, но без резкого падения"
    # )
    if message.text == "/status":
        bot.send_message(message.chat.id, "Бот работает стабильно ✅")
bot.infinity_polling()
@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "Бот работает стабильно ✅")
