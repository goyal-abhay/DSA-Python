n = int(input())

ct = 0
while n:
    n = (n & (n-1))
    ct+=1

print(ct)