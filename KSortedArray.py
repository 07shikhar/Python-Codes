arr = [[1, 2, 3, 4], [2, 2, 3, 4], [5, 5, 6, 6], [7, 8, 9, 9]]
arr1 = []
k = len(arr)
for i in range(k):
    for j in range(k):
        arr1.append(arr[i][j])

arr1.sort()
for i in arr1:
    print(i, end=" ")
