def doUnion(a, n, b, m):
    if n > m:
        for i in range(n):
            a.append(b[i])
            if len(a) == n + m:
                break
        s = set(a)
    else:
        for i in range(m):
            b.append(a[i])
            if len(b) == n + m:
                break
        s = set(b)
    return len(s)


a = [1, 8, 5, 6, 4]
b = [1, 5, 7, 4, 52, 78, 14]
n = len(a)
m = len(b)
ans = doUnion(a, n, b, m)
print(ans)