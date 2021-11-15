arr = [6,-1,-3,4,-2,2,4,6,-12,-7]
n = len(arr)
arr2 = []
c = 0
s = 0
for i in range(n):
    # for j in range(i + 1, n):
    #     if arr[i] != 0:
    #         arr[i] += arr[j]
    #         if arr[i] == 0:
    #             c += 1
    s += arr[i]
    if s == 0:
        c += 1
        # else:
        #     c += 1

if c > 0:
    print(c)
else:
    print("No")
