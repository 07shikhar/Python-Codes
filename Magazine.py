class Magazine:
    def __init__(self, author, viewers, cost, name):
        self.author = author
        self.viewers = viewers
        self.cost = cost
        self.name = name


class Publisher:
    def __init__(self, publishingHouse, magazineList):
        self.publishingHouse = publishingHouse
        self.magazineList = magazineList

    def findMaxMagByCost(self):
        x = max(self. magazineList, key=lambda i: i.cost)

        if x is None:
            return None
        else:
            return x

    def sortMagByCost(self):
        y = sorted(self. magazineList, key=lambda i: i.cost)

        if len(y) == 0:
            return None
        else:

            return y


if __name__ == '__main__':
    magazineList = []
    n = int(input())
    for i in range(n):
        author = input()
        viewers = int(input())
        cost = int(input())
        name = input()
        obj = Magazine(author, viewers, cost, name)
        magazineList.append(obj)

    obj1 = Publisher("abc", magazineList)
    value1 = obj1.findMaxMagByCost()
    value2 = obj1.sortMagByCost()
    if value1 is None:
        print("No data found")
    else:
        print(value1.author, value1.viewers, value1.cost, value1.name, sep="\n")

    if value2 is None:
        print("No data found")
    else:
        for i in value2:
            print(i.cost, sep="\n")
