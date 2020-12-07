import sqlite3
import telebot
from information import TOKEN_BOT
bot = telebot.TeleBot(TOKEN_BOT)


class RegistRation:

    def adduser(self, user_id, message):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT user_id FROM users")
        if self.cursor.fetchone() is None:
            self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
            bot.send_message(message.chat.id, "Вы зарегистрированы")
        else:
            bot.send_message(message.chat.id, "Вы уже зарегистрированы")
        self.connection.commit()
        self.cursor.close()
