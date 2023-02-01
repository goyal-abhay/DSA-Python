n = int(input())
i = int(input())

m = (1<<i)
if (n & m):
    print('Set')
else:
    print('Unset')