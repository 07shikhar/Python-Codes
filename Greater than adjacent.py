arr = [35, 15, 45, 25, 55]
n = len(arr)
c = 0
for i in range(1, n - 1):
    if arr[i] < arr[i + 1] and arr[i] < arr[i - 1]:
        c += 1

print(c)
