import random
toss=input("Enter batting or bowling : ")
runsc=0
a,b=1,2
c,d=3,4
if toss=="batting":
    runs=0
    while a<b:
        run=int(input("Enter run b/w 0 and 11 : "))
        while run>10 or run<0:
            run=int(input("Enter run b/w 0 and 11 : "))    
        x=random.randint(1,10)
        print("you entered ",run)
        print("comp entered ",x)
        runs+=run
        print("total till now",runs)
        if run==x:
            print("you are out ")
            print("runs made ",runs-x)
            a,b=2,1
            print("your turn to bowl")
    while c<d:
         bowl=int(input("Enter run b/w 0 and 11 : "))
         y=random.randint(1,10)
         runsc+=y
         print("you entered ",bowl)
         print("comp entered ",y)
         print("total till now",runsc)
         if bowl==y:
             print("comp is out ")
             print("runs made by comp ",runsc-y)
             if runsc<runs:
                 print("you won")
                 c,d=4,3
         elif runsc>=(runs-x):
             c,d=4,3
             print("you lost")
e,f=1,2
g,h=3,4
if toss=="bowling":
    runsu=0
    runscb=0
    while e<f:
        bowling=int(input("Enter run b/w 0 and 11 : "))
        k=random.randint(1,10)
        print("you entered ",bowling)
        print("comp entered ",k)
        runscb+=k
        print("total till now",runscb)
        if bowling==k:
            print("comp is out ")
            print("runs made ",runscb-bowling)
            e,f=2,1
            print("your turn to bat")
    while g<h:
        bat=int(input("Enter run b/w 0 and 11 : "))
        while bat>10 or bat<0:
            bat=int(input("Enter run b/w 0 and 11 : ")) 
        v=random.randint(1,10)
        runsu+=bat
        print("you entered ",bat)
        print("comp entered ",v)
        print("total till now",runsu)
        if bat==v:
            print("you are out ")
            print("runs made by you ",runsu-v)
            g,h=h,g
            if runscb>runsu:
                print("you lost")
        elif runsu>=runscb:
            g,h=4,3
            print("you won")







    
            
