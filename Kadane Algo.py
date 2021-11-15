arr = [1, 2, 3, -2, 5]
currSum = 0
maxSum = 0
c = 0
for i in range(len(arr)):
    currSum += arr[i]
    if currSum > maxSum:
        maxSum = currSum
    if currSum < 0:
        currSum = 0
    if arr[i] < 0:
        c += 1
        if c == len(arr):
            arr.sort()
            maxSum = arr[len(arr) - 1]

print(maxSum)
