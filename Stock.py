prices = [7, 6, 4, 3, 1]
n = len(prices)
maxPro = []
for i in range(n):
    for j in range(i + 1, n):
        diff = prices[j] - prices[i]
        if diff > 0:
            maxPro.append(diff)

maxPro.sort(reverse=True)
if len(maxPro) > 0:
    print(maxPro[0])
else:
    print("0")
#-------------------------------------
# arr = [1, 1, 1, 1]
# n = len(arr)
# k = 2
# c = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         if arr[i] + arr[j] == k:
#             c += 1
# print(c)
#-------------------------------------
# l1 = [1, 5, 10, 20, 40, 80]
# l2 = [6, 7, 20, 80, 100]
# l3 = [3, 4, 15, 20, 30, 70, 80, 120]
# l4 = []
# for i in l1:
#     for j in l2:
#         for k in l3:
#             if i == j == k:
#                 l4.append(i)
#
# print(l4)
