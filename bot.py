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


bot.infinity_polling()