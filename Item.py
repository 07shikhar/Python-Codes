class Item:
    def __init__(self, itemName, itemType, unitPice):
        self.itemName = itemName
        self.itemType = itemType
        self.unitPrice = unitPice


class Store:
    def __init__(self, itemInventory):
        self.itemInventory = itemInventory

    def buyItem(self, inputName, orderedQty):
        bill = 0
        for key in self.itemInventory.keys():
            if inputName == key.itemName:
                if self.itemInventory[key] == 0:
                    bill = 0
                elif self.itemInventory[key] < orderedQty:
                    bill = key.unitPrice * self.itemInventory[key]
                    self.itemInventory[key] = 0
                elif self.itemInventory[key] >= orderedQty:
                    bill = key.unitPrice * self.itemInventory[key]
                    self.itemInventory[key] -= orderedQty

        if bill == 0:
            return None
        else:
            return bill


if __name__ == '__main__':

    itemInventory = {}
    n = int(input("range"))
    for i in range(n):
        itemName = input("name")
        itemType = input("type")
        unitPice = int(input("name"))
        obj = Item(itemName, itemType, unitPice)
        stock = int(input("Stock"))
        itemInventory[obj] = stock

    obj1 = Store(itemInventory)
    orderDic = {}
    m = int(input("range for od"))

    for i in range(m):
        inputName = input("Name to check")
        orderedQty = int(input("Qty ordered"))
        orderDic[inputName] = orderedQty
    for key in orderDic.keys():
        result = obj1.buyItem(key, orderDic[key])
        if result is None:
            print("{} is not available".format(key))
        else:
            print("Bill of item {} = {}".format(key, result))

    print("Stock in hand")
    for i in itemInventory:
        print("{} {}".format(i.itemName, itemInventory[i]))

