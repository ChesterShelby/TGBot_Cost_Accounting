import sqlite3


class RegistRation:

    def __init__(self):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(result)

    def add_user(self, user_id):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))

    def update_users(self, user_id):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        return self.cursor.execute("UPDATE 'users' SET 'status' = ? WHERE 'useer_id' = ?", (user_id,))

    def close(self):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        self.connection.close()
