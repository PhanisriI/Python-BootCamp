# replace the elements in an array with avg of maximum and minimum element
list1=list(map(int,input().split()))
minimum=list1[0]
maximum=0
for i in list1:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
avg=(maximum+minimum)//2
for i in range(len(list1)):
    list1[i]=avg
print(*list1)