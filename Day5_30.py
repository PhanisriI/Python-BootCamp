"""
n=input()
total=0
for i in n:
    if i.isnumeric():
        total+=int(i)
print(total)

#without built in functions
n=input()
total=0
numbers="0123456789"
for i in n:
    if i in numbers:
        total+=int(i)
print(total)

#find the element is a number or not using ascII values
n=input()
total=0
for i in n:
    if ord(i)>=48 and ord(i)<=57:
        total+=int(i)
print(total)

#WAP to print all the capital letter in a given string
n=input()
final=""
for i in n:
    if ord(i)>=65 and ord(i)<=90:
        final+=i
print(final)
"""
