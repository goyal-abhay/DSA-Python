# Given an array and two integers x and K. Print freq(x) in each subarray of size K.

arr = list(map(int,input().split()))
k = int(input())
x = int(input())
n = len(arr)

freq = 0
for i in range(k):
    if arr[i]==x:
        freq+=1

for j in range(k,n):
    print(freq)
    if arr[j]==x:
        freq+=1
    if arr[j-k]==x:
        freq-=1

print(freq)