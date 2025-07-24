from gitignore.API_TOKEN import API_TOKEN   
import telebot

api_token = API_TOKEN.api_token()
bot = telebot.TeleBot(api_token)

user_id = []

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to my bot.")
    if message.chat.id not in user_id:
        user_id.append(message.chat.id)

@bot.message_handler(regexp="(^hello|hi|hey)$")
def greet(message):
    bot.reply_to(message, "Hello! How are you?")

@bot.message_handler(commands=['SURPRISE'])
def surprise(message):
    for id in user_id:
        bot.send_message(id, "SURPRISE!!")

bot.polling()