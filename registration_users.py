import sqlite3
import telebot
import datetime
from tokenBot import TOKEN

bot = telebot.TeleBot(TOKEN)
keyboard2 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard2.row('Создать таблицу', 'Калькулятор', 'Удалить таблицу', 'lol')


class RegistRation:

    def __init__(self):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        self.connection.commit()
        self.cursor.close()

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
        id Integer PRIMARY KEY AUTOINCREMENT,
        Categories TEXT
        )""")
        self.connection.commit()
        self.cursor.close()


    def deletetable(self, user_id):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"DROP TABLE '{user_id}'")
        self.connection.commit()
        self.cursor.close()

    def everyday(self, user_id):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        date = datetime.date.today()
        self.cursor.execute(f"SELECT '{date}' FROM '{user_id}'")
        if self.cursor.fetchone() is None:
            self.cursor.execute(f"""ALTER TABLE '{user_id}' ADD COLUMN '{date}' INTEGER""")
        self.connection.commit()
        self.cursor.close()

    def add_expenses(self, user_id):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        date = datetime.date.today()
        self.cursor.execute(f"INSERT INTO '{user_id}' (Categories, {date}) VALUES ()")
        self.connection.commit()
        self.cursor.close()
