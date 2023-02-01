# Check if A[i]^A[j]==k exist in an array.

arr = list(map(int,input().split()))
k = int(input())
c=0
arr.sort()
for i in range(len(arr)):
    a = k^arr[i]
    if a in arr:
        c = a
        break
if c:
    print("Yes")
else:
    print('No')