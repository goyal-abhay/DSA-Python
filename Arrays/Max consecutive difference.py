#Given an unsorted array. Find max consecutive difference b/w 2 elemenets in a sorted array.

arr = list(map(int,input().split()))

def maxGap(a):
    n = len(a)
    if n<2:
        return 0
    maxNum = max(a)
    minNum = min(a)
    if minNum==maxNum:
        return 0
    gap = (maxNum-minNum)//(n-1)
    if (maxNum-minNum)%(n-1) != 0:
        gap+=1
    minArr = [10**9]*n
    maxArr = [-(10**9)]*n
    for i in range(n):
        bkt = (a[i]-minNum)//gap
        minArr[bkt] = min(minArr[bkt],a[i])
        maxArr[bkt] = max(maxArr[bkt],a[i])
    ans = -(10**9)
    prev = -(10**9)
    for i in range(n):
        if prev==(-(10**9)):
            prev = maxArr[i]
        else:
            ans = max(ans,minArr[i]-prev)
            prev = maxArr[i]
    return ans

print(maxGap(arr))