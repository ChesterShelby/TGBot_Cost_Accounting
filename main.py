import telebot
import sqlite3
import datetime
from registration_users import RegistRation
from tokenBot import TOKEN


bot = telebot.TeleBot(TOKEN)
db = RegistRation()
keyboard1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard1.row('/start', 'Регистрация', 'Обо мне')
keyboard2 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
item1 = ['Создать таблицу', 'Калькулятор']
item2 = ['Удалить таблицу', 'Добавить расход']
keyboard2.row(item1, item2)
keyboard3 = telebot.types.InlineKeyboardMarkup()
keyboard3.row(telebot.types.InlineKeyboardButton('Да', callback_data='yes'),
              telebot.types.InlineKeyboardButton('Нет', callback_data='no'))
keyboard4 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)



@bot.message_handler(commands=['start'])
def start_message(message):
    print('Bot start')
    bot.send_message(message.chat.id, 'Привет! Я твой личный помошник по учету твоих финансов!', reply_markup=keyboard1)


@bot.message_handler(regexp="Регистрация")
def register(message):
    db.adduser(message.from_user.id, message)
    print('Зарегистрирован новый пользователь')


@bot.message_handler(regexp="Создать таблицу")
def create_table(message):
    db.createtable(message.from_user.id, message)
    #db.everyday(message.from_user.id)
    print('Создана таблица для пользователя')
    bot.send_message(message.chat.id, 'Создаем ради тебя целую таблицу...')
    take_categories(message)


def take_categories(message):
    sent = bot.send_message(message.from_user.id, 'Напиши категории затрат через пробел')
    bot.register_next_step_handler(sent, add_categories)


def add_categories(message):
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    mes = message.text
    mes = str(mes)
    user_id = message.from_user.id
    categories = mes.split(' ')
    print(categories)
    print(user_id)
    for i in range(len(categories)):
        cursor.execute(f"""INSERT INTO '{user_id}' (Categories) VALUES (?)""", (categories[i],))
    bot.send_message(message.from_user.id, 'Таблица создана', reply_markup=keyboard2)
    connection.commit()
    cursor.close()


@bot.message_handler(regexp="Удалить таблицу")
def delete_table(message):
    bot.send_message(message.chat.id, 'Ты уверен? Все твои расходы и данные о тебе будут удалены...',
                     reply_markup=keyboard3)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'yes':
        db.deletetable(call.message.chat.id)
        print('Удалена таблица пользователя')
        bot.send_message(call.message.chat.id, 'Таблица удалена')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Хорошо, продолжаем', reply_markup=keyboard4)


@bot.message_handler(regexp="Добавить расход")
def get_categories(message):
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    user_id = message.chat.id
    result = cursor.description(f"SELECT Categories FROM '{user_id}'").fetchall()
    bot.send_message(message.chat.id, result)
    sent = bot.send_message(message.chat.id, "Напиши категорию в которую хочешь вставить  данные и сколько ты потратил",
                            result)
    bot.register_next_step_handler(sent, safe_massage_categories)


def safe_massage_categories(message):
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    mes = message.text
    user_id = message.from_user.id
    categories = mes.split(' ')
    print(categories)
    date = datetime.date.today()
    cursor.execute(f"""INSERT INTO '{user_id}' ('{categories[0]}','{date}') VALUES (?)""", (categories[1],))




bot.polling(none_stop=True, interval=0)
