#string methods can only used for specific tym can change the string completely using these methods
"""
1.isAlpha
isDigit
isAlum
isUpper
isLower
converting to :

lower
upper
swapcase
title- returns the word with changing the first letter to capital
captalize - returns the word with first letter capital and remaing all are small letters
replace(char,char)
split() - splits the word based on space
split(char)- taking the passed character as base and splits the words into parts by removing the character
strip - starting and ending extra spaces are removed
""" 
word=input()

print(word.isalpha())
print(word.isalnum())
print(word.isdigit())
print(word.isupper())
print(word.islower())
print(word.isnumeric())
print(word.istitle())
print(word.isascii())

print(word.capitalize())
print(word.lower())
print(word.upper())
print(word.title())
print(word.swapcase())
print(word.split())
print(word.split('i'))
print(word.replace('h','H'))
print(word.strip())


