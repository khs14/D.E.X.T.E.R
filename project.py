import speech_recognition as sr
t=''
#a=1
#b=2
#while a<b:
r=sr.Recognizer()
with sr.Microphone() as source:
    print("speak now .... ")
    audio=r.listen(source)
try:
    print(".........",r.recognize_google(audio))
    t=r.recognize_google(audio).lower()
except Exception:
    print("sorry didn't get that")
    t=input("Enter text : " )
    t=t.lower()
print(t)
    
