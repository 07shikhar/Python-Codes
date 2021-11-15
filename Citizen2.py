class Citizen:
    def __init__(self, id, name, age, frontlineWorker, vaccineOpted, preference=None):
        self.id = id
        self.name = name
        self.age = age
        self.frontlineWorker = frontlineWorker
        self.vaccineOpted = vaccineOpted
        self.preference = preference

    def setPreference(self):
        if self.frontlineWorker.lower() == "yes" or self.age > 45:
            self.preference = 1
        else:
            self.preference = 0


class VaccinationDrive:
    def __init__(self, cLst):
        self.cLst = cLst

    def getPreferredVaccinationCount(self):
        count = 0
        for i in self.cLst:
            i.setPreference()
            if i.preference == 1:
                count += 1
        if count == 0:
            return None
        else:
            return count

    def getCitizensAsPerVaccine(self, vName):
        lst = []
        for i in self.cLst:
            if i.vaccineOpted == vName:
                lst.append(i)

        lst.sort(key=lambda i: i.age)
        if len(lst) == 0:
            return None
        else:
            return lst


if __name__ == '__main__':
    cLst = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        name =input("name")
        age = int(input("age"))
        frontlineWorker = input("frontline?")
        vaccineOpted = input("vaccine opted")
        obj = Citizen( id, name, age, frontlineWorker, vaccineOpted)
        cLst.append(obj)

    obj1 = VaccinationDrive(cLst)
    v1 = obj1.getPreferredVaccinationCount()
    vName = input("Vaccine to check")
    v2 = obj1.getCitizensAsPerVaccine(vName)
    if v2 is None:
        print("Vaccine Not found")
    else:
        for i in v2:
            print(i.id, i.name, i.age, sep= "\n")

    if v1 is None:
        print("Citizen not found")
    else:
        print(v1)

