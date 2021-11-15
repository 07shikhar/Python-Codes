arr = [1, 4, 45, 6, 10, 8]
n = 6
c = 0
arr2 = []
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] == 22:
                c += 1
                arr2.append([arr[i], arr[j], arr[k]])

if c > 0:
    print(c)
else:
    print("No")
print(arr2)