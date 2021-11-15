arr = [1, 2, 3, 4, 5]
n = len(arr)
for i in range(n - 2):
    arr[i],arr[i+2] = arr[i+2], arr[i]

print(arr)
    