class Apparel:
    def __init__(self, brand, price, type, inStock):
        self.brand = brand
        self.price = price
        self.type = type
        self.inStock = inStock


class Store:
    def __init__(self, apparelList):
        self.apparelList = apparelList

    def checkApparelAvail(self, ibrand, itype, isize, number):
        c1 = 0
        c2 = 0
        c3 = 0
        for i in self.apparelList:
            if ibrand == i.brand and itype == i.type:
                c1 += 1
                for size, stock in i.instock.items():
                    if isize == size:
                        c2 += 1
                        if number < stock:
                            c3 += 1
                            stock -= number
                            print(size, ":", stock)
                        #     return True
                        # else:
                        #     return False

        if c1 > 0 and c2 > 0 and c3 > 0:
            return True

        else:
            return False


if __name__ == '__main__':
    apparelList = []
    n = int(input("Range"))
    for i in range(n):
        brand = input("brand")
        price = int(input("name"))
        type = input("type")
        inStock = {}
        m = int(input("for dic"))
        for j in range(m):
            size = input("Size")
            stock = int(input("stock"))
            inStock[size] = stock

        obj = Apparel(brand, price, type, inStock)

    obj1 = Store(apparelList)
    ibrand = input("Brand to check")
    itype = input("Type to check")
    isize = input("city to check")
    number = int(input("Number"))

    result = obj1.checkApparelAvail(ibrand, itype, isize, number)
    if not result:
        print("Size is not available")
    status = False
    for i in apparelList:
        if i.brand == ibrand and i.type == itype:
            status = True
            break
    if not status:
        print("Apparel not Found")
