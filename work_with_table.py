import sqlite3


class WorkWithTable:

    def create_table(self, user_id):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 'user_id' = ? (
        login TEXT
        id INTEGER
        )""", (user_id,))

