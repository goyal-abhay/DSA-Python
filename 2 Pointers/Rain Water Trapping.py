#Given an array of size n, where A[i] represents the height of the ith wall. Pick any 2 walls such that max water can be stored b/w them.

A = list(map(int,input().split()))
n = len(A)
ans = 0
i = 0
j = n-1
while i!=j:
    if A[i]>=A[j]:
        w = (j-i)*A[j]
        j-=1
    else:
        w = (j-i)*A[i]
        i+=1
    ans = max(ans,w)
print(ans)