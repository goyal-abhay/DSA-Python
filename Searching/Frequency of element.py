# Given a sorted array which may contain duplicates. Find the frequency of the given element using first and last occurence.

n = int(input())
a = list(map(int,input().split()))
k = int(input())

def FO(l,h):
    while l<=h:
        m = (l+h)//2
        if a[m]<k:
            l = m+1
        elif a[m]>k:
            h = m-1
        else:
            if m==0:
                return m
            elif a[m-1]!=k:
                return m
            else:
                h = m-1

def LO(l,h):
    while l<=h:
        m = (l+h)//2
        if a[m]<k:
            l = m+1
        elif a[m]>k:
            h = m-1
        else:
            if m==n-1:
                return m
            elif a[m+1]!=k:
                return m
            else:
                l = m+1


x = FO(0,n-1)
y = LO(0,n-1)
print(y-x+1)