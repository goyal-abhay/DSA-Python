# Place C cows at N stalls such that min distance b/w 2 adjacent cows is max. (1 slot can have max 1 cow)

n = int(input())
a = list(map(int,input().split()))
c = int(input())

def func(m):
    cnt = 1
    pre = a[0]
    for i in range(1,n):
        if a[i]-pre<m:
            continue
        else:
            cnt+=1
            pre = a[i]
    if cnt>=c:
        return 1
    return 0

def BS(l,h):
    while l<=h:
        m = (l+h)//2
        if not func(m):
            h = m-1
        else:
            if not func(m+1):
                return m
            else:
                l = m+1

print(BS(min(a),max(a)))