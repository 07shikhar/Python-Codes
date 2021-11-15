class Food:
    def __init__(self, name, proteins, fat, carbs, energy=0, status=None):
        self.name = name
        self.proteins = proteins
        self.fat = fat
        self.carbs = carbs
        self.energy = energy
        self.status = status


class Nutrition:
    def __init__(self, energyDict, foodList):
        self.energyDict = energyDict
        self.foodList = foodList

    def setEnergy(self):
        for i in self.foodList:
            i.energy = i.proteins + i.fat + i.carbs
            for key in self.energyDict.keys():
                if self.energyDict[key][0] <= i.energy <= self.energyDict[key][1]:
                    i.status = key

    def getEnergyRichFood(self, iEnergy):
        lst = []
        for i in self.foodList:
            if i.energy <= iEnergy:
                lst.append(i)

        if len(lst) == 0:
            return None
        else:
            return lst


if __name__ == '__main__':
    foodList = []
    energyDict = {}
    n = int(input())
    for i in range(n):
        name = input()
        proteins = float(input())
        fat = float(input())
        carbs = float(input())
        obj = Food(name, proteins, fat, carbs)
        foodList.append(obj)

    m = int(input())
    for i in range(m):
        status = input()
        lowerLimit = int(input())
        upperLimit = int(input())
        if lowerLimit > upperLimit:
            lowerLimit, upperLimit = upperLimit, lowerLimit
        tup = (lowerLimit, upperLimit)
        energyDict[status] = tup

    obj1 = Nutrition(energyDict, foodList)
    iEnergy = int(input())
    obj1.setEnergy()
    print("Energy of Food:")
    for i in foodList:
        print("{} - {} - {}".format(i.name, i.energy, i.status))
    v1 = obj1.getEnergyRichFood(iEnergy)
    if v1 is None:
        print("No Food Found")
    else:
        print("Food within given criteria:")
        for i in v1:
            print("{} : {}".format(i.name, i.energy))



