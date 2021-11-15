r1 = 20
n = 4
r2 = 40
x = 144
h = x / 60
if type(h) == float:
    h = int(h) + 1
print(h)
d1 = h-n
a1 = n * r1
a2 = d1*r2
t = a1 + a2
print(t)
