n=input()
h=n.count('-')
a=""
print("-"*h,end="")
for i in n:
    if i=='-':
        a+=i
    else:
        print(i,end="")
