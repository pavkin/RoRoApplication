# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from SQLighter import SQLighter
from config import database_name

class Sign_in(object):

    def __init__(self, root):
        self.win = Toplevel(root)
        self.title = 'Sign in'

        self.login = StringVar(self.win)

        self.label_login = Label(self.win, text = 'Login: ')
        self.entry_login = Entry(self.win, textvariable = self.login, width = 24, bd = 2)

        self.label_login.grid(row = 0, column = 0)
        self.entry_login.grid(row = 0, column = 1)

        self.password = StringVar(self.win)
        
        self.label_password = Label(self.win, text = 'Password: ')
        self.entry_password = Entry(self.win, textvariable = self.password, width = 24, bd = 2)

        self.label_password.grid(row = 1, column = 0)
        self.entry_password.grid(row = 1, column = 1)

        self.btn_sign_in = Button(self.win, text = 'Sign in', width = 12)
        self.btn_sign_in.bind('<Button-1>', self.event_sign_in)
        self.btn_sign_in.grid(row = 2, column = 0)

        self.btn_cancel = Button(self.win, text = 'Cancel', width = 12)
        self.btn_cancel.bind('<Button-1>', self.event_cancel)
        self.btn_cancel.grid(row = 2, column = 1)
        
        self.win.mainloop()

    def event_sign_in(self, event):
        base = SQLighter(database_name)
        users = base.select_users(self.login.get())

        if len(users) == 0:
            messagebox.showerror('Error', 'User with this login is not in the database!')
            base.close()
            return
        elif users[0][2] != self.password.get():
            messagebox.showerror('Error', 'Wrong password!')
            base.close()
            return
        else:
            # Past code...
            messagebox.showinfo('Success', 'You entered the database!')

        base.close()

        self.win.destroy()

    def event_cancel(self, event):
        self.win.destroy()

class Sign_up(object):

    def __init__(self, root):
        self.win = Toplevel(root)
        self.title = 'Sign up'

        self.login = StringVar(self.win)

        self.label_login = Label(self.win, text = 'Login: ')
        self.entry_login = Entry(self.win, textvariable = self.login, width = 24, bd = 2)

        self.label_login.grid(row = 0, column = 0)
        self.entry_login.grid(row = 0, column = 1)

        self.password = StringVar(self.win)
        
        self.label_password = Label(self.win, text = 'Password: ')
        self.entry_password = Entry(self.win, textvariable = self.password, width = 24, bd = 2)

        self.label_password.grid(row = 1, column = 0)
        self.entry_password.grid(row = 1, column = 1)

        self.btn_sign_up = Button(self.win, text = 'Sign up', width = 12)
        self.btn_sign_up.bind('<Button-1>', self.event_sign_up)
        self.btn_sign_up.grid(row = 2, column = 0)

        self.btn_cancel = Button(self.win, text = 'Cancel', width = 12)
        self.btn_cancel.bind('<Button-1>', self.event_cancel)
        self.btn_cancel.grid(row = 2, column = 1)
        
        self.win.mainloop()

    def event_sign_up(self, event):
        base = SQLighter(database_name)
        users = base.select_users(self.login.get())

        if len(users) > 0:
            messagebox.showerror('Error', 'User with this login is already in the database!')
            base.close()
            return
        else:
            base.insert_users(self.login.get(), self.password.get()) 
            messagebox.showinfo('Success', 'You are registred in the database!')

        base.close()

        self.win.destroy()

    def event_cancel(self, event):
        self.win.destroy() 
                                 
