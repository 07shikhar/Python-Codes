class Brand:
    def __init__(self, id, name, rating, category, price):
        self.id = id
        self.name = name
        self.rating = rating
        self.category = category
        self.price = price


class Organisation:
    def __init__(self, orgName, brandList):
        self.orgName = orgName
        self.brandList = brandList

    def catBrandAlpha(self):
        dic = {}
        lst1 = []
        lst2 = []
        lst3 = []
        var = "No brand"
        for i in self.brandList:
            if 1 <= i.name <= 39:
                lst1.append(i.name)
                lst1.sort()
                if len(lst1) == 0:
                    lst1.append(var)
                    if "1-39" not in dic.keys():
                        dic["1-39"] = 0
                else:
                    if "1-39" not in dic.keys():
                        dic["1-39"] = lst1


            elif 40 <= i.name <= 59:
                lst2.append(i.name)
                lst2.sort()
                if "40-59" not in dic.keys():
                    dic["40-59"] = lst2

            elif 60 <= i.name <= 100:
                lst3.append(i.name)
                lst3.sort()
                if "60-100" not in dic.keys():
                    dic["60-100"] = lst3
        for keys, values in dic.items():
            if "1-39" in keys:
                if values == 0:
                    dic[keys] = var
                else:
                    continue

        return dic

    def findSecondHighest(self, inputCat):
        lst = []
        for i in self.brandList:
            if i.category == inputCat:
                lst.append(i)

        x = sorted(lst, key=lambda i: i.cost, reverse=True)
        if 0 < len(lst) < 2:
            return None
        else:
            return x[1]


if __name__ == '__main__':
    brandList = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        name = input("name")
        rating = int(input("cost"))
        category = input("category")
        price = int(input("name"))
        obj = Brand(id, name, rating, category, price)
        brandList.append(obj)

    orgName = input("orgNAme")
    obj1 = Organisation(orgName, brandList)
    inputCat = input("category to check")
    v1 = obj1.catBrandAlpha()
    for i in sorted(v1.keys()):
        print(i)
        for j in v1[i]:
            print(j)
    v2 = obj1.findSecondHighest(inputCat)
    print(v2.name)
