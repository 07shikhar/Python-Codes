# # def func(lst, oq):
# #     result = filter(lambda x: x < oq, lst)
# #     return result
# #
# #
# # n = int(input("range"))
# # lst = []
# # for i in range(n):
# #     ele = int(input("ele"))
# #     lst.append(ele)
# #
# # oq = int(input("oq"))
# # v1 = func(lst, oq)
# # for i in v1:
# #     print(i)
# # lst = [1, 3, 4, 6, 2, 8]
# # for i in lst:
# #     print(lst[i])
# # result = filter(lambda x: x < oq, lst)
# # for i in result:
# #     print(i)
# # for i in lst:
# #     if i < 7:
# #         print(i)
# # date = '21/06/2021'
# # l = date.rsplit('/', 1)
# # print(l[-2])
# # l = ["05","06","08"]
# # a = int(l[1]) - int(l[0])
# # print(a)
# # l1 = [3, 6, 9, 12, 15, 18, 21]
# # l1.append([2, 5, 8, 7])
# # print(l1[5][4])
# # l2 = [4,8,12,16,20,24,28]
# # l3 = []
# # e1 = l1[1::2]
# # e2 = l2[0::2]
# # l3.extend(e1)
# # l3.extend(e2)
# # print(l3)
# # print(l1[0])
# # print('The value of x is {} and y is {} and z is {}'.format(42,89,15))
#
# # a = 1
# # b = 2
# # v = map(str)
# # for i in v:
# #     print(i)
#
#
# # print(sum1)
# # lst = list(str)
# # print(lst)
# # for i in lst:
# #     if i == 'a':
# #         sum1 +=1
# #     :
# #         sum1 +=2
# #
# # print(sum1)
# # print(ord("a"))
# #0 d = [x for x in range(5)]
# # t = [x for x in range(7) if x in d and x%2==0]
# # print(t)
# t = {1:'A', 2:'B', 3:'C'}
# # del t[1]
# # t[1] = 'D'
# # del t[2]
# # del t[3]
# # print(len(t))
# for i in t:
#     print(i)
# l1 = [1,5,8,9]
# n = len(l1)
# l2 = [15,14,78,56]
# l3 = l1+l2
# for i in l3:
#     print(i, end=" ")
# r = list(dict.fromkeys(l1))
# print(r)
# v = l1[2:1:-1]
arr = [10, 20, 30, 40, 50]
x = len(arr)
print(x)
n = 3
for j in range(n):
    y = arr[x-1]
    for i in range(x-1,0,-1):
        arr[i] = arr[i-1]

    arr[0] = y
print(arr)
