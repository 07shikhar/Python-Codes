arr = [2, 3, 4, 5, -1, 0]
maxPro = 0
m = 1
n = len(arr)
for i in range(n):
    for j in range(i + 1, n):
        arr[i] = arr[i] * arr[j]
        if arr[i] > maxPro:
            maxPro = arr[i]
print(maxPro)
