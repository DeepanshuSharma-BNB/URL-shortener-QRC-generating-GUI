# url shortner and copy it to clipboard

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pyshorteners
import pyqrcode
import png
from pyqrcode import QRCode
import clipboard

win = Tk()
win.geometry("350x160")
win.resizable(width=False, height=False)
win.title("URL Shortener/QR Code Generator")

def link_short():
    global sl
    sl = str(e1.get())
    global s
    s = pyshorteners.Shortener().tinyurl.short(sl)
    lkshort.set(s)

def copy_link():
    clipboard.copy(s)

def qrc_gen():
    try:
        url = pyqrcode.create(sl)
        url.png('myqrcode.png', scale = 10)
        messagebox.showinfo(" ", "QR Code Generated!")
    except:
        messagebox.showerror("Error", "Please provide valid input!")

lkshort=StringVar();
Label(win, text="Write link here: ").place(x = 20, y = 40)
b1 = Button(win, text="Shorten the Link", command=link_short, fg = "black", bg = "light grey", font="-size 9 -weight bold").place(x = 20, y = 100)
b2 = Button(win, text="Copy Link", command=copy_link, fg = "black", bg = "light grey", font="-size 9 -weight bold").place(x = 140, y = 100)
b3 = Button(win, text="Generate QR code", command=qrc_gen, fg = "black", bg = "light grey", font="-size 9 -weight bold").place(x = 220, y = 100)

e1 = Entry(win)
e1.place(x = 120, y = 40)
e2 = Entry(win, textvariable=lkshort)
e2.place(x = 120, y = 70)

win.mainloop()
