#find the max element of a given given list
li1=list(map(int,input().split()))
maximum=0
for i in li1:
    if i>maximum:
        maximum=i
print(maximum)