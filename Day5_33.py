"""#remove all the brackets from the given algebraic expression
n=input()
no=[ord('{'),ord('}'),ord('['),ord(']'),ord('('),ord(')')]
for i in n:
    if ord(i) not in no:
        print(i,end="")

#2nd method using "pass"
n=input()
no=[ord('{'),ord('}'),ord('['),ord(']'),ord('('),ord(')')]
for i in n:
    if ord(i) in no:
        pass
    else:
        print(i,end="")

"""

