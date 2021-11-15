arr1 = [7, 0, 5, 1, 3]
arr2 = [1, 2, 1, 3, 4]
n = len(arr1)
diff = 0
l1 = []
for i in range(n):
    diff += arr1[i]
    diff -= arr2[i]
    l1.append(diff)

print(max(l1))
