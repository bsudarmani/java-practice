#countdown
import time
n = int(input("Enter a number:"))

for i in range(n,0,-1):
    print(i)
    time.sleep(1)
