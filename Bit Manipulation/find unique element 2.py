# Every element appears thrice. Just one element comes once. Find unique element.

arr = list(map(int,input().split()))
mask = (1<<31)
ans = 0
while mask:
    ct = 0
    for i in range(len(arr)):
        if (mask & arr[i]):
            ct+=1
    if ct%3!=0:
        ans+=mask
    mask>>=1
print(ans)