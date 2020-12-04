import sqlite3


class RegistRation:

    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_users(self, status=True):
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'users' WHERE 'status' = ?", (status,)).fetchall()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id, status=True):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id', 'status') VALUES (?,?)", (user_id, status))

    def update_users(self, user_id, status):
        return self.cursor.execute("UPDATE 'users' SET 'status' = ? WHERE 'useer_id' = ?", (user_id, status))

    def close(self):
        self.connection.close()
