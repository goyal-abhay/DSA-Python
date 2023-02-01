# Binary Search-

n = int(input())
a = list(map(int,input().split()))
k = int(input())

def BS(l,h):
    while l<=h:
        m = (l+h)//2
        if a[m]==k:
            return m
        elif a[m]>k:
            h = m-1
        else:
            l = m+1

print(BS(0,n-1))