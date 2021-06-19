api_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'

import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
from arrays import loading_messages
import threading
import os
from tkinter import messagebox as msg  
from PIL import Image, ImageTk
from gtts import gTTS


def error(t):                                 
    info = msg.showerror('Error', t)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Personal Assistant")
        self.minsize(500,400)

        
        
        container = tk.Frame(self)
        self.tk.call('wm', 'iconphoto', self._w, tk.PhotoImage(file='C:/Users/home/OneDrive/Desktop/Coding/Hackathon/NHacks VI/app/Modules/icon.png'))

        container.pack(side = "top", fill = "both", expand = True)
        

        self.frames = {} 
        for F in (StartPage, Main):
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(x = 0, y = 0)
            
        self.show_frame(Main)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='green', background='#03a5fc')
        self['bg'] = '#03a5fc'

        gen_loading_msg = random.choice(loading_messages)
        loading_msg = tk.Message(self, width=300, text = gen_loading_msg, background='#03a5fc')
        self.my_progress = ttk.Progressbar(self,style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=300, mode='determinate')

        self.my_progress.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        loading_msg.place(relx = 0.5, rely = 0.4, anchor = CENTER)
        
    
    def changeProgVal(self, num):
        self.my_progress.start(num)
        
class Main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        background_image = Image.open("C:/Users/home/OneDrive/Desktop/Coding/Hackathon/NHacks VI/app/Modules/bg.jpg")
        
        Font_tuple = ("calibri", 16, "bold")
        canvas_for_image = Canvas(self, borderwidth=0, highlightthickness=0)
        canvas_for_image.image = ImageTk.PhotoImage(background_image.resize((200, 200), Image.ANTIALIAS))
        canvas_for_image.create_image(0, 0, image=canvas_for_image.image, anchor='nw')
        canvas_for_image.place(relx=0.1, relwidth=1, relheight=1, rely=0.9, anchor=CENTER)
        heading1 = tk.Message(self, width=300, text = 'Assisto', font=Font_tuple)

        heading1.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        

    
# app = tkinterApp()
# app.mainloop()


