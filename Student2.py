class Student:
    def __init__(self, sId, name, sClass, fee, feePaid):
        self.sId = sId
        self.name = name
        self.sClass = sClass
        self.fee = fee
        self.feePaid = feePaid


class School:
    def __init__(self, busList, sList):
        self.busList = busList
        self.sList = sList

    def getFee(self):
        dic = {}
        for i in self.sList:
            for j in self.busList:
                if i.sId == j:
                    total = i.fee + 1200
                    dic[i.sId] = total

        if len(dic) == 0:
            return None
        else:
            return dic

    def getFeeNotPaid(self, iClass):
        lst = []
        for i in self.sList:
            v = i.sClass.split("-")
            if iClass == v[0]:
                if i.feePaid.lower() == 'no':
                    lst.append(i)

        if len(lst) == 0:
            return None
        else:
            return sorted(lst, key=lambda i: i.name)


if __name__ == '__main__':
    busList = []
    sList = []
    n = int(input())
    for i in range(n):
        sId = int(input())
        name = input()
        sClass = input()
        fee = int(input())
        feePaid = input()
        obj = Student(sId, name, sClass, fee, feePaid)
        sList.append(obj)

    m = int(input())
    for i in range(m):
        ele = int(input())
        busList.append(ele)

    obj1 = School(busList, sList)
    iClass = input()
    v1 = obj1.getFee()
    v2 = obj1.getFeeNotPaid(iClass)

    if v1 is None:
        print("no student availed bus service")
    else:
        for i in v1:
            print("{}#{}".format(i, v1[i]))

    if v2 is None:
        print("class not present or all fee paid")
    else:
        for i in v2:
            print("{}#{}#{}".format(i.sId, i.name, i.sClass))
