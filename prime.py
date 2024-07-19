"""
num=int(input())
count=0
for i in range(2,num//2):
    if num%i==0:
        count+=1
        break
if count==1:
    print("Not a prime number")
else:
    print("Is a prime number")
"""
#square root method 
import math
num=int(input())
r=int(math.sqrt(num))
count=0
for i in range(2,r+1):
    if num%i==0:
        count+=1
        break
if count==1:
    print("Not a prime number")
else:
    print("Is a prime number")