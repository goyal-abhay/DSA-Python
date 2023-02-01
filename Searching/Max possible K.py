# Given an unsorted array of positive integers and int x (x>=0). Find max possible k such that none of the subarrays of size k has a sum>x.

n = int(input())
a = list(map(int,input().split()))
x = int(input())

def isPoss(m):
    if m==n+1:
        return 0
    sm = 0
    for i in range(m):
        sm+=a[i]
    if sm>x:
        return 0
    else:
        for i in range(m,n):
            sm+=a[i]
            sm-=a[i-m]
            if sm>x:
                return 0
    return 1

def BS(l,h):
    while l<=h:
        m = (l+h)//2
        if not isPoss(m):
            h = m-1
        else:
            if not isPoss(m+1):
                return m
            else:
                l = m+1

print(BS(0,n))