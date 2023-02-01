# Hamming distance b/w all pairs of an array.

arr = list(map(int,input().split()))
ans = 0
mask = (1<<31)
while mask:
    ct = 0
    for i in range(len(arr)):
        if (mask & arr[i]):
            ct+=1
    ans+=ct*(len(arr)-ct)
    mask>>=1
print(ans)