from gitignore import API_TOKEN   
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

api_token = API_TOKEN.api_token()
bot = telebot.TeleBot(api_token)

button1 = InlineKeyboardButton(text="my github", url="https://github.com/aliramezanikhoshrodi")
button2 = InlineKeyboardButton(text="my telegram", callback_data="my_info")
inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_keyboard.add(button1, button2)

user_id = []

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to my bot.", reply_markup=inline_keyboard)
    if message.chat.id not in user_id:
        user_id.append(message.chat.id)

@bot.message_handler(regexp="(^hello|hi|hey)$")
def greet(message):
    bot.reply_to(message, "Hello! How are you?")

@bot.message_handler(commands=['SURPRISE'])
def surprise(message):
    for id in user_id:
        bot.send_message(id, "SURPRISE!!")

@bot.callback_query_handler(func=lambda call: True)
def call(call):
    if call.data == "my_info":
        bot.answer_callback_query(call.id, "My name is Ali Ramezani Khoshrodi. You can find me on GitHub or Telegram.", show_alert=True)
    else:
        bot.answer_callback_query(call.id, "Unknown command.", show_alert=True)

bot.polling()