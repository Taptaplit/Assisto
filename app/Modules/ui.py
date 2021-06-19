import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
from arrays import loading_messages
from Modules.internet import SpeedTest
from Modules.Assistant import fetch_microphone_input, respond, record
import threading
import os
from tkinter import messagebox as msg  
from PIL import Image, ImageTk
from gtts import gTTS


def error(t):                                 
    info = msg.showerror('Error', t)

def internetCheck(load, control):
    sped = SpeedTest()
    load.start(30)
    sped.getBestServer()
    load.start(60)
    sped1, sped2 = sped.download_upload()
    if float(sped1) >= 5.0 and float(sped2) >= 5.0:
        print(sped1, sped2)
        load.start(100)
        control.show_frame(Main)
        return
    else:
        error("You need internet connection above 5 mibs!")
        control.destroy()


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Personal Assistant")
        self.minsize(500,400)
        
        container = tk.Frame(self)
        self.tk.call('wm', 'iconphoto', self._w, tk.PhotoImage(file='C:/Users/home/OneDrive/Desktop/Coding/Hackathon/NHacks VI/app/Modules/icon.png'))

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} 
        for F in (StartPage, Main):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
            
        self.show_frame(StartPage)

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
        
        self.after(200, lambda: threading.Thread(target=internetCheck, args=(self.my_progress,controller)).start())
    
    def changeProgVal(self, num):
        self.my_progress.start(num)
        
class Main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        image = Image.open("C:/Users/home/OneDrive/Desktop/Coding/Hackathon/NHacks VI/app/Modules/record.png")
        image1 = Image.open("C:/Users/home/OneDrive/Desktop/Coding/Hackathon/NHacks VI/app/Modules/icon.png")
        bgimage = Image.open("C:/Users/home/OneDrive/Desktop/Coding/Hackathon/NHacks VI/app/Modules/icon.png")
        
        
        
        self.btnText = tk.StringVar()
        self.btnText.set("Enable Microphone")
        self.recordBool = tk.StringVar()
        self.recordBool.set("false")
        self.listenText = tk.StringVar()
        self.listenText.set("No Audio Detected")
        Font_tuple = ("Comic Sans MS", 16, "bold")
        
        background_image = ImageTk.PhotoImage(bgimage.resize((500, 400), Image.ANTIALIAS))
        background_label = Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)    
        heading1 = tk.Message(self, width=300, text = 'Assisto', font=Font_tuple)
        self.pre_entry_text = ttk.Label(self, textvariable=self.listenText)
        btn = tk.Button(self, textvariable=self.btnText, borderwidth = '0', bg='#03a5fc', relief=FLAT, activebackground="#04e000", command = lambda: threading.Thread(target=self.setBtnText).start())
        
        canvas_for_image1 = Canvas(self, borderwidth=0, highlightthickness=0)
        canvas_for_image1.image = ImageTk.PhotoImage(image1.resize((200, 200), Image.ANTIALIAS))
        canvas_for_image1.create_image(0, 0, image=canvas_for_image1.image, anchor='nw')
        
        canvas_for_image = Canvas(self, borderwidth=0, highlightthickness=0)
        canvas_for_image.image = ImageTk.PhotoImage(image.resize((40, 40), Image.ANTIALIAS))
        canvas_for_image.create_image(0, 0, image=canvas_for_image.image, anchor='nw')
        canvas_for_image.bind("<Button-1>", self.pushToRecord)
        text = Entry(self, bg="#6c9fce", relief=FLAT, font=('calibri', 12))
        entryBtn = tk.Button(self, text="Send", height=1, bg='#03a5fc', relief=FLAT, activebackground="#04e000", command=lambda: threading.Thread(target=respond, args=(text.get(),)).start())
        
        heading1.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        self.pre_entry_text.place(relx = 0.2, rely = 0.4, anchor = CENTER)
        btn.place(relx = 0.2, rely = 0.5, anchor = CENTER)
        canvas_for_image1.place(relx=0.9,  rely=0.6, anchor=CENTER)
        canvas_for_image.place(relx=0.1, relwidth=0.1, relheight=0.1, rely=0.9, anchor=CENTER)
        text.place(relx = 0.4, rely = 0.9, anchor = CENTER, relwidth=0.4)
        entryBtn.place(relx = 0.8, rely = 0.9, anchor = CENTER, relwidth=0.3)
        
    def setBtnText(self):
        get = self.btnText.get()
        if (get == 'Enable Microphone'):
            self.btnText.set("Stop")
            return self.runMicrophone()
        else:
            self.btnText.set('Enable Microphone')
            self.listenText.set('No Audio Detected')
            return
    def pushToRecord(self, e):
        threading.Thread(target=self.recordAudio).start()
    def recordAudio(self):
        get = self.recordBool.get()
        if get == "false":
            self.recordBool.set("true")
            return self.recordMic()
        else:
            self.recordBool.set("false")
    
    def runMicrophone(self):
        while True:
            if (self.btnText.get() == 'Stop'):
                self.listenText.set('Listening')
                fetch_microphone_input(self.listenText)
            if (self.btnText.get() == 'Enable Microphone'):
                break
    
    def recordMic(self):
        text = ''
        while True:
            if (self.recordBool.get() == 'true'):
                textData = record()
                text += textData
            if (self.recordBool.get() == 'false'):
                print(text)
                tts = gTTS(text, lang='en')
                tts.save('assisto-recorded-audio.mp3')
                break