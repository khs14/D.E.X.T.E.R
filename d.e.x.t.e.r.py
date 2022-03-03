import wikipedia
import math
import random
import webbrowser
import speech_recognition as sr
import sys
import cv2
import numpy as np
import pyttsx3
import datetime


cal=["+","plus","add","addition","sum",
   "-","subtract","minus","subtraction","difference",
   "multiplication","times","*","product","multiply",
   "/","ratio","division","divide",
   "log","logarithm","antilog","antilogarithm","sin","sine","cos","cosine","tan","tangent",
   "square","squareroot","cube","cuberoot","power"]

dexter_func=['timer','stopwatch','word a day','bored','i am bored',"hi",'hello','hey','sup']

def txt_to_speech(Text):
    speaker = pyttsx3.init()
    speaker.say(Text)
    speaker.runAndWait()



def known(t):
        for i in ["hi",'hello','hey','sup']:
            if i==t:
                txt_to_speech("Hello Master")
                messagebox.showinfo(title='Greetings', message="Hello master")
        if t=='meme':
                import memes
        elif t=='memes':
            import memes
        elif ('show'and'memes') in t.split():
            import memes
        elif ("biology"and"facts") in t.split():
            import bio
        elif ("geography"and"facts") in t.split():
            import geo
        elif ("astronomy"and"facts") in t.split():
            import astro
        elif ("animal"and"facts") in t.split():
            import animal
        elif ("chemistry"and"facts")in t.split():
            import chem
        elif ("physics"and"facts") in t.split():
            import physics
        elif ("play" and "music") in t.split():
            import mp3
        elif ("play"and"song") in t.split():
            import mp3
        elif t=="sing a song for me":
            import mp3
        elif t=="sing a song":
            import mp3
        elif ("open"and"stopwatch")in t.split():
            import stopwatch
        elif('start'and"stopwatch") in t.split():
            import stopwatch
        elif (t=='stopwatch'):
            import stopwatch
        elif ('set'and'timer') in t.split():
            import timer
        elif ('start'and'timer')in t.split():
            import timer
        elif ('open'and'timer') in t.split():
            import timer
        elif t=='timer':
            import timer
        elif t == 'game':
            import game
        elif ('play'and"game") in t.split():
            import game
        elif t=='open youtube':
                webbrowser.open_new_tab("https://www.youtube.com/")
        elif t=='open gmail':
                webbrowser.open_new_tab("https://mail.google.com/mail/")
        elif t=='open linkedin':
                webbrowser.open_new_tab("https://www.linkedin.com/") 
        
        elif t=='bored' or ('bored'in t.split()):
            what=input("Enter memes or game : ")
            if what=='meme':
                import memes
            if what=='game':
                import game
        elif t=='word a day' or ('word a day'in t.split()):
            import word
        for i in cal: 
            if i in t:
                import calculator

def unknown(t):
        try:
                print(wikipedia.summary(t,sentences=2))
        except Exception :
                webbrowser.open_new_tab("https://www.google.com/search?q="+t)
        




def get_audio():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("speak now .... ")
            audio=r.listen(source)
        try:
            print(".........",r.recognize_google(audio))
            search=r.recognize_google(audio).lower()
            known(search)
        except Exception:
            messagebox.showerror(title='Error', message="Speech Recognition not working please try the text method.Sorry for the Inconvenience")

def get_text():
        l1=Label(root,text="Please Enter the Search",fg='Black')
        l1.pack(pady=10)
        e=Entry(root,fg='blue')
        e.pack(pady=5)
        def text():
            e.pack(pady=5)
            t=e.get()
            search = t.lower()
            known(search)
        button=Button(root,text='Click to Enter the search',command=text,bg='black',fg='white')
        button.pack(pady=5)
        

import tkinter
from tkinter import messagebox
from tkinter import * 
root = Tk() 
root.title('D.E.X.T.E.R') 
root.geometry("500x500")


menubar = Menu(root)

from PIL import ImageTk,Image 
i=ImageTk.PhotoImage(Image.open(r'dexterlogo.jpg'))
l=Label(image=i)
l.pack()


speak=Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Speak', menu =speak) 
speak.add_command(label ='click to start', command = get_audio)
speak.add_separator()
speak.add_command(label ='Exit', command = root.destroy)


txt= Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Text', menu = txt)
txt.add_command(label ='Click to Enter Text', command = get_text)
txt.add_separator()
txt.add_command(label ='Exit', command = root.destroy)
txt.add_separator()


x=datetime.date.today()
date= Menu(menubar, tearoff = 0)

menubar.add_cascade(label=x, menu = date)
def exit():
        sys.exit()


root.config(menu = menubar)
root.mainloop()        


    
        




        
