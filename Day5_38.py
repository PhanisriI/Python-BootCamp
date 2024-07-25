# check number of variables
n=input()
j=['a', 'e', 'i' ,'o' ,'u']
count=0
for i in n.lower():
    if  i in j:
        count+=1
print(count)




