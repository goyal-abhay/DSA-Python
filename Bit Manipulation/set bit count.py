n = int(input())

m = (1<<32)
ct = 0
while m:
    if (n & m):
        ct+=1
    m>>=1

print(ct)