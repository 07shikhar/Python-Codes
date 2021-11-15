class Container:
    def __init__(self, id, length, breadth, height, pricePerSqFt):
        self.id = id
        self.length = length
        self.breadth = breadth
        self.height = height
        self.pricePerSqFt = pricePerSqFt

    def findVolume(self):
        volume = self.length * self.breadth * self.height
        return volume


class PackagingCompany:
    def __init__(self, clst):
        self.clst = clst

    def findContainerCost(self, inputId):
        price = 0
        for i in self.clst:
            if inputId == i.id:
                price = i.findVolume() * i.pricePerSqFt

        if price == 0:
            return None
        else:
            return price

    def largestVolume(self):
        # largest = []

        nw = max(self.clst, key=lambda i: i.findVolume())
        # largest.append(nw)
        return nw


if __name__ == '__main__':
    clst = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        length = int(input("length"))
        breadth = int(input("breadth"))
        height = int(input("height"))
        pricePerSqFt = int(input("name per"))
        obj = Container(id, length, breadth, height, pricePerSqFt)
        clst.append(obj)

    obj2 = PackagingCompany(clst)
    inputId = int(input("id to check"))
    result1 = obj2.findContainerCost(inputId)
    result2 = obj2.largestVolume()

    if result1 is None:
        print("Not found")

    else:
        print(result1)

    # for i in result2:
    #     print(i.id)
    print(result2.id)
