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
from tkinter import * 
root = Tk() 
root.title('D.E.X.T.E.R') 
root.geometry("100x100")
menubar = Menu(root)

speak=Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Speak', menu =speak) 
speak.add_command(label ='click to start', command = None)
speak.add_separator()
speak.add_command(label ='Exit', command = root.destroy)


txt= Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Text', menu = txt)
txt.add_command(label ='Click to Enter Text', command = None)
txt.add_separator()
txt.add_command(label ='Exit', command = root.destroy)
txt.add_separator()
 
x=datetime.date.today()
date= Menu(menubar, tearoff = 0)

menubar.add_cascade(label=x, menu = date)



def get_audio():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("speak now .... ")
            audio=r.listen(source)
        try:
            print(".........",r.recognize_google(audio))
            t=r.recognize_google(audio).lower()
        except Exception:
            print("sorry didn't get that")
            text=input("Enter text : " )
            t=text.lower()

def exit():
        sys.exit()
##q,w=7,8
##while q<w:
##                
##        for i in ["hi",'hello','hey','sup']:
##            if i==t:
##                print('hello master')
##        
##        if t=='meme':
##                import memes
##        elif t=='memes':
##            import memes
##        elif ('show'and'memes') in t.split():
##            import memes
##        elif ("biology"and"facts") in t.split():
##            import bio
##        elif ("geography"and"facts") in t.split():
##            import geo
##        elif ("astronomy"and"facts") in t.split():
##            import astro
##        elif ("animal"and"facts") in t.split():
##            import animal
##        elif ("chemistry"and"facts")in t.split():
##            import chem
##        elif ("physics"and"facts") in t.split():
##            import physics
##        elif ("play" and "music") in t.split():
##            import mp3
##        elif ("play"and"song") in t.split():
##            import mp3
##        elif t=="sing a song for me":
##            import mp3
##        elif t=="sing a song":
##            import mp3
##        elif ("open"and"stopwatch")in t.split():
##            import stopwatch
##        elif('start'and"stopwatch") in t.split():
##            import stopwatch
##        elif (t=='stopwatch'):
##            import stopwatch
##        elif ('set'and'timer') in t.split():
##            import timer
##        elif ('start'and'timer')in t.split():
##            import timer
##        elif ('open'and'timer') in t.split():
##            import timer
##        elif t=='timer':
##            import timer
##        elif t == 'game':
##            import game
##        elif ('play'and"game") in t.split():
##            import game
##        
##        elif t=='bored' or ('bored'in t.split()):
##            what=input("Enter memes or game : ")
##            if what=='meme':
##                import memes
##            if what=='game':
##                import game
##        elif t=='word a day' or ('word a day'in t.split()):
##            import word
##        for i in cal: 
##            if i in t:
##                import calculator
##        if t not in["+","plus","add","addition","sum","-","subtract","minus","subtraction","difference",
##       "multiplication","times","*","product","multiply",
##       "/","ratio","division","divide",
##       "log","logarithm","antilog","antilogarithm","sin","sine","cos","cosine","tan","tangent",
##       "square","squareroot","cube","cuberoot","power",'timer','stopwatch','word a day','bored','i am bored'] :
##            try:
##                print(wikipedia.summary(t,sentences=2))
##            except Exception :
##                webbrowser.open_new_tab("https://www.google.com/search?q="+t)
##        choice=input("enter no or quit or bye to exit : " )
##        if choice=='no':
##            q,w=w,q
##        if choice=='quit':
##            q,w=w,q
##        if choice=='bye':
##            q,w=w,q
root.config(menu = menubar)
root.mainloop()        


    
        




        
