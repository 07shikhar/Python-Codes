s = "tcs7dca7rock57"
l = list(s)
n = len(l)
s1 = ""
s2 = ""
for i in range(n):
    for j in range(i + 1, n):
        if s[i] + s[j] == '56':
            s1 = s[i] + s[j]
    if s[i] == '7' and s[i - 1].isdigit():
        s2 = s[i - 1] + s[i]

print(len(s1))
print(s2)
if len(s1) > 0 and len(s2) > 0:
    s = s.replace(s1, "").replace(s2, "#").replace("7", "").replace("#", s2)
elif len(s1) == 0 and len(s2) > 0:
    s = s.replace(s2, '#').replace("7", "").replace("#", s2)
elif len(s1) > 0 and len(s2) == 0:
    s = s.replace(s1, "").replace("7", "")
print(s)
