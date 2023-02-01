# Given an array and Q queries where Q{i}. Find max element from 0th to ith index.

arr = list(map(int,input().split()))
Q = int(input())
pmax = [0]*len(arr)
pmax[0] = arr[0]
for i in range(1,len(arr)):
    pmax[i] = max(pmax[i-1],arr[i])
for x in range(Q):
    i = int(input())
    print(pmax[i])