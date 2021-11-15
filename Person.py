class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


class Society:
    def __init__(self, plst):
        self.plst = plst

    def AvgHeight(self):
        sum = 0
        avg = 0
        for i in self.plst:
            sum += i.height
            avg = sum / len(self.plst)

        return avg

    def taller(self):
        tlst = []
        for i in self.plst:
            if i.height > self.AvgHeight():
                tlst.append(i.name)

        return tlst


if __name__ == '__main__':
    plst = []
    n = int(input("Range"))
    for i in range(n):
        name = input("name")
        height = int(input("height"))
        weight = int(input("weight"))
        obj = Person(name, height, weight)
        plst.append(obj)

    obj2 = Society(plst)
    r1 = obj2.AvgHeight()
    print("The average height is {}".format(r1))
    r2 = obj2.taller()
    for i in r2:
        print("Person taller than average is {}".format(i), sep= "\n")
