# arr = [6, -1, -3, 4, -2, 2, 4, 6, -12, -7]
# c = 0
# n = len(arr)
# for i in range(n-1):
#     for j in range(i+1, n):
#         arr[i] += arr[j]
#         if arr[i] == 0:
#             c += 1
#
#
# print(c)
arr = [2, 4, 6, 8, 9, 10, 12]
arr2 = [2, 4, 6, 8, 10, 12]
for i in range(len(arr)):
    if arr[i] not in arr2:
        print(i)
