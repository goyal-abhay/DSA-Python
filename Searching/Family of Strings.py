# Consider a family of strings(containing 0 and 1), where s[0] = 0 and s[i] = s[i-1].0.(s[i-1])'. Given 2 int n and k. Find kth char in s[n].

n,k = map(int,input().split())

def BS(l,h):
    bit = 0
    while l<=h:
        m = (l+h)//2
        if m==k:
            return bit
        elif m>k:
            h = m-1
        else:
            l = m+1
            bit = 1 - bit

print(BS(0,(2**(n+1))-2))