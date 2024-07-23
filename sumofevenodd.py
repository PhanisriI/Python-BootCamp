num=int(input())
Even_total=0
odd_total=0
while(num!=0):
    digit=num%10
    if digit%2==0:
        Even_total+=(digit**2)
    else:
        odd_total+=(digit**2)
    num//=10
print(f"even digits:{Even_total} and odd digits:{odd_total}")