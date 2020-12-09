import sqlite3
import telebot
import datetime
from information import TOKEN_BOT
bot = telebot.TeleBot(TOKEN_BOT)
keyboard2 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard2.row('/table', '/calculator')


class RegistRation:

    def __init__(self):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        self.connection.commit()

    def adduser(self, user_id, message):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT user_id FROM users")
        if self.cursor.fetchone() is None:
            self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
            bot.send_message(message.chat.id, "Вы зарегистрированы", reply_markup=keyboard2)
        else:
            bot.send_message(message.chat.id, "Вы уже зарегистрированы", reply_markup=keyboard2)
        self.connection.commit()
        self.cursor.close()

    def createtable(self, user_id, message):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS '{user_id}' (
        Categories TEXT
        )""")
        self.connection.commit()
        self.cursor.close()


    def deletetable(self, user_id, message):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"DROP TABLE '{user_id}'")
        self.connection.commit()
        self.cursor.close()
        bot.send_message(message.chat.id, 'Ня.пока...', reply_markup=keyboard2)

    def everyday(self, user_id):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        date = datetime.date.today()
        self.cursor.execute(f"SELECT '{date}' FROM '{user_id}'")
        if self.cursor.fetchone() is None:
            self.cursor.execute(f"""ALTER TABLE '{user_id}' ADD COLUMN '{date}' INTEGER""")
        self.connection.commit()
        self.cursor.close()

    def take_categories(self, user_id, message):
        sent = bot.send_message(message.from_user.id, 'Напиши категории затрат через пробел', reply_markup=keyboard2)
        bot.register_next_step_handler(sent, self.add_categories(user_id, message))

    def add_categories(self, user_id, message):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        sent = message.text
        sent = str(sent)
        categories = sent.split(' ')
        for i in range(len(categories)):
            print(categories[i])
            # cursor.execute(f"""INSERT INTO '{user_id}' (Categories) VALUES (?)""", categories[i])
        bot.send_message(message.chat.id, sent)
        self.connection.commit()
        self.cursor.close()


