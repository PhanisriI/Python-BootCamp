"""
question 7.1:
you are given a comma seperated natural numbers 1 to 10 
print even numbers
"""
my_list=list(map(int,input().split(",")))
print(my_list[1:len(my_list):2]) 


#this problem can also be solved by using for-loop
li1=list(map(int,input().split()))
for i in range(1,len(li1),2):
    print(li1[i],end=" ")



"""question 7.2:
take list of elemnets
print alternate numbers
"""

li1=list(map(int,input().split()))
print(li1[0:len(li1):2])



"""
question 7.2:
you are given a space seperated integer list
find number of even and odd elements in the list
"""
my_list=list(map(int,input().split()))
even_count=0
odd_count=0
for i in my_list:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"there are {even_count} even numbers and {odd_count} odd numbers")
