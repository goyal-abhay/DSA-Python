# Rotate the given array k times in clockwise direction.

arr = list(map(int,input().split()))
k = int(input())
n = len(arr)
tarr = [0]*n
for i in range(n):
    tarr[(i+k)%n] = arr[i]
print(tarr)