arr = [2, 202, 3, 200, 4, 5]
n = len(arr)
msis = [0 for x in range(n)]
print(msis)
for i in range(n):
    msis[i] = arr[i]
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and msis[i] < msis[j] + arr[i]:
            msis[i] = msis[j] + arr[i]
print(msis)
