#Sum of bitwise OR of all subarrays
arr = list(map(int,input().split()))
ans = 0
mask = (1<<31)
while mask:
    next = len(arr)
    for i in reversed(range(len(arr))):
        if (arr[i] & mask):
            next = i
        ans+=(len(arr)-next)*mask
    mask>>=1
print(ans)