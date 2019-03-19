# -*- coding: utf-8 -*-
import sqlite3

class SQLighter:

    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def count_users(self):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM users').fetchall()
            return len(result)

    def insert_users(self, login, password):
        with self.connection:
            self.cursor.execute('INSERT INTO users VALUES(?, ?, ?)', (self.count_users(), login, password))
            self.cursor.execute('INSERT INTO user_balance VALUES(?, ?, ?)', (self.count_user_balance(), self.count_users(), 500))
            
    def select_users(self, login):
        with self.connection:
            return self.cursor.execute('SELECT * FROM users WHERE login = ?', (login, )).fetchall()

    def delete_users(self, login):
        with self.connection:
            user = self.cursor.execute('SELECT * FROM users WHERE login = ?', (login, )).fetchall()[0]
            self.cursor.execute('DELETE FROM user_data WHERE user = ?', (user[0], ))
            self.cursor.execute('DELETE FROM user_balance WHERE user = ?', (user[0], ))
            self.cursor.execute('DELETE FROM user_images WHERE user = ?', (user[0], ))
            self.cursor.execute('DELETE FROM users WHERE id = ?', (login, ))

    def count_images(self):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM images').fetchall()
            return len(result)

    def insert_images(self, name, file_name):
        with self.connection:
            self.cursor.execute('INSERT INTO images VALUES(?, ?, ?)', (self.count_images(), name, file_name))

    def select_images(self, name):
        with self.connection:
            return self.cursor.execute('SELECT * FROM images WHERE name = ?', (name, )).fetchall()

    def count_user_balance(self):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM user_balance').fetchall()
            return len(result)

    def select_user_balance(self, login):
        with self.connection:
            user_id = self.select_users(login)[0]
            return self.cursor.execute('SELECT * FROM user_balance WHERE user = ?', (user_id, ))

    def update_user_balance(self, login, value):
        with self.connection:
            user_id = self.select_users(login)[0]
            self.cursor.execute('UPDATE user_balance SET balance = ? WHERE user = ?', (login, user_id, )) 

    def close(self):
        self.connection.close()
