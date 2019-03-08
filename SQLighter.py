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
            self.cursor.execute('INSERT INTO users VALUES(?, ?, ?)', (self.count_users() + 1, login, password))

    def select_users(self, login):
        with self.connection:
            return self.cursor.execute('SELECT * FROM users WHERE login = ?', (login, )).fetchall()

    def close(self):
        self.connection.close()
