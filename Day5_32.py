n=int(input())
for i in range(n):
    for j in range(n):
        if i==j:
            print(" ",end="")
        else:
            print("*",end="")
    print()
#print upper triangular matrix
#print lower triangular matrix
#print parallelogram and rhombus
#print number pyramid
"""
   1
  121
 12321
1234321
"""