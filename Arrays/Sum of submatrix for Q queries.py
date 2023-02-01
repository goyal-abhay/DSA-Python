# Given a 2D array and Q queries. Each query contains four integers i1,j1,i2,j2 (where i1<i2 and j1<j2). Find sum of submatrix formed by (i1,j1) and (i2,j2).

m,n = map(int,input().split())
arr = []
for i in range(m):
    c = list(map(int,input().split()))
    arr.append(c)


for i in range(m):
    for j in range(1,n):
        arr[i][j]+=arr[i][j-1]

for i in range(1,m):
    for j in range(n):
        arr[i][j]+=arr[i-1][j]

q = int(input())
for i in range(q):
    i1,j1,i2,j2 = map(int,input().split())
    ans = arr[i2][j2]
    if i1>0:
        ans-=arr[i1-1][j2]
    if j1>0:
        ans-=arr[i2][j1-1]
    if i1>0 and j1>0:
        ans+=arr[i-1][j-1]
    print(ans)