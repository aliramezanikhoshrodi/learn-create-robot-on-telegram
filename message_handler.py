from gitignore import API_TOKEN   
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

api_token = API_TOKEN.api_token()
bot = telebot.TeleBot(api_token)

button1 = InlineKeyboardButton(text="my github", url="https://github.com/aliramezanikhoshrodi")
button2 = InlineKeyboardButton(text="my telegram", callback_data="my_info")
inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_keyboard.add(button1, button2)

reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
reply_keyboard.add("button3", "button4")

user_id = []

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to my bot.")
    bot.send_message(message.chat.id, "Please tell me your name.")
    bot.register_next_step_handler(message, get_name)
    if message.chat.id not in user_id:
        user_id.append(message.chat.id)
def get_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"Hello {name}! How old are you?")
    bot.register_next_step_handler(message, get_age, name)
def get_age(message, name):
    age = message.text
    bot.send_message(message.chat.id, f"Name: {name}\nAge: {age}", reply_markup=reply_keyboard)
    bot.send_message(message.chat.id, "Now you can interact with the buttons below.", reply_markup=inline_keyboard)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == "button3":
        bot.reply_to(message, "You clicked button3!")
    elif message.text == "button4":
        bot.reply_to(message, "You clicked button4!")
    else:
        bot.reply_to(message, "Please use the buttons provided.")
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