arr = [16,17,4,3,5,2]
n = len(arr)
l = 2
# for i in range(n-1):
#     if arr[i+1] > arr[i]:
#         print("{} is a leader".format(arr[i+1]))
#
# print("{} is a leader".format(arr[n-1]))
for i in range(l):
    f = arr[0]
    for j in range(n-1):
        arr[j] = arr[j+1]

    arr[n-1] = f

print(arr)
