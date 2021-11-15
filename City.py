class City:
    def __init__(self, id, stateName, cityName, rainfallRcvd, year):
        self.id = id
        self.stateName = stateName
        self.cityName = cityName
        self.rainfallRcvd = rainfallRcvd
        self.year = year


class RainfallAnalysis:
    def __init__(self, cityList):
        self.cityList = cityList

    def getStateWiseRainfall(self):
        lst = {}
        for i in self.cityList:
            if i.stateName not in lst.keys():
                lst[i.stateName] = i.rainfallRcvd
            else:
                lst[i.stateName] += i.rainfallRcvd

        if len(lst) == 0:
            return None
        else:
            return lst

    def AvgRain(self, iState):
        sum1 = 0
        avg = 0
        aLst = []
        dic = {}
        for i in self.cityList:
            if i.stateName == iState:
                aLst.append(i)

        for i in aLst:
            sum1 += i.rainfallRcvd
            avg = sum1 / len(aLst)

        for i in aLst:
            if i.rainfallRcvd > avg:
                dic[i.cityName] = i.rainfallRcvd

        if len(dic) == 0:
            return None
        else:
            return dic


if __name__ == '__main__':
    cityList = []
    n = int(input())
    for i in range(n):
        id = int(input())
        stateName = input()
        cityName = input()
        rainfallRcvd = int(input())
        year = int(input())
        obj = City(id, stateName, cityName, rainfallRcvd, year)
        cityList.append(obj)

    obj1 = RainfallAnalysis(cityList)
    v1 = obj1.getStateWiseRainfall()
    iState = input()
    v2 = obj1.AvgRain(iState)
    if v1 is None:
        print("No data Found")
    else:
        for i in sorted(v1.keys()):
            print("{} {}".format(i, v1[i]))

    if v2 is None:
        print("No city available")
    else:
        for i in v2:
            print("{} {}".format(i, v2[i]))
