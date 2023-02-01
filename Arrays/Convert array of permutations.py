# Given an array which is a permutation of numbers from 0 to n-1. Convert the array (if a[i]==j then a[j]==i)



arr = list(map(int,input().split()))
n = len(arr)
for i in range(n):
    if arr[i]>=0:
        idx = arr[i]
        val = i
        while idx!=i:
            temp = arr[idx]
            arr[idx] = -(val+1)
            val = idx
            idx = temp
        arr[idx] = -(val + 1)
for i in range(n):
    arr[i] = -1*arr[i]-1

print(*arr)