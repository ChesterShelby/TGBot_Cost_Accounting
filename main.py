import telebot
from information import TOKEN_BOT
from registration_users import RegistRation

bot = telebot.TeleBot(TOKEN_BOT)
db = RegistRation('db.db')
keyboard1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard1.row('/start', '/reg', '/unreg')


@bot.message_handler(commands=['start'])
def start_message(message):
    print('Bot start')
    bot.send_message(message.chat.id, 'Привет! Я твой личный помошник по учету твоих финансов! \n' 'Не бойся, я не '
                                        'расскажу твоей маме, что ты покупаешь пиво))))', reply_markup=keyboard1)


@bot.message_handler(commands=['reg'])
def register(message):
    print(1)
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
    else:
        db.update_users(message.from_user.id, True)
    bot.send_message(message.chat.id, "Вы успешно зарегистрировались", reply_markup=keyboard1)


@bot.message_handler(commands=['unreg'])
def register(message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id, False)
        bot.send_message(message.chat.id, "Вы и так не зарегистрированы", reply_markup=keyboard1)
    else:
        db.update_users(message.from_user.id, False)
        bot.send_message(message.chat.id, "Ваша таблица расходов удалена", reply_markup=keyboard1)


bot.polling(none_stop=True, interval=0)
