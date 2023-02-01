# Given height of N pillars. Find total height of rainfall trapped.

arr = list(map(int,input().split()))

n = len(arr)
pmax = [0]*n
pmax[0] = arr[0]
for i in range(1,n):
    pmax[i] = max(pmax[i-1],arr[i])

smax = [0]*n
smax[n-1] = arr[n-1]
for i in reversed(range(n-1)):
    smax[i] = max(smax[i+1],arr[i])

ans = 0
for i in range(1,n):
    h1 = pmax[i]
    h2 = smax[i]
    h = arr[i]
    dh = min(h1,h2)
    if dh>h:
        ans+=(dh-h)

print(ans)
