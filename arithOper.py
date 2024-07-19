a=int(input())
b=int(input())
print(f"addition: {a+b},subtraction: {a-b} multiplication: {a*b} division: {a/b} modulus: {a%b}")
print(f"power: {a**b}")


"""
logical operators:
1.Logical AND
2.Logical OR

"""

age=int(input())
if age>=18 and age<24:
    print("Allowed to ride 2-wheeler")
elif age>=24 and age<45:
    print("Allowed to ride 2-wheeler and 4-wheeler")
elif age>=45 and age<=65:
    print("Allowed to ride 2 and 4 and 6 wheeler")
else:
    print("invalid input")



apple=15
banana=4
orange=5
X=int(input())
n_apples=int(input())
n_banana=int(input())
n_orange=int(input())
cost=(n_apples*apple)+(n_banana*banana)+(n_orange*orange)
if cost<=X:
    print("shopkeeper did not cheat")
else:
    print("shopkeeper cheated")


n=int(input())
if n>0:
    if n%2==0:
        print("positive even number")
    else:
        print("positive odd number")
elif n<0:
    if abs(n)%2==0:
        print("negative even number")
    else:
        print("negative odd number")
else:
    print("number neither even nor odd")


"""
mr.z is selected for olympics he is participating in swimming competition only one is selected from the participants.Mr x and mr y are
freinds of z.mr x is participating in badminton, mr y in table tennis. 

According to selection committe the requirement for badminton are 
height should be 140cm ,weight= factors of 2, bodyfat is less than 12%.

According to selection committe requirement for table tennis are height min 118cm to 148cms, weight= factors of number of medals
won by mr z , body fat 14%.

Acc to prev history mr z participated in 14 games outof he is having success rate of 50%.
WAP to check whether mr x, y, Z from india travell in a same plane or not?
"""
x_height=int(input())
x_weight=int(input())
x_fat=int(input())
y_height=int(input())
y_weight=int(input())
y_fat=int(input())
x=0
y=0
if x_height>=140 and x_weight%2==0 and x_fat<12:
    x=1
if y_height>=118 and y_height<=148 and y_weight%7==0 and y_fat<14:
    y=1
if x==1 and y==1:
    print("in same plane")
else:
    print("not in same plane")
