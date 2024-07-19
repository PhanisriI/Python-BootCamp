"""
given a space seperated interger list
find the avg of elements present in even index
"""
li1=list(map(int,input().split()))
count=0
total=0
for i in range(0,len(li1)):
    if i%2==0:
        count+=1
        total=total+li1[i]
print(total/count)

"""
hw:
1. WAP to find area of circle
2. WAP to perimeter of perimeter of circle
3. WAP to find area of a triangle
4. WAP to find perimeter of triangle
"""