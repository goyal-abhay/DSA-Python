# Every element appears twice. Just one element comes once. Find unique element.

arr = list(map(int,input().split()))
ans = 0
for i in arr:
    ans = (ans^i)
print(ans)
