# Find the floor value of square root of N.

n = int(input())

def BS(l,h):
    while l<=h:
        m = (l+h)//2
        if m*m>n:
            h = m-1
        else:
            if (m+1)*(m+1)>n:
                return m
            else:
                l = m+1
print(BS(0,n))