from tkinter import *
import tkinter
import time
import sys
from tkinter import messagebox
root = Tk()
root.title("Timer")
root.geometry("500x500")
title=Label(root,text="This program is a stopwatch in seconds",fg='green')

title.pack(pady=10)


seconds=Label(root,text="Enter number of Seconds : ",fg='black')

seconds.pack(pady=5)
e=Entry(root,fg='blue')

e.pack(pady=5)

def stopwatch_layout(s):
    seconds=0
    stopwatch_label.config(text="Number of Seconds  :"+str(seconds+1))
    for i in range(s):
        stopwatch_label.after(1000,stopwatch_layout(s+1))
    

def stop():
    sys.exit()

def input_func():
    sec=int(e.get())
    stopwatch_layout(sec)
    

stopwatch_label=Label(root,text='',font='Helvetica,24')        

        
              
input1=Button(root,text='Click to Enter the value and start',command=input_func,bg='black',fg='white')
input1.pack(pady=5)


stop=Button(root,text='Click to Stop',command=stop,bg='black',fg='white')
stop.pack(pady=5)

root.mainloop()
