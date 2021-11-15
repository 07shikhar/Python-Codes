def repeatedNumbers(x, y):
    c = 0
    for i in range(x, y + 1, 1):
        s = str(i)
        if len(list(s)) == len(set(s)):
            c += 1
    return c


print(repeatedNumbers(101, 200))
