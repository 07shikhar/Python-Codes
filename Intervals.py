# arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
# n = len(arr)
# l1 = []
# for i in range(0, n-1):
#     if arr[i][1] >= arr[i + 1][0]:
#         l1.append([arr[i][0], arr[i + 1][1]])
#     else:
#         l1.append(arr[i])
#
# print(l1)
arr = [1, 20, 6, 4, 5]
n = len(arr)
inv_count = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            inv_count += 1

print(inv_count)

