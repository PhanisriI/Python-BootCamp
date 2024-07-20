"""
Find the element present in k+Nth index
"""
K=int(input())
N=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if (K+N)<len(arr):
        print(arr[K+N])
        break
    else:
        print("ERROR")
        break

    