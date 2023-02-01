# Every element comes twice. Two elements appears once. Find two elements.

arr = list(map(int,input().split()))
over = 0
for i in range(len(arr)):
    over^=arr[i]
lsb = 1
while (lsb & over)==0:
    lsb<<=1
val1 = 0
for i in range(len(arr)):
    if (arr[i] & lsb):
        val1^=arr[i]
val2 = (over^val1)
print(val1,val2)