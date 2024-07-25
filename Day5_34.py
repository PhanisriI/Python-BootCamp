#reverse the numbers present in an given string
n=input()
total=""
numbers="0123456789"
for i in n:
    if i in numbers:
        total+=(i)
# print(total[-1::-1])
total=int(total)
while(total!=0):
    print(total%10, end="")
    total//=10