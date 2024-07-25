#print the non repeating or unique charactwers in a string 
n=input()
es=""
for i in n:
    if n.count(i)==1 and i.isalpha():  # use isalpha() to remove the space
        es=es+i
print(es)

for i in n:
    if i not in es and i.isalpha():  # use isalpha() to remove the space
        es=es+i
print(es)
