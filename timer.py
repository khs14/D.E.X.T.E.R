import time
import sys
hr=int(input("Enter number of Hours : "))
m=int(input("Enter number of Mitnutes : "))
s=int(input("Enter number of Seconds : "))
seconds=(hr*3600)+(m*60)+s
for i in range(seconds):
    print(seconds-i," seconds left")
    time.sleep(1)
print("time up")
try:
    sys.exit()
except:
    print('exited')

