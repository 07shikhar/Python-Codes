s = "GfG"
ans = ord(s[0])
for i in range(1, len(s)):
    ans = ans ^ ord(s[i])

print(ans)


