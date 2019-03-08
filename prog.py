# -*- coding: utf-8 -*-
from tkinter import *
from utils import Sign_in, Sign_up

def event_sign_in(event):
    win_sign_in = Sign_in(root)

def event_sign_up(event):
    win_sign_up = Sign_up(root)

root = Tk()
root.minsize(800, 600)
root.title('RoRo - приложение')

but_sign_in = Button(root)
but_sign_in['text'] = 'Sign in'
but_sign_in.bind('<Button-1>', event_sign_in)
but_sign_in.grid(row = 1, column = 0)

but_sign_up = Button(root)
but_sign_up['text'] = 'Sign up'
but_sign_up.bind('<Button-1>', event_sign_up)
but_sign_up.grid(row = 2, column = 0)

root.mainloop()
