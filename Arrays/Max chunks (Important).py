# Find max chunks.

arr = list(map(int,input().split()))
cmax = 0
ans = 0
for i in range(len(arr)):
    cmax = max(cmax,arr[i])
    if cmax==i:
        ans+=1
print(ans)