# Min value of arr[i]^arr[j]

arr = list(map(int,input().split()))
m = max(arr)
for i in range(len(arr)-1):
    a = arr[i]^arr[i+1]
    if a < m:
        m = a
print(m)