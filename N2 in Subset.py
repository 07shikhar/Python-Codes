arr = [8, 5, 3, 6, 9, 2, 3, 6, 9, 8]
n = len(arr)
n2 = 5
c = 0
s = 3
for i in range(0, n - s, s):
    for j in range(i, i + s):
        if arr[j] == n2:
            c += 1
        else:
            c = 0
if c > 0:
    print("1")
else:
    print("0")
