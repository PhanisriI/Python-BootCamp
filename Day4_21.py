"""
a,b=map(int,input().split())
if a>b:
    if a%b==0:
        Gcd=b
        lcd=a
        
    else:
        Gcd=1
        lcd=a*b
        
else:
    if b%a==0:
        Gcd=a
        lcd=b
        
    else:
        Gcd=1
        lcd=a*b
print(f"gcd={Gcd} and lcd={lcd}")
"""

a,b=map(int,input().split())
tem1,tem2=a,b
while(b!=0):
    a,b=b,a%b
print("gcd=",a)
print("lcm=",(tem1*tem2)//a)

