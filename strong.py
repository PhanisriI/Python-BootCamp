num=int(input())
n=num
total=0
while(n>0):
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    total+=fact
    n//=10
if total==num:
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")
