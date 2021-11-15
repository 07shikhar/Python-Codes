l1 = [12, 10, 5, 6, 52, 36]

r = len(l1)
e = l1[r-1]
k = 2
l2 = []
l3 = []
for i in range(r):
    if i == 0:
        l2.append(l1[i])
        for i in l2:
            for j in l1:
                if i == j:
                    l1.remove(i)
                    l1.append(j)


l1.pop(r-1)
l1.insert(0, e)


print(l1)
