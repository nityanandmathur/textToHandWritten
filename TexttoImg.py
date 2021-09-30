from tkinter import *
import pywhatkit as kit
from PIL import Image
import time

class MyWindow:
    def __init__(self,win):
        self.lbl = Label(win, text = "Enter your name")
        self.t1 = Entry(bd = 3)
        self.btn = Button(win, text = "Convert", command= self.cnvsn)  
        self.btn1 = Button(win, text = "Show", command = self.disp)    
        self.lbl.place(x = 100, y = 50)
        self.t1.place(x = 220, y = 50)
        self.btn.place(x = 100, y = 100)
        self.btn1.place(x = 200, y = 100)

        


    def cnvsn(self):
        kit.text_to_handwriting(self.t1.get())

    def disp(self):
        im = Image.open(r"F:\GUI\dist\pywhatkit.png")
        im.show()
        

window = Tk()
mywin = MyWindow(window)
window.title("Text to Image")
window.geometry("400x300+10+20")
window.mainloop()