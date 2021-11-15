arr = [1, 5, 3, 4, 3, 5, 6]
n = len(arr)
l = []
for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            l.append(i+1)
            break
print(l[0])



