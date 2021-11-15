def triplet(arr, n, x):
    c = 0
    arr2 = []
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] < x:
                    c += 1
                    arr2.append([arr[i], arr[j], arr[k]])
    return arr2


if __name__ == '__main__':
    arr = [-2, 0, 1, 3]
    n = len(arr)
    x = 2
    ans = triplet(arr, n, x)
    print(ans)
