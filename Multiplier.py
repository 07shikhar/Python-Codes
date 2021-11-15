def multiplier(l1, r):
    l2 = []
    for i in range(0, r):
        if l1[i] % 10 == 0:
            l2.append(l1[i])
    for j in l2:
        if j in l1:
            l1.remove(j)
            l1.append(j)
    return l1


l1 = [10, 12, 5, 40, 30, 7, 5, 9, 10]
r = len(l1)
a = multiplier(l1, r)
print(a)
