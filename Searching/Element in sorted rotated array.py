# Find index of k in sorted rotated array

n = int(input())
a = list(map(int,input().split()))
k = int(input())

def BS(l,h):
    while l<=h:
        m = (l+h)//2
        if a[m]<=a[n-1]:
            h = m-1
        else:
            if a[m]>a[m+1]:
                return m
            else:
                l = m+1

x = BS(0,n-1)
if k<=a[n-1]:
    print(BS(x+1,n-1))
else:
    print(BS(0,x))