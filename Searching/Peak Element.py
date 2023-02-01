# Find the peak element in unsorted array.

n = int(input())
a = list(map(int,input().split()))

def BS(l,h):
    while l<=h:
        m = (l+h)//2
        if m==0 and a[m]>a[m+1]:
            return a[m]
        elif m==n-1 and a[m]>a[m-1]:
            return a[m]
        else:
            if a[m]>a[m+1] and a[m]>a[m-1]:
                return a[m]
            elif a[m]<a[m+1]:
                l = m+1
            else:
                h = m-1

print(BS(0,n-1))