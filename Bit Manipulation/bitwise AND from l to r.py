# Find bitwise AND of all numbers from l to r.

l,r = map(int,input().split())

mask = (1<<31)
ans = 0
while (mask):
    if ((mask & l) == (mask & r)):
        if (mask & l):
            ans+=mask
        mask>>=1
    else:
        break

print(ans)