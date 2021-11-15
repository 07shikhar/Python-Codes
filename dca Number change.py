def convertNumber(n):
    v = str(n)
    u = list(v)
    ulst = []
    for i in u:
        if int(i) == 0:
            i = 9
            ulst.append(str(i))
        else:
            o = 9 - int(i)
            ulst.append(str(o))
    s = ""
    for i in ulst:
        s += i

    fn = int(s)
    return fn


n = int(input())
if n > 5000:
    print("not possible")
else:
    print((convertNumber(n)))
