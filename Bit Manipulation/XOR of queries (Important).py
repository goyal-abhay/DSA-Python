# XOR of all elements for query[i,j] such that A[i]^A[i+1]^...^A[j-1]^A[j] (i<=j)

arr = list(map(int,input().split()))
q = int(input())
pxor = [0]*len(arr)
pxor[0] = arr[0]
for x in range(len(arr)):
    pxor[x] = pxor[x-1]^arr[x]
for _ in range(q):
    i,j = map(int,input().split())
    if i==0:
        print(pxor[j])
    else:
        print(pxor[j]^pxor[i-1])
    