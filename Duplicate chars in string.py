s = "geeksforgeeks"
arr = []
dic = {}
for i in range(len(s)):
    if s[i] not in dic.keys():
        dic[s[i]] = 1
    else:
        dic[s[i]] += 1

for i in dic.keys():
    if dic[i] > 1:
        print("{}:{}".format(i, dic[i]))
