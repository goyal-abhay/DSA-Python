# Given an array. Find sum of all subarrays.

arr = list(map(int,input().split()))
n = len(arr)

ans = 0
for i in range(n):
    ans+=(i+1)*(n-i)*arr[i]

print(ans)