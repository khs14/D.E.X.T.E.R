import time
import sys
i=0
print("enter crtl + c to end ")
ask=input("Enter 0 to start : ")
if ask=='0':
    while True:
        print(i)
        i+=1
        time.sleep(1)


