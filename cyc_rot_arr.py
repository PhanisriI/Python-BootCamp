#CYCLIC ROTATION ARRAY
"""
print the element at a particular index"""

K=int(input())
arr=list(map(int,input().split()))
n=len(arr)
p=K%n
print(arr[p])