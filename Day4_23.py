"""year=int(input())

if year%400==0:
    print("leap year")
else:
    print("not leap year")"""

s_year=int(input())
e_year=int(input())
for i in range(s_year,e_year):
    if i%400==0 or (i%4==0 and (i%100)!=0):
        print(i)


