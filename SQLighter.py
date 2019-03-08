# -*- coding: utf-8 -*-
import sqlite3

class SQLighter:

    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def count(self, table):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM ' + str(table)).fetchall()
            return len(result)

    def select(self, table, column, value):
        with self.connection:
            return self.cursor.execute('SELECT * FROM ' + str(table) + ' WHERE ' + str(column) + ' = ?', (value, )).fetchall()

    def insert_users(self, login, password):
        with self.connection:
            self.cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (self.count('users') + 1, login, password, ))

    def close(self):
        self.connection.close()
