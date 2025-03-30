import telebot
from dotenv import load_dotenv
import os
import AiModel

load_dotenv()


BOT_KEY = os.getenv("BOT_KEY")
bot = telebot.TeleBot(BOT_KEY)

valid_user = False
@bot.message_handler(commands=['9b8027a83c4088dd90a104ac75acca9d09bd08f6'])
def start(message):
    global valid_user
    valid_user = True
    bot.reply_to(message, "¡Hola! Soy tu asistente personal. ¿En qué puedo ayudarte hoy? Procura por favor NO ENVIAR tantos mensajes en un periodo corto de tiempo")

@bot.message_handler(commands=['stop'])
def stop(message):
    global valid_user
    if valid_user:
        bot.reply_to(message, "¡Hasta luego!")
        bot.stop_polling()


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global valid_user
    if valid_user:
        response = AiModel.message_gen(message.text,bot,message)
        bot.reply_to(message,response)
        



if __name__ == "__main__":
    bot.polling(none_stop=True)




