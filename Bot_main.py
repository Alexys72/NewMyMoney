from consts import *
import telebot


bot = telebot.TeleBot("5107602714:AAHPy02DSuZwBBifglq-ALAybX0SnD-lglY")


@bot.message_handler(func=lambda message: message.text.lower().startswith("привет"))
def send_message(message):
    bot.send_message(message.chat.id, "Привет! Начнем стого, как мне тебя называть?")


@bot.message_handler(func=lambda message: message.text.lower().startswith(f"Хорошо,{S_ENTER_NAME}"))
def send_message(message):
    bot.send_message(message.chat.id, "name")
    consts.set_state(message.chat.id, config.States.S_ENTER_NAME.value)

bot.infinity_polling()


