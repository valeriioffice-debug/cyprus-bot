import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот запущен 🚀")

@bot.message_handler(commands=['status'])
def status(message):
    bot.send_message(message.chat.id, "Статус: работает ✅")

print("Bot is running...")
bot.infinity_polling()
@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "Бот работает стабильно ✅")
