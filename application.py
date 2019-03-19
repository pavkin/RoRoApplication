# -*- coding: utf-8 -*-
from tkinter import *
from sign_in import Sign_in
from sign_up import Sign_up
from SQLighter import SQLighter
from config import database_name
from PIL import Image, ImageTk
from PIL import *
import requests, re

class Application(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master) 
        self.grid() 
        self.create_app_widgets()

    def clear_widgets(self):
        items = self.grid_slaves()
        for item in items:
            item.destroy()
        
    def create_app_widgets(self):
        self.header = Label(self, text = 'RoRo - Application')
        self.header.grid(row = 0, column = 0)

        self.btn_sign_in = Button(self, text = 'Sign in', width = 24, height = 2)
        self.btn_sign_in.bind('<Button-1>', self.event_btn_sign_in)
        self.btn_sign_in.grid(row = 1, column = 0)

        self.btn_sign_up = Button(self, text = 'Sign up', width = 24, height = 2)
        self.btn_sign_up.bind('<Button-1>', self.event_btn_sign_up)
        self.btn_sign_up.grid(row = 2, column = 0)

    def create_main_widgets(self):    
        self.search = StringVar(self)

        self.entry_search = Entry(self, textvariable = self.search, width = 64)
        self.entry_search.grid(row = 0, column = 0)

        self.btn_search = Button(self, text = 'Search', width = 16, height = 1)
        self.btn_search.bind('<Button-1>', self.get_image)
        self.btn_search.grid(row = 0, column = 1)

        self.image_frame = Frame(self)
        self.image_frame.grid(row = 1, column = 0, columnspan = 2)

    def get_image(self, event):
        name = self.search.get()
        url = 'https://scryfall.com/search?q=' + str(name)
        req = requests.get(url)
        html_content = req.text

        result = re.findall('(?<=title\=").*?https://img\.scryfall\.com/cards/.*?(?=")', html_content)
        
        i = 0
        while i < len(result):
            result[i] = re.split(' ; ', re.sub(' \(.*?\)".*(?=https://img\.scryfall\.com/cards/.*?)', ' ; ', result[i]))
            file_name = re.sub('__', '_', re.sub('__', '_', re.sub('[^a-zA-Z]', '_', result[i][0]))).lower()
            name = result[i][0]
            url = result[i][1]

            i += 1

            base = SQLighter(database_name)

            if len(base.select_images(name)) > 0:
                base.close()
            else:
                image = requests.get(url)
                cat = open("img\\" + file_name + ".jpg", "wb")
                cat.write(image.content)
                cat.close()

                base.insert_images(name, file_name + ".jpg")
                
                base.close()
        
            im = Image.open("img\\" + file_name + ".jpg")
            ph = ImageTk.PhotoImage(im)

            label = Label(self.image_frame, image=ph)
            label.image=ph
            label.grid(row = i, column = 0)

            break;


    def event_btn_sign_in(self, event):
        win_sign_in = Sign_in(self)

    def event_btn_sign_up(self, event):
        win_sign_up = Sign_up(self)
        
app = Application() 
app.master.title('RoRo - application') 
app.mainloop()
