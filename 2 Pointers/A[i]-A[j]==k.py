# Given a sorted array of size N containing distinct elements. Check if there exist a pair (i,j) such that A[j] - A[i]==K (K>0)

A = list(map(int,input().split()))
k = int(input())
n = len(A)
flag = 0
i = 0
j = 1
while j<n:
    if A[j]-A[i]==k:
        flag = 1
        break
    elif A[j]-A[i]>k:
        i+=1
        if i==j:
            j+=1
    else:
        j+=1
if flag==1:
    print(True)
else:
    print(False)