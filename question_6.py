"""
question 6:
take space seperated input from the user and print alternate elemnts

"""

my_list=list(map(int,input().split()))
for i in range(0,len(my_list),2):
    print(my_list[i],end=" ")