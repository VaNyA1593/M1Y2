import config
import telebot
import random

API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am CoinBot.
I Can do /coin\и
""")


@bot.message_handler(commands=['coin'])
def coin(message):
    coinv = ["oryol","reshka"]
    answer = random.choice(coinv)
    bot.reply_to(message, f""" {answer}
""")

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)


bot.infinity_polling()