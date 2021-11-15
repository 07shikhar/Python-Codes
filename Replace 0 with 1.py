arr = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1]
n = len(arr)
for i in range(n):
    if arr[i] == 0:
        arr[i] += 1
    else:
        arr[i] -= 1

print(arr)