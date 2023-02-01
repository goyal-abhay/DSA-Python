# Given a 2D array and an int K. Each row and each column is sorted in the array. Find the position of the K.

m,n = map(int,input().split())
arr = []
for i in range(m):
    c = list(map(int,input().split()))
    arr.append(c)
k = int(input())

i = 0
j = n-1
while i<m and j>=0:
    if arr[i][j]==k:
        print(i,j)
        break
    elif arr[i][j]<k:
        i+=1
    else:
        j-=1

if i==m or j==-1:
    print(-1)
