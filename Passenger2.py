class Passenger:
    def __init__(self, id, name, seat, mealOpted, classOpted):
        self.id = id
        self.name = name
        self.seat = seat
        self.mealOpted = mealOpted
        self.classOpted = classOpted


class Airlines:
    def __init__(self, plst, bmDict):
        self.plst = plst
        self.bmDict = bmDict

    def getMealCount(self):
        count1 = 0
        count2 = 0
        dic = {}
        for i in self.plst:
            if i.classOpted.lower() == "economy":
                if i.mealOpted.lower() == "yes":
                    count1 += 1
                    dic["EconomyMealsOrdered"] = count1

                else:
                    count2 += 1
                    dic["EconomyMealsNotOrdered"] = count2

        dic2 = sorted(dic.items(), key= lambda x:x[1])

        if len(dic2) == 0:
            return None
        else:
            return dic2

    def getMealFromSeat(self, iSeat):
        # lst = []
        x = None
        for i in self.plst:
            if i.seat == iSeat:
                for key in self.bmDict.keys():
                    if i.id == key:
                        x = self.bmDict[key]

        if x is None:
            return None
        else:
            return x


if __name__ == '__main__':
    plst = []
    bmDict = {}
    n = int(input())
    for i in range(n):
        id = int(input())
        name = input()
        seat = input()
        mealOpted = input()
        classOpted = input()
        obj = Passenger(id, name, seat, mealOpted, classOpted)
        plst.append(obj)

    for i in plst:
        if i.classOpted.lower() == "business":
            food1 = input()
            food2 = input()
            bmDict[i.id] = [food1, food2]
        else:
            continue

    obj1 = Airlines(plst, bmDict)
    iSeat = input()
    v1 = obj1.getMealCount()
    v2 = obj1.getMealFromSeat(iSeat)
    if v1 is None:
        print("no")
    else:
        for i in v1:
            print("{}:{}".format(i[0], i[1]))

    if v2 is None:
        print("Nah")
    else:
        for i in v2:
            print(i)


