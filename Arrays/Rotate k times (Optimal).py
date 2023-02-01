# Rotate the given array k times in clockwise direction.

arr = list(map(int,input().split()))
k = int(input())
n = len(arr)

def rev(x,y):
    while x<y:
        t = arr[x]
        arr[x] = arr[y]
        arr[y] = t
        x+=1
        y-=1
    return 0

rev(0,n-k-1)
rev(n-k,n-1)
rev(0,n-1)

print(arr)