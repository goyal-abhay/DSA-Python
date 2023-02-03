# Given a sorted array of size N containing distinct elements. Check if there exist a pair (i,j) such that A[i] + A[j]==K (i!=j)

A = list(map(int,input().split()))
k = int(input())
n = len(A)
i = 0
j = n-1
flag = 0
while i<j:
    if A[i]+A[j]==k:
        flag = 1
        break
    elif A[i]+A[j]<k:
        i+=1
    else:
        j-=1
if flag==1:
    print(True)
else:
    print(False)