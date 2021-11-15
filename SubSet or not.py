arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]
c = 0
for i in arr1:
    for j in arr2:
        if i == j:
            c += 1

if c == len(arr2):
    print("Yes")
else:
    print("no")
