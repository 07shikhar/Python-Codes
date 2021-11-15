arr = [1, 10, 5, 2, 7]
s = 0
m = 9
arr2 = []
n = len(arr)
for i in range(n):
    if arr[i] > m:
        print("1")
    else:
        for j in range(i + 1, n):
            arr[i] += arr[j]
            if arr[i] > m:
                arr2.append(j - i + 1)
                s = 0
print(arr2)
