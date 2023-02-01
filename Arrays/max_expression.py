# Given an array and 3 intergers p,q,r. Maximize (p*a[i] + q*a[j] + r*a[k]) [i<j<k]

arr = list(map(int,input().split()))
p,q,r = map(int,input().split())

n = len(arr)
ans = min(arr)

pmax = [0]*n
pmax[0] = p*arr[0]
for i in range(1,n):
    pmax[i] = max(pmax[i-1],p*arr[i])

smax = [0]*n
smax[n-1] = r*arr[n-1]
for i in reversed(range(n-1)):
    smax[i] = max(smax[i+1],r*arr[i])

for i in range(1,n-1):
    ans = max(ans, pmax[i-1] + q*arr[i] + smax[i+1])

print(ans)