class City:
    def __init__(self, pin, name, population, area):
        self.pin = pin
        self.name = name
        self.population = population
        self.area = area


class District:
    def __init__(self,vlst):
        self.vlst = vlst

    def findMinCityByPin(self):
        x = min(self.vlst, key=lambda i: i.pin)

        if x is None:
            return None
        else:
            return x

    def sortCityByPopulation(self):
        y = sorted(self.vlst, key=lambda i: i.population)

        if len(y) == 0:
            return None
        else:
            return y


if __name__ == '__main__':
    vlst = []
    n = int(input())
    for i in range(n):
        pin = int(input())
        name = input()
        population = int(input())
        area = int(input())
        obj = City(pin, name, population, area)
        vlst.append(obj)
    obj1 = District(vlst)
    v1 = obj1.findMinCityByPin()
    v2 = obj1.sortCityByPopulation()
    if v1 is None:
        print("No Data Found")
    else:
        print("{}\n{}\n{}\n{}".format(v1.pin, v1.name, v1.population, v1.area))
    if v2 is None:
        print("No Data Found")
    else:
        for i in v2:
            print(i.population)
