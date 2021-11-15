start = [2, 4, 1, 6, 9, 6]
end =   [3, 5, 7, 8, 10, 12]
n = len(start)
c = 1
for i in range(n - 1):
    if end[i] <= start[i + 1]:
        c = c + 1

print(c)
