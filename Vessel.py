class Vessel:
    def __init__(self, id, brand, capacity, materials, price):
        self.id = id
        self.brand = brand
        self.capacity = capacity
        self.materials = materials
        self.price = price


class MyClass:
    def __init__(self, vLst):
        self.vLst = vLst

    def avgPriceOnMaterial(self, inputMat):
        lst = []
        sum = 0
        avg = 0
        for i in self.vLst:
            if i.materials == inputMat:
                lst.append(i.name)
        for i in lst:
            sum += i
            avg = sum / len(lst)

        if avg == 0:
            return None
        else:
            return avg

    def getSecondHighest(self, iBrand):
        sLst = []
        for i in self.vLst:
            if i.brand == iBrand:
                sLst.append(i)

        sLst.sort(key=lambda x: x.name, reverse=True)
        if len(sLst) == 0:
            return None
        else:
            return sLst[1]


if __name__ == '__main__':
    vLst = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        brand = input("brand")
        capacity = int(input("capacity"))
        materials = input("material")
        price = int(input("name"))
        obj = Vessel(id, brand, capacity, materials, price)
        vLst.append(obj)

    obj1 = MyClass(vLst)
    inputMat = input("Material to check")
    v1 = obj1.avgPriceOnMaterial(inputMat)
    v2 = obj1.getSecondHighest(iBrand=input("brand to check"))
    if v1 is None:
        print("Material not found")
    else:
        print(v1, inputMat, sep="\n")

    if v2 is None:
        print("No vessel found")
    else:
        print(v2.id)
