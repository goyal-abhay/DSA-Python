# Given an array and integer K. Print sum of elements in each subarray of size k.

arr = list(map(int,input().split()))
k = int(input())
n = len(arr)

sum = 0
for i in range(k):
    sum+=arr[i]

for j in range(k,n):
    print(sum)
    sum+=arr[j]
    sum-=arr[j-k]

print(sum)