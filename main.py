import telebot
from information import TOKEN_BOT

bot = telebot.TeleBot(TOKEN_BOT)
print(TOKEN_BOT)


@bot.message_handler(commands=['start'])
def start_message(message):
    print('Bot start')
    bot.send_message(message.chat.id, 'Привет! Я твой личный помошник по учету твоих финансов! \n'
                        'Не бойся, я не расскажу твоей маме что ты покупаешь пиво))))')


bot.polling(none_stop=True, interval=0)
