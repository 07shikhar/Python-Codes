class Allium:
    def __init__(self, marketId, alliumType, producingState, price):
        self.marketId = marketId
        self.alliumType = alliumType
        self.producingState = producingState
        self.price = price


class MyClass:
    def __init__(self, alst):
        self.alst = alst

    def findTypeByState(self, inputState):
        count = 0
        for i in self.alst:
            if i.producingState == inputState:
                count += 1
                return i.alliumType

        if count == 0:
            return None

    def sortByPrice(self, number):
        lst = []
        sum = 0
        avg = 0
        for i in self.alst:
            if i.name < number:
                lst.append(i)

        x = sorted(lst, key=lambda x: x.name)
        for i in x:
            sum += i.name
            avg = sum / len(lst)

        return avg


if __name__ == '__main__':
    alst = []
    n = int(input("range"))
    for i in range(n):
        marketId = int(input("market id"))
        alliumType = input("type")
        producingState = input("prod state")
        price = int(input("name"))
        obj = Allium(marketId, alliumType, producingState, price)
        alst.append(obj)

    obj1 = MyClass(alst)
    istate = input("state to check")
    v1 = obj1.findTypeByState(istate)
    num = int(input("num"))
    v2 = obj1.sortByPrice(num)
    if v1 is None:
        print("State not found")
    else:
        print(v1)

    print(v2)
