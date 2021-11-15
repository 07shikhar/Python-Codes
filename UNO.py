n = 1098765
s = str(n)
while int(s) > 9:
    s2 = 0
    for i in s:
        s2 += int(i)
    s = str(s2)

if int(s) == 1:
    print("UNO")
else:
    print(s)


