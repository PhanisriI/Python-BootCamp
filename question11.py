li1=list(map(int,input().split()))
minimum=li1[0]
for i in li1:
    if i<minimum:
        minimum=i
print(minimum)