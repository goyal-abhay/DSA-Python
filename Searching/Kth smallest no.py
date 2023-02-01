# Given an unsorted array and int k. Find Kth smallest no.

n = int(input())
a = list(map(int,input().split()))
k = int(input())

def func(x):
    cnt = 0
    for i in range(n):
        if a[i]<=x:
            cnt+=1
    return cnt

def BS(l,h):
    while l<=h:
        m = (l+h)//2
        if func(m)<k:
            l = m+1
        else:
            if func(m-1)<k:
                return m
            else:
                h = m-1

print(BS(min(a),max(a)))