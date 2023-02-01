# Given a sorted array of length>=2 and elements of array belongs to [1...n-1]. All elements comes once, only one element comes twice. Find that element. 

n = int(input())
a = list(map(int,input().split()))

def BS(l,h):
    while l<=h:
        m = (l+h)//2
        if a[m]==m:
            h = m-1
        else:
            if a[m]==a[m+1]:
                return a[m]
            else:
                l = m+1

print(BS(0,n-1))