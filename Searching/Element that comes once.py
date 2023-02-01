# In an unsorted array, all elements occurs in pair, only one element occurs once. Find that unique element.

n = int(input())
a = list(map(int,input().split()))

def BS(l,h):
    while l<=h:
        m = (l+h)//2
        if m==0:
            if a[m]!=a[m+1]:
                return a[m]
            else:
                l = m+1
        elif m==n-1:
            if a[m]!=a[m-1]:
                return a[m]
            else:
                h = m-1
        elif a[m]!=a[m+1] and a[m]!=a[m-1]:
            return a[m]
        else:
            if a[m]==a[m+1]:
                f = m
            else:
                f = m-1
            if f%2==0:
                l = m+1
            else:
                h = m-1

print(BS(0,n-1))