import pyshorteners
from tkinter import *

win = Tk()
win.geometry("400x270")
win.config(bg='skyblue')
#button function
def short():
    url= Url_text.get()
    s = pyshorteners.Shortener().tinyurl.short(url)
    URL_short.insert(END,s)
#label for entering user url
Label(win,text="Enter Your URL link", font="impack 17 bold",bg='black',fg='white').pack(fill="x")
#Entry box
Url_text=Entry(win,font="10",bd=3,width=40)
Url_text.pack(pady=20)
#submit button
Button(win,text="Click here",font='impack 12 bold', bg='pink', fg='white',command=short).pack()
#Short url
URL_short=Entry(win,font="impack 15 bold",bg="skyblue", width=30,bd=0)
URL_short.pack(pady=30)
mainloop()
