import telebot
from information import TOKEN_BOT
from registration_users import RegistRation


bot = telebot.TeleBot(TOKEN_BOT)
db = RegistRation()
keyboard1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard1.row('/start', '/регистрация')
keyboard2 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard2.row('/Создать таблицу', '/calculator')


@bot.message_handler(commands=['start'])
def start_message(message):
    print('Bot start')
    bot.send_message(message.chat.id, 'Привет! Я твой личный помошник по учету твоих финансов! \n' 'Не бойся, я не '
                                      'расскажу твоей маме, что ты покупаешь пиво))))', reply_markup=keyboard1)


@bot.message_handler(commands=['регистрация'])
def register(message):
    print(1)
    db.adduser(message.from_user.id, message)


@bot.message_handler(commands=['Создать таблицу'])
def createtable():
    


@bot.message_handler(commands=['calculator'])
def calcul(message):
    bot.send_message(message.chat.id, "Данная опция еще в разработке))", reply_markup=keyboard2)


bot.polling(none_stop=True, interval=0)
