num=int(input())
num1=num
digicount=0
while(num1>0):
    num1=num1//10
    digicount+=1
num1=num
total=0
while(num1>0):
    digit=num1%10
    total+=digit**digicount
    num1//=10
if total==num:
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not a armstrong number")