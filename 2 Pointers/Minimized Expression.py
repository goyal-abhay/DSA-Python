# Given 3 sorted arrays of sizes N. Find i,j,k such that max(A[i],B[j],C[k])-min(A[i],B[j],C[k]) should be minimized.

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
n = len(A)
i,j,k = 0,0,0
ans = 10**9
while i<n and j<n and k<n:
    m1 = max(A[i],B[j],C[k])
    m2 = min(A[i],B[j],C[k])
    ans = min(ans,m1-m2)
    if m2==A[i]:
        i+=1
    elif m2==B[j]:
        j+=1
    else:
        k+=1
print(ans)