# Given an array and Q queries where Q{i,j}. Find sum of elements from arr[l] to arr[r].

arr = list(map(int,input().split()))
Q = int(input())
psum = [0]*len(arr)
psum[0] = arr[0]
for i in range(1,len(arr)):
    psum[i] = psum[i-1] + arr[i]
for x in range(Q):
    i,j = map(int,input().split())
    if i==0:
        print(psum[j])
    else:
        print(psum[j]-psum[i-1])