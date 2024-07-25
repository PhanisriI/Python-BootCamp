"""
Capital letters A-Z : 65-90
small letters a-z :   97-122
numbers 0-9 :         48-57
ascii value for space:     32
special characters:  91-96 and 123-127
"""
"""
methods:
1.ord()
2.chr()

"""

print(ord(' '))
print(ord('9'))
print(chr(91+1))

for i in range(32,128):
    print(chr(i),end=" ") # main characters starts from range 32 