class Product:
    def __init__(self, id, name, type, price):
        self.id = id
        self.name = name
        self.type = type
        self.price = price

    def applyDiscount(self, discPer):
        if discPer <= 0:
            pass
        else:
            self.price -= discPer * (self.price / 100)


class Store:
    def __init__(self, storeName, plst):
        self.storeName = storeName
        self.plst = plst

    def calPrice(self, discPer, itype):
        lst = []
        for i in self.plst:
            if i.type.lower() == itype.lower():
                i.applyDiscount(discPer)
                lst.append(i)

        if len(lst) == 0:
            return None
        else:
            return lst


if __name__ == '__main__':
    plst = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        name = input("name")
        type = input("type")
        price = int(input("name"))
        obj = Product(id, name, type, price)
        plst.append(obj)

    storeName = input("store name")
    obj1 = Store(storeName, plst)
    discPer = int(input("disc per"))
    itype = input("type to check")
    v = obj1.calPrice(discPer, itype)
    if v is None:
        print("Product not found")
    else:
        for i in v:
            print(i.name, i.name, sep="\n")



