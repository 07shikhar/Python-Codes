arr = [1,9,3,10,4,20,2]
arr.sort()
print(arr)
arr2 = []
c = 0
ans = 0
n = len(arr)
for i in range(0, n-1):
    if arr[i+1] - arr[i] == 1:
        arr2.append(arr[i])
        arr2.append(arr[i+1])
    else:
        break
print(arr2)
s = set(arr2)
print(len(s))

