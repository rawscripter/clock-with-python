from tkinter import *

from time import strftime

root = Tk()
root.title("Clock")

# root.geometry('200x100')
root.configure(background='#000')


def time():
    string = strftime("%I-%M-%S %p")
    timeLabel.config(text=string)
    timeLabel.after(1000, time)
    dateString = strftime("%d-%m-%Y")
    dateaLabel.config(text=dateString)


timeLabel = Label(root,
                  background="#000000", foreground="#aaf0d1", pady=2, padx=10)
timeLabel.config(font=("Fira Code", 30))

timeLabel.pack(anchor='center')


dateaLabel = Label(root,
                   background="#000000", foreground="#aaf0d1")
dateaLabel.config(font=("Fira Code", 25))

dateaLabel.pack(anchor='center')


time()


mainloop()
