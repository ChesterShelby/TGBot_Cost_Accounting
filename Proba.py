import telebot
from information import TOKEN_BOT

bot = telebot.TeleBot(TOKEN_BOT)

@bot.message_handler(commands=['calculator'])
def start_message(message):
    print('start calculator')
    bot.send_message(message.chat.id, 'Запускаю калькулятор...')
    #Здесь должен быть запуск кода из другого файла, чтобы работал калькулятор, я все написал чтобы код конектился к боту
    #просто запусти этот код, как все сделаешь и напиши боту /calculator , должно все работать)