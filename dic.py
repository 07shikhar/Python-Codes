# dic = {}
# n = int(input("Enter length"))
#
#
# for i in range(n):
#     k = input("Enter type of product")
#     v1 = input("Enter name of product")
#     # dic[k] = v1
#     if k in dic:
#         # l.append(v1)
#         # dic[k] = l
#         dic[k] = [dic[k], v1]
#
#     else:
#         dic[k] = v1
# print(dic)
#
# final_list = []
#
# dict_key = input("Enter type")
#
# if dict_key in dic:
#
#         desc = dic.get(dict_key)
#         final_list.append(desc)
#         print(final_list)
#
#
# else:
#     print("Product not available")

# for i in final_list:
#     print(final_list[1])
# n = int(input("Enter length"))
# lst = []
# for i in range(n):
#     name = input("NAme")
#     age = int(input("Age"))
#     lst.append(name)
#     lst.append(age)
#
# if age < 45:
#     print(name)
# years_dict = dict()
#
# for line in list:
#     if line[0] in years_dict:
#         # append the new pages to the existing array at this slot
#         years_dict[line[0]].append(line[1])
#     else:
#         # create a new array in this slot
#         years_dict[line[0]] = [line[1]]
dic = {}
mj = []
n = int(input("Enter length"))

for i in range(n):
    k = input("Enter type of product")
    v1 = input("Enter name of product")
    # dic[k] = v1
    if k in dic:
        dic[k].append(v1)

    else:
        dic[k] = [v1]

key2 = max(dic, key = lambda i: dic[i])
print(dic[key2])
v2 = dic[key2]
mj.append(v2)
largest_value = max(mj)
print(largest_value)
# for keys, values in dic.items():
#     for i in values:
#         print(i)
#
# final_list = []
#
# dict_key = input("Enter type")
#
# if dict_key in dic:
#
#     desc = dic.get(dict_key)
#     final_list.append(desc)
#     for desc in final_list:
#         for j in desc:
#             print(j)
# adf = []
# final_list = []
# n = int(input("Enter length"))
# for i in range(n):
#     name = input("Enter name")
#     age = input("Enter age")
#     course = input("Enter course")
#     adf.append([age, name, course])

# adf.append(age)
# adf.append(course)
# x = course.strip(" ")
# if '/' in x:
#     final_list.append(name)

# else:
#     continue

# print(final_list)

# adf.sort()
# for i in adf:
#     print(*i)
