# Find the smallest good base K of int N such that K>=2 and all digits in N(k) must be 1 each.

n = int(input())
mn = 0
for i in reversed(range(1,64)):
    l = 2
    h = n-1
    while l<=h:
        m = (l+h)//2
        val = 0
        x = 1
        f = 0
        for j in range(i+1):
            val+=x
            if val>=n:
                break
            if j<i and (n-val)//x<m:
                f = 1
                break
            if j<i:
                x*=m
        if val>n or f==1:
            h = m-1
        elif val<n:
            l = m+1
        else:
            print(m)
            mn = 1
            break
    if mn == 1:
        break