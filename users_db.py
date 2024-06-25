import sqlite3

class UsersDB():
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (user TEXT PRIMARY KEY, password TEXT)''')
        self.conn.commit()

    def read_db(self, user_name: str, password: str):
        self.cursor.execute('''SELECT * FROM users WHERE user=? AND password=?''', (user_name, password))
        result = self.cursor.fetchone()
        if result:
            return True
        return False

    def write_db(self, user_name: str, password: str):
        self.cursor.execute('''INSERT INTO users (user, password) VALUES (?,?)''', (user_name, password))
        self.conn.commit()
        return True