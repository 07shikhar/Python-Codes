nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']
dic = {}
for i in range(len(nuts)):
    dic[nuts[i]] = i

for i in range(len(bolts)):
    if bolts[i] in dic:
        nuts[i] = bolts[i]
print(dic)
print(nuts)
print(bolts)



