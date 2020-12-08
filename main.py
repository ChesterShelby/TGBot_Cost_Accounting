import telebot
from information import TOKEN_BOT
from registration_users import RegistRation


bot = telebot.TeleBot(TOKEN_BOT)
db = RegistRation()
keyboard1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard1.row('/start', '/регистрация')
keyboard2 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard2.row('/table', '/calculator')
keyboard3 = telebot.types.InlineKeyboardMarkup()
keyboard3.row(telebot.types.InlineKeyboardButton('Да', callback_data='yes'),
              telebot.types.InlineKeyboardButton('Нет', callback_data='no'))




@bot.message_handler(commands=['start'])
def start_message(message):
    print('Bot start')
    bot.send_message(message.chat.id, 'Привет! Я твой личный помошник по учету твоих финансов! \n' 'Не бойся, я не '
                                      'расскажу твоей маме, что ты покупаешь пиво))))', reply_markup=keyboard1)


@bot.message_handler(commands=['регистрация'])
def register(message):
    db.adduser(message.from_user.id, message)
    print('Зарегистрирован новый пользователь')


@bot.message_handler(commands=['table'])
def create_table(message):
    db.createtable(message.from_user.id, message)
    db.everyday(message.from_user.id)
    print('Создана таблица для пользователя')


@bot.message_handler(commands=['deletetable'])
def delete_table(message):
    bot.send_message(message.chat.id, 'Ты уверен? Все твои расходы и данные о тебе будут удалены...',
                     reply_markup=keyboard3)
    db.deletetable(message.from_user.id, message)
    print('Удалена таблица пользователя')


@bot.message_handler(commands=['calculator'])
def calcul(message):
    bot.send_message(message.chat.id, "Данная опция еще в разработке))", reply_markup=keyboard2)


bot.polling(none_stop=True, interval=0)
