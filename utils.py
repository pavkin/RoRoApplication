# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from SQLighter import SQLighter
from config import database_name

class Sign_in:

    def __init__(self, root):
        self.win_sign_in = Toplevel(root)
        self.win_sign_in.title('Sign in')

        self.frame_sign_in = Frame(self.win_sign_in)

        self.win_sign_in_login = StringVar(self.win_sign_in)

        self.label_login = Label(self.win_sign_in, text = 'Login: ', justify = RIGHT)
        self.entry_login = Entry(self.win_sign_in, textvariable = self.win_sign_in_login, width = 24, bd = 2)

        self.label_login.grid(row = 1, column = 0)
        self.entry_login.grid(row = 1, column = 1)

        self.win_sign_in_password = StringVar(self.win_sign_in)

        self.label_password = Label(self.win_sign_in, text = 'Password: ', justify = RIGHT)
        self.entry_password = Entry(self.win_sign_in, textvariable = self.win_sign_in_password, width = 24, bd = 2)

        self.label_password.grid(row = 2, column = 0)
        self.entry_password.grid(row = 2, column = 1)

        self.but_sign_in = Button(self.win_sign_in)
        self.but_sign_in['text'] = 'Sign in'
        self.but_sign_in.bind('<Button-1>', self.sign_in_enter)
        self.but_sign_in.grid(row = 3, column = 0)

        self.but_cancel = Button(self.win_sign_in)
        self.but_cancel['text'] = 'Cancel'
        self.but_cancel.bind('<Button-1>', self.sign_in_cancel)
        self.but_cancel.grid(row = 3, column = 1)

    def sign_in_enter(self, event):
        base = SQLighter(database_name)
        users_login = base.select('users', 'login', self.win_sign_in_login.get())

        if len(users_login) == 0:
            messagebox.showerror('Error', 'User with this login is not in the database!')
        elif users_login[0][2] != self.win_sign_in_password.get():
            messagebox.showerror('Error', 'Wrong password!')
        else:
            messagebox.showinfo('Success', 'You entered the database!')

        base.close()

        self.win_sign_in.destroy()

    def sign_in_cancel(self, event):
        self.win_sign_in.destroy()

class Sign_up:

    def __init__(self, root):
        self.win_sign_up = Toplevel(root)
        self.win_sign_up.title('Sign up')

        self.frame_sign_up = Frame(self.win_sign_up)

        self.win_sign_up_login = StringVar(self.win_sign_up)

        self.label_login = Label(self.win_sign_up, text = 'Login: ', justify = RIGHT)
        self.entry_login = Entry(self.win_sign_up, textvariable = self.win_sign_up_login, width = 24, bd = 2)

        self.label_login.grid(row = 1, column = 0)
        self.entry_login.grid(row = 1, column = 1)

        self.win_sign_up_password = StringVar(self.win_sign_up)

        self.label_password = Label(self.win_sign_up, text = 'Password: ', justify = RIGHT)
        self.entry_password = Entry(self.win_sign_up, textvariable = self.win_sign_up_password, width = 24, bd = 2)

        self.label_password.grid(row = 2, column = 0)
        self.entry_password.grid(row = 2, column = 1)

        self.but_sign_up = Button(self.win_sign_up)
        self.but_sign_up['text'] = 'Sign up'
        self.but_sign_up.bind('<Button-1>', self.sign_up_enter)
        self.but_sign_up.grid(row = 3, column = 0)

        self.but_cancel = Button(self.win_sign_up)
        self.but_cancel['text'] = 'Cancel'
        self.but_cancel.bind('<Button-1>', self.sign_up_cancel)
        self.but_cancel.grid(row = 3, column = 1)

    def sign_up_enter(self, event):
        base = SQLighter(database_name)
        users_login = base.select('users', 'login', self.win_sign_up_login.get())

        if len(users_login) > 0:
            messagebox.showerror('Error', 'User with this login is already in the database!')
        else:
            base.insert_users(self.win_sign_up_login.get(), self.win_sign_up_password.get())
            messagebox.showinfo('Success', 'You are registered in the database!')

        base.close()

        self.win_sign_up.destroy()

    def sign_up_cancel(self, event):
        self.win_sign_up.destroy()
