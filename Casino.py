arr = [2, 202, 2, 3, 200, 4, 5]
n = len(arr)
l = []
m = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[i] < arr[j]:
            arr[i] += arr[j]
            if arr[i] > m:
                m = arr[i]

print(m)


