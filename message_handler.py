import API_TOKEN as API_TOKEN
import telebot

api_token = API_TOKEN.api_token()
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to my bot.")

bot.polling()