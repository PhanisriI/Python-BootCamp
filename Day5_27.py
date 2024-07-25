n=input()
skip=int(input())
for i in n:
    if ord(i)>=65 and ord(i)<=90:
        x=65+(((ord(i)-65)+skip)%26)
        print((chr(x)),end="")
    elif ord(i)>=97 and ord(i)<=122:
        x=97+(((ord(i)-97)+skip)%26)
        print((chr(x)),end="")
