#password verifier
"""
Mr x is trying to create a new password for his ig account. These are the required conditions for created a new password
1. Minimum length is 8 max length is 15
2. only @,/ is allowed in a password
3.No spaces are allowed
4.only alpha numerics are allowed
you are supposed to print weak if length is exact 8
median : length b/w 8 to 12
strong: length b/w 12 to 15
"""
word=input()
length=len(word)
verify=0
elements_possible='abcdefghijklmnopqrstuvwxyz@/0123456789'
con='@' or '/'
for i in word:
    if length>=8 and length<=15 and i!=' ':
        if i in con and (i in elements_possible):                      #membership operator "in" is used
              verify=1
if verify==1 and len(word)==8:
     print("weak password")
elif verify==1 and length>8 and length<12:
    print("median")
elif verify==1 and length>=12 and length<15:
     print("Strong")
else:
    print("Enter valid characters")
    
