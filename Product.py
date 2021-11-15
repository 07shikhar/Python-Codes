class Product:
    def __init__(self, productName, productType, productPrice, quantityOnHand, reorderedQuantity):
        self.productName = productName
        self.productType = productType
        self.productPrice = productPrice
        self.quantityOnHand = quantityOnHand
        self.reorderedQuantity = reorderedQuantity


def findAvailableStock(plst, nameList):
    dic = {}
    c = 0
    for i in plst:
        for name in nameList:
            if i.productName == name:
                dic[i.productName] = i.quantityOnHand
                c += 1

    if c > 0:
        return dic
    else:
        return None


def updateStockByProductType(plst, qtyToAdd, iptype):
    count = 0
    for i in plst:
        if i.productType == iptype:
            count += 1
            if i.quantityOnHand < i.reorderedQuantity:
                i.quantityOnHand += qtyToAdd

    if count > 0:
        return plst
    else:
        return None


if __name__ == '__main__':
    plst = []
    n = int(input("Enter range"))
    for i in range(n):
        productName = input("name")
        productType = input("type")
        productPrice = int(input("name"))
        quantityOnHand = int(input("On hand"))
        reorderedQuantity = int(input("reordered"))
        obj = Product(productName, productType, productPrice, quantityOnHand, reorderedQuantity)
        plst.append(obj)

    nameList = []
    m = int(input("range for names"))
    for i in range(m):
        name = input("enter {} name".format(i+1))
        nameList.append(name)

    qtyToAdd = int(input("Add qty to add"))
    iptype = input("type to check")

    v1 = findAvailableStock(plst, nameList)

    if v1 is None:
        print("No product found")

    else:
        for i in v1:
            print("{} {}".format(i, v1[i]))

    v2 = updateStockByProductType(plst, qtyToAdd, iptype)

    if v2 is None:
        print("No product Found")

    else:
        for i in v2:
            print(i.productName, i.quantityOnHand)
