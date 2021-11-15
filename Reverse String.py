# a = "geeks quiz practice code"
# l = a.split(" ")
# s = l[::-1]
# for i in s:
#     print(i, end=" ")
a = [6, 5, 4, 4]
c = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] >= a[j]:
            c += 1
print(c)
