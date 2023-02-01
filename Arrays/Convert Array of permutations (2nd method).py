# Given an array which is a permutation of numbers from 0 to n-1. Convert the array (if a[i]==j then a[j]==i)

arr = list(map(int,input().split()))

n = len(arr)
for i in range(n):
    old = arr[i]%n
    arr[old] = n*i + arr[old]
for i in range(n):
    arr[i]//=n
print(arr)