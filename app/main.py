from Modules.ui import tkinterApp
from tkinter import messagebox as msg  

    
def error(t):                                 
   info = msg.showerror('Error', t)
try:
    app = tkinterApp()
    app.mainloop()
except Exception as e:
    error(f'Error: {e}')
# app.iconbitmap("Modules/icon.png")

quit()

