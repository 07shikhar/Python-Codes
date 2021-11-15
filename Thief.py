def thief(arr, n):
    maxsum = 0
    for i in range(n):
        for j in range(i + 2, n, 2):
            arr[i] += arr[j]
            if arr[i] > maxsum:
                maxsum = arr[i]
    return maxsum


arr = [1, 2, 3]
n = len(arr)
print(thief(arr, n))
