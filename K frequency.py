arr = [1, 1, 1, 2, 2, 3]
d = {}
k = 2
for i in arr:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
print(d)
for j in d.keys():
    if d[j] >= k:
        print(j)
