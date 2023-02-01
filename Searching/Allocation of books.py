# Allocate N books to M students such that max no of pages alloted to any student should be min.

n = int(input())
a = list(map(int,input().split()))
m = int(input())

def func(mid):
    c = 1
    s = 0
    for i in range(n):
        if s+a[i]>mid:
            c+=1
            s = a[i]
        else:
            s+=a[i]
    if c<=m:
        return 1
    return 0

def BS(l,h):
    while l<=h:
        mid = (l+h)//2
        if not func(mid):
            l = mid+1
        else:
            if not func(mid-1):
                return mid
            else:
                h = mid-1

print(BS(max(a),sum(a)))