# -*- coding: utf-8 -*-
from tkinter import *
from utils import Sign_in, Sign_up

def event_btn_sign_in(event):
    win_sign_in = Sign_in(root)

def event_btn_sign_up(event):
    win_sign_up = Sign_up(root)

root = Tk()
root.title('RoRo - приложение')

header = Label(root, text = 'RoRo - Application')
header.grid(row = 0, column = 0)

btn_sign_in = Button(root, text = 'Sign in', width = 24, height = 2)
btn_sign_in.bind('<Button-1>', event_btn_sign_in)
btn_sign_in.grid(row = 1, column = 0)

btn_sign_up = Button(root, text = 'Sign up', width = 24, height = 2)
btn_sign_up.bind('<Button-1>', event_btn_sign_up)
btn_sign_up.grid(row = 2, column = 0)

root.mainloop()
