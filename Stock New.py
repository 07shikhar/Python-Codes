arr = [10, 18, 26, 31, 4, 69, 53]
l1 = []
n = len(arr)
m = 0
for i in range(n - 1):
    d = 0
    for j in range(i + 1, n):
        d = arr[j] - arr[i]
        if d > m:
            m = d
            l1.append(m)

print(l1)
