# WAP to print the consonants count
#1st method
n=input()
j=['a', 'e', 'i' ,'o' ,'u']
count=0
for i in n.lower():
    if  (i not in j) and (i.isalpha()) :
        count+=1
print(count)
 
#2nd method
n=input()
s="bcdfghjklmnpqrstvwxyz"
count=0
for i in n.lower():
    if  i in s:
        count+=1
print(count)