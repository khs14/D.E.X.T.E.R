print("""HELLO  USER!!------
I am your Mr.Calculator
I have the following features which work on speech recognition or text string input:
1. I can perform single operations like division,multiplication,addition,subtraction
2. I can calculate any float power of a given number
3. I can calculate values of trigonomertic functions like sin, cos ,tan etc.
4. I can also calculate log and antilog of a given number
So Let's Start!!!""")
speech_input=str(input("Enter a simple mathematical calculation: "))       
l=["+","plus","add","addition","sum",
   "-","subtract","minus","subtraction","difference",
   "multiplication","times","*","product","multiply",
   "/","ratio","division","divide",
   "log","logarithm","antilog","antilogarithm","sin","sine","cos","cosine","tan","tangent",
   "square","squareroot","cube","cuberoot","power"]
speech_input=speech_input.lower()
l2=speech_input.split()
import math
for i in l2:
    if i in l:
        if i=="+" or i=="plus":                                                       
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j-1])
                    num2=num1+float(l2[j+1])
                    print("It's",num2)
        elif i=="sum" or i=="addition":                                         
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+2])
                    num2=num1+float(l2[j+4])
                    print("It's",num2)
        elif i=="add":                                                                  
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+1])
                    num2=num1+float(l2[j+3])
                    print("It's",num2)
        elif i=="subtract":                                                           
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+1])
                    num2=float(l2[j+3])-num1
                    print("It's",num2)
        elif i=="difference" or i=="subtraction":                              
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+2])
                    num2=float(l2[j+4])-num1
                    print("It's",num2)
        elif i=="-":                                                                        
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+1])
                    num2=float(l2[j-1])-num1
                    print("It's",num2)
        elif i=="minus":                                                         
            for j in range(0,len(l2)):
                if l2[j]==i:
                    pos=j
                    num1=float(l2[j+1])
                    num2=float(l2[j-1])-num1
                    print("It's",num2)
        elif i=="mutiply":                                                      
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
        elif i=="cube":                                                              
            for j in range(0,len(l2)):
                if(l2[j]==i and l2[j+1]=="root"):
                    print("It's",round(float(l2[j+3])**(1/3),4))
                    break
                elif l2[j+1]=="of":                                                  
                    print("It's",round(float(l2[j+2])**3,4))
                    break
        elif i=="cuberoot":                                                        
             for j in range(0,len(l2)):
                  if l2[j]==i :
                    print("It's",round(float(l2[j+2])**(1/3),4))
                    break
        elif i=="power":                                                              
             for j in range(0,len(l2)):
                 if (l2[j]==i and l2[j-3]=="raised"):
                     print("It's", round(float(l2[j-4])**float(l2[j+1]),4))
                     break
                 elif(l2[j]==i and l2[j-3]!="raised"):                              
                     print("It's", round(float(l2[j-3])**float(l2[j+1]),4))
                     break
        elif (i=="sin"or i=="sine"):
             for j in range(0,len(l2)):                                               
                 if (l2[j]==i and l2[j+1]=="of"):
                     print("It's",round(math.sin(float(l2[j+2])),4),"where the angle is measured in radians.")
                 elif(l2[j]==i and l2[j+1]!="of"):                                   
                     print("It's",round(math.sin(float(l2[j+1])),4),"where the angle is measured in radians.")
        elif (i=="cosine"or i=="cos"):
             for j in range(0,len(l2)):                                               
                 if (l2[j]==i and l2[j+1]=="of"):
                     print("It's",round(math.cos(float(l2[j+2])),4),"where the angle is measured in radians.")
                 elif(l2[j]==i and l2[j+1]!="of"):                                   
                     print("It's",round(math.cos(float(l2[j+1])),4),"where the angle is measured in radians.")
        elif (i=="tan"or i=="tangent"):
             for j in range(0,len(l2)):                                              
                 if (l2[j]==i and l2[j+1]=="of"):
                     print("It's",round(math.tan(float(l2[j+2])),4),"where the angle is measured in radians.")
                 elif(l2[j]==i and l2[j+1]!="of"):                                  
                     print("It's",round(math.tan(float(l2[j+1])),4),"where the angle is measured in radians.")
        elif (i=="log" or i=="logarithm"):                                       
             for j in range(0,len(l2)):
                if (l2[j]==i and l2[j+1]=="of"):                                    
                     print("It's",round(math.log10(float(l2[j+2])),4))
                     break
                else:                                                                  
                     print("It's",round(math.log10(float(l2[j+1])),4))
                     break
        elif (i=="antilog" or i=="antilogarithm"):                              
             for j in range(0,len(l2)):
                if (l2[j]==i and l2[j+1]=="of"):
                    print("It's",10**float(l2[j+2]))
                    break
                else:                                                                      
                    print("It's",10**float(l2[j+1]))







