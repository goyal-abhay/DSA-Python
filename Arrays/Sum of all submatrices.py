# Given a 2D array. Find sum of all submatrices of the 2D array.



n = int(input())
arr = [[0*n]*n]
for i in range(n):
    l = list(map(int,input().split()))
    arr.append(l)

sum = 0
for i in range(n):
    for j in range(n):
        sum+=(arr[i][j]*(i+1)*(j+1)*(n-i)*(n-j))

print(sum)