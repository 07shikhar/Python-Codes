# def geeko(a, b, c, n):
#     if n == a + b + c:
#         return n
#
def pali(s):
    n = len(s)
    if n == 0 or n == 1:
        return True

    if s[0] == s[n - 1]:
        return pali(s[1:n - 1])

    return False


s = "racecar"
p = pali(s)
print(p)
