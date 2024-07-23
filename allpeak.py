a=list(map(int,input().split()))
count=0
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        #print(a[i],end=' ')
        count=i
if a[-1]>a[-2] and a[-1]>count:
        count=len(a)-1
print(a[count])

"""
a=list(map(int,input().split()))
count=0
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        print(a[i],end=' ')01
"""