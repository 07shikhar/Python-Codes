class Service:
    def __init__(self, id, regNo, model, mileage, isInsured, paymentRcvd):
        self.id = id
        self.regNo = regNo
        self.model = model
        self.mileage = mileage
        self.isInsured = isInsured
        self.paymentRcvd = paymentRcvd


class ServiceCentre:
    def __init__(self, mileageDic, serviceList):
        self.mileageDic = mileageDic
        self.serviceList = serviceList

    def getTotalPayment(self, mName, stateCode):
        sum = 0
        count1 = 0
        for i in self.serviceList:
            v = i.model.split(" ")
            if mName.lower() == v[0].lower():
                count1 += 1
                if stateCode.lower() in i.regNo.lower():
                    if i.isInsured.lower() == 'yes':
                        sum += i.paymentRcvd

        if count1 == 0:
            return None
        else:
            return sum

    def getServicedCar(self):
        lst = []
        for i in self.serviceList:
            for key in self.mileageDic.keys():
                if i.model == key:
                    if i.mileage >= self.mileageDic[key]:
                        lst.append(i)

        if len(lst) == 0:
            return None
        else:
            return sorted(lst, key= lambda x:x.mileage, reverse=True)


if __name__ == '__main__':
    serviceList = []
    mileageDic = {}
    n = int(input())
    for i in range(n):
        id = int(input())
        regNo = input()
        model = input()
        mileage = int(input())
        isInsured = input()
        paymentRcvd = float(input())
        obj = Service(id, regNo, model, mileage, isInsured, paymentRcvd)
        serviceList.append(obj)

    m = int(input())
    for i in range(m):
        mode = input()
        expMileage = int(input())
        mileageDic[mode] = expMileage

    obj1 = ServiceCentre(mileageDic, serviceList)
    mName = input()
    stateCode = input()
    v1 = obj1.getTotalPayment(mName, stateCode)
    v2 = obj1.getServicedCar()
    if v1 is None:
        print("Insured car not found with given model and state code")
    else:
        print("{} {} {}".format(stateCode.upper(), mName.upper(), v1))

    if v2 is None:
        print("Car Not Found")
    else:
        for i in v2:
            print("{}#{}#{}#{}".format(i.id, i.regNo, i.model, i.mileage))

