from tkinter import *
import tkinter
import time
import sys
from tkinter import messagebox
root = Tk()
root.title("Timer")
title=Label(root,text="This program takes number of hours, minutes and seconds for a timer",fg='green')

title.pack(pady=10)

hours=Label(root,text="Enter number of Hours : ",fg='black')

hours.pack(pady=5)

e1=Entry(root,fg='blue')

e1.pack(pady=5)

hours=Label(root,text="Enter number of Minutes : ",fg='black')

hours.pack(pady=5)
e2=Entry(root,fg='blue')

e2.pack(pady=5)


seconds=Label(root,text="Enter number of Seconds : ",fg='black')

seconds.pack(pady=5)
e3=Entry(root,fg='orange')

e3.pack(pady=5)

def timer_layout(hr,m,s):
    seconds=(hr*3600)+(m*60)+s
    timer_label.config(text=hr+':'+m':'+s)
def update():
    if seconds
    timer_label.config()
    for i in range(seconds):
        print(seconds-i," seconds left")
        time.sleep(1)
    messagebox.showerror(title='Over', message='Timer over')
    try:
        sys.exit()
    except:
        print('exited')



def printan():
    try:
        hour=int(e1.get())
        minute=int(e2.get())
        sec=int(e3.get())
    timer(hour,minute,sec)
    except Exception :
        messagebox.showerror(title='Error', message='Try again')

        

        
              
button=Button(root,text='Click to Enter the value',command=printan,bg='black',fg='white')
button.pack(pady=5)
root.mainloop()
