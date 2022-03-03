print("""HELLO  USER!!------
I am your Mr.Calculator
I have the following features which work on speech recognition or text string input:
1. I can perform single operations like division,multiplication,addition,subtraction
2. I can calculate any float power of a given number
3. I can calculate values of trigonomertic functions like sin, cos ,tan etc.
4. I can also calculate log and antilog of a given number
So Let's Start!!!""")
speech_input=str(input("Enter a simple mathematical calculation: "))       #str(input("what do you want to add: "))
l=["+","plus","add","addition","sum",
   "-","subtract","minus","subtraction","difference",
   "multiplication","times","*","product","multiply",
   "/","ratio","division","divide",
   "log","logarithm","antilog","antilogarithm","sin","sine","cos","cosine","tan","tangent",
   "square","squareroot","cube","cuberoot","power"]

l2=t
import math
for i in l2:
    if i in l:
        if i=="+" or i=="plus":                                                      # Eg. "197 + 214" 
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j-1])
                    num2=num1+float(l2[j+1])
                    print("It's",num2)
        elif i=="sum" or i=="addition":                                          # Eg. "wHaT iS the SuM OF 197 and 214"
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+2])
                    num2=num1+float(l2[j+4])
                    print("It's",num2)
        elif i=="add":                                                                   # Eg. " HoW will YOU ADd 9999 and 013392
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+1])
                    num2=num1+float(l2[j+3])
                    print("It's",num2)
        elif i=="subtract":                                                            #Eg. subtract 19 from 31
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+1])
                    num2=float(l2[j+3])-num1
                    print("It's",num2)
        elif i=="difference" or i=="subtraction":                               #Eg. what is the difference between 8 and 19
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+2])
                    num2=float(l2[j+4])-num1
                    print("It's",num2)
        elif i=="-":                                                                        #Eg. what is 12 - 8
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+1])
                    num2=float(l2[j-1])-num1
                    print("It's",num2)
        elif i=="minus":                                                          #Eg. 12 minus 8
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+1])
                    num2=float(l2[j-1])-num1
                    print("It's",num2)
        elif i=="mutiply":                                                      #Eg. Multiply 18 and 12
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+1])
                    num2=float(l2[j+3])*num1
                    print("It's",num2)
        elif i=="times" or i=="*":                                            #Eg. what is 11 times 12
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j-1])
                    num2=float(l2[j+1])*num1
                    print("It's",num2)
        elif i=="product" or i=="multiplication":                    #Eg. what is the product of 3 and 9
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+2])
                    num2=float(l2[j+4])*num1
                    print("It's",num2)
        elif i=="ratio" or i=="division":                                #Eg. find the ratio of 8 and 4
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+4])
                    num2=float(l2[j+2])/num1
                    print("It's",num2)
        elif i=="divide":                                                  #Eg. divide 12 by 3
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+3])
                    num2=float(l2[j+1])/num1
                    print("It's",num2)
        elif i=="/":                                                       #Eg. 12 / 4
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+1])
                    num2=float(l2[j-1])/num1
                    print("It's",num2)
        elif i=="square":                                                         #Eg. square root of 100
            for j in range(0,len(l2)):
                if(l2[j]==i and l2[j+1]=="root"):
                    print("It's",round(math.sqrt(float(l2[j+3])),4))
                    break
                elif l2[j+1]=="of":                                                 #Eg. square of 10
                    print("It's",round(float(l2[j+2])**2,4))
                    break
        elif i=="squareroot":                                                      #Eg. square root of 100
             for j in range(0,len(l2)):
                  if l2[j]==i :
                    print("It's",round(math.sqrt(float(l2[j+2])),4))
                    break
        elif i=="cube":                                                              #cube root of 27
            for j in range(0,len(l2)):
                if(l2[j]==i and l2[j+1]=="root"):
                    print("It's",round(float(l2[j+3])**(1/3),4))
                    break
                elif l2[j+1]=="of":                                                  #Eg. cube of 10
                    print("It's",round(float(l2[j+2])**3,4))
                    break
        elif i=="cuberoot":                                                        #Eg. square root of 100
             for j in range(0,len(l2)):
                  if l2[j]==i :
                    print("It's",round(float(l2[j+2])**(1/3),4))
                    break
        elif i=="power":                                                             #Eg. 5 raised to the power 3 
             for j in range(0,len(l2)):
                 if (l2[j]==i and l2[j-3]=="raised"):
                     print("It's", round(float(l2[j-4])**float(l2[j+1]),4))
                     break
                 elif(l2[j]==i and l2[j-3]!="raised"):                              #Eg. 3 to the power 2
                     print("It's", round(float(l2[j-3])**float(l2[j+1]),4))
                     break
        elif (i=="sin"or i=="sine"):
             for j in range(0,len(l2)):                                               #Eg. sine of 5
                 if (l2[j]==i and l2[j+1]=="of"):
                     print("It's",round(math.sin(float(l2[j+2])),4),"where the angle is measured in radians.")
                 elif(l2[j]==i and l2[j+1]!="of"):                                   #Eg. sine 5
                     print("It's",round(math.sin(float(l2[j+1])),4),"where the angle is measured in radians.")
        elif (i=="cosine"or i=="cos"):
             for j in range(0,len(l2)):                                               #Eg. cosine of 5
                 if (l2[j]==i and l2[j+1]=="of"):
                     print("It's",round(math.cos(float(l2[j+2])),4),"where the angle is measured in radians.")
                 elif(l2[j]==i and l2[j+1]!="of"):                                   #Eg. cosine 5
                     print("It's",round(math.cos(float(l2[j+1])),4),"where the angle is measured in radians.")
        elif (i=="tan"or i=="tangent"):
             for j in range(0,len(l2)):                                               #Eg. tan of 5
                 if (l2[j]==i and l2[j+1]=="of"):
                     print("It's",round(math.tan(float(l2[j+2])),4),"where the angle is measured in radians.")
                 elif(l2[j]==i and l2[j+1]!="of"):                                   #Eg. tan 5
                     print("It's",round(math.tan(float(l2[j+1])),4),"where the angle is measured in radians.")
        elif (i=="log" or i=="logarithm"):                                       #Eg. what is log 100
             for j in range(0,len(l2)):
                if (l2[j]==i and l2[j+1]=="of"):                                    # log of 100 
                     print("It's",round(math.log10(float(l2[j+2])),4))
                     break
                else:                                                                      #log 100 
                     print("It's",round(math.log10(float(l2[j+1])),4))
                     break
        elif (i=="antilog" or i=="antilogarithm"):                              #antilog of 2
             for j in range(0,len(l2)):
                if (l2[j]==i and l2[j+1]=="of"):
                    print("It's",10**float(l2[j+2]))
                    break
                else:                                                                      #antilog 2
                    print("It's",10**float(l2[j+1]))

