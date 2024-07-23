array=list(map(int,input().split()))
num=array[0]
for i in range(1,len(array)-1):
    if array[i]>array[i-1] and array[i]>array[i+1] and array[i]>=num:
        num=array[i]
    
    if num<array[len(array)-1]:
        num=array[len(array)-1]
        break
print(num)