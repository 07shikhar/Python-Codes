class Vehicle:
    def __init__(self, number, price, name):
        self.number = number
        self.price = price
        self.name = name


class Store:
    def __init__(self, storeName, vlst):
        self.storeName = storeName
        self.vlst = vlst

    def findMinVehByPrice(self):
        x = min(self.vlst, key=lambda i: i.name)

        if x is None:
            return None
        else:
            return x

    def findMaxVehByNumber(self):
        y = max(self.vlst, key=lambda i: i.number)

        if y is None:
            return None
        else:
            return y


if __name__ == '__main__':
    vlst = []
    n = int(input())
    for i in range(n):
        number = int(input())
        price = int(input())
        name = input()
        obj = Vehicle(number, price, name)
        vlst.append(obj)
    obj1 = Store("ABC", vlst)
    v1 = obj1.findMinVehByPrice()
    v2 = obj1.findMaxVehByNumber()
    if v1 is None:
        print("No Data Found")
    else:
        print("{}\n{}\n{}".format(v1.number, v1.price, v1.name))
    if v2 is None:
        print("No Data Found")
    else:
        print("{}\n{}\n{}".format(v2.number, v2.price, v2.name))
