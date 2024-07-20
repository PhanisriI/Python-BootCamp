#sum of digits

num=int(input())
sum=0
while(num>0):
    r=num%10
    sum=sum+r
    num=num//10
print(sum)
