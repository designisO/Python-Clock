from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('Python Timeclock')

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
label = Label(root, font=('arial', 80, 'bold'), background ='darkblue', foreground='white')
label.pack(anchor= 'center')
time()
mainloop()

