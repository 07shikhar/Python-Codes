arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
arr1 = []
for i in range(len(arr)):
    if arr[i] > 1:
        arr1.append(arr[i])

for i in range(len(arr1)):
    arr.remove(arr1[i])
    arr.append(arr1[i])

print(arr)
