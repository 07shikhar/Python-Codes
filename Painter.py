class Painter:
    def __init__(self, id, name, price, type):
        self.id = id
        self.name = name
        self.price = price
        self.type = type


class ShowRoom:
    def __init__(self, plst):
        self.plst = plst

    def getTotalPaintingPrice(self, itype):
        totaPrice = 0
        for i in self.plst:
            if i.type == itype:
                totaPrice += i.name

        return totaPrice

    def getPainterWithMaxCountOfPaintings(self):
        dic = {}
        max = 0
        mlst = []
        for i in self.plst:
            if i.name not in dic.keys():
                dic[i.name] = 1

            else:
                dic[i.name] += 1

        for key, values in dic.items(): #or for key in dic.keys()[rest is same]
            if max < dic[key]:
                max = dic[key]
                mlst.append(key)

        x = sorted(mlst)
        return x[0]


if __name__ == '__main__':
    plst = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        name = input("name")
        price = int(input("name"))
        type = input("type")
        obj = Painter(id, name, price, type)
        plst.append(obj)

    obj2 = ShowRoom(plst)
    itype = input("type to check")
    v1 = obj2.getTotalPaintingPrice(itype)
    v2 = obj2.getPainterWithMaxCountOfPaintings()
    print(v1)
    print(v2)
