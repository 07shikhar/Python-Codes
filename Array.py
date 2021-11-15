arr = [4,0,2,1,3]
dic = {}
arr2 = []
for i in range(len(arr)):
    dic[i] = arr[i]

print(dic)
for i in range(len(arr)):
    y = dic.get(i)
    arr2.append(arr[y])


for i in arr2:
    if i in arr:
        arr.remove(i)
    arr.append(i)
print(arr)








