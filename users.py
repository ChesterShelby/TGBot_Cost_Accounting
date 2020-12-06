import sqlite3

class NewUser:

    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def new_user(self):
        with self.connection:
