def stock(arr, n):
    l = []
    for i in range(n - 1, 0, -1):
        c = 1
        for j in range(i - 1, 0, -1):
            if arr[i] > arr[j]:
                c += 1
            else:
                c = 1
                break
        l.append(c)
    l.append(1)
    return l


arr = []
n = int(input())
for i in range(n):
    ele = int(input())
    arr.append(ele)

ans = stock(arr, n)
for i in ans[::-1]:
    print(i, end=" ")
# arr = [100, 60, 70, 65, 80, 85]
