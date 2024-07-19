"""
int 
float
string
boolean 
sets 
list    
tuple   
dict 
"""
print("Hello World")
print("SWEC")

"""
printing formats
1.usng print stmt by predefined variables
2.using print by taking input
3.using fstring
"""

var1="python" #type-1
print("Good morning",var1)

var2=input("enter your name")  #type-2
print("good morning",var2)

var3=input("enter your name \n")  #type-2
print("good morning",var3)

name=input("enter your name")
age=int(input())
print(f"Hello {name}, you are {age} years old")

userName=input("Enter the name")
sub1,sub2,sub3,sub4,sub5=map(int,input().split())
avg=(sub1+sub2+sub3+sub4+sub5)/5
print(f"Hi {userName}, your marks average is {avg}")


"""
String can be type casted into different datatypes like "list,tuple,int,float"
(end="") used for formating the print statement 
"""
name=input("Enter your name")
age = int(input())
if age>=18:
    print(f"{name}, you are ellgible to vote! :)")
else:
    print(f"{name}, you are not elligble to vote :(")
 