def itemCount(arr, n):
    dic = {}
    lst = []
    for i in range(n):
        if arr[i] not in dic.keys():
            dic[arr[i]] = 1
        else:
            dic[arr[i]] += 1

    for item in dic.keys():
        if dic[item] == 1:
            lst.append(item)

    return lst[0]


if __name__ == '__main__':
    arr = [101, 102, 103, 104]
    n = len(arr)
    ans = itemCount(arr, n)
    print(ans)
