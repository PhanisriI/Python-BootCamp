"""#print all the vowesl follwed by consonants
n=input()
j=['a', 'e', 'i' ,'o' ,'u']
count=0
for i in n.lower():
    if  i in j:
        print(i,end="")
for k in n.lower():
    if  (k not in j) and (k.isalpha()) :
        print(k,end="")
        """
