num = 7876
s = str(num)
arr = list(s)
n = len(arr)
l = []
d = 0
for i in range(n - 1):
    d = 0
    d += int(arr[i]) - int(arr[i + 1])
    l.append(d)
    l.append(d * -1)
print(l)
c = 0
for i in l:
    if i <= 1:
        c += 1
if c == len(l):
    print("Correct")
else:
    print("Not Correct")
