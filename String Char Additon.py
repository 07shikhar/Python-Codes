s = "321"
arr = list(s)
n = len(arr)
arr2 = []
for i in range(n-1):
    a = arr[i] + arr[i+1]
    arr.append(a)
if s not in arr:
    arr.append(s)

sum = 0
for i in arr:
    sum += int(i)

print(sum)


