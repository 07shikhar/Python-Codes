arr = [10, 20, 30, 40, 50]
n = len(arr)
l1 = []

for i in range(n - 1):
    s = 0
    for j in range(i + 1, n):
        s += arr[j]
    l1.append(s)


print(l1)
