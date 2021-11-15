class Doctor:
    def __init__(self, id, name, deptName, consultFee, sundayAvailable):
        self.id = id
        self.name = name
        self.deptName = deptName
        self.consultFee = consultFee
        self.sundayAvailable = sundayAvailable


class Hospital:
    def __init__(self, doctorList):
        self.doctorList = doctorList

    def getDoctorList(self, ideptName):

        lst = []
        for i in self.doctorList:
            if ideptName.lower() == i.deptName and i.sundayAvailable == 'available':
                lst.append(i)
        return lst

    def selectDoctor(self, fee):

        for i in self.doctorList:
            if (i.sundayAvailable == 'not available') and (i.consultFee > fee):
                self.doctorList.remove(i)
                return True
            else:
                return False


if __name__ == '__main__':
    doctorList = []
    n = int(input("items"))
    for i in range(n):
        id = input("id")
        name = input("name")
        deptName = input("Dept name")
        consultFee = int(input("Consult fee"))
        sundayAvailable = input("Sunday ava")
        obj = Doctor(id, name, deptName, consultFee, sundayAvailable)
        doctorList.append(obj)

    v2 = Hospital(doctorList)
    ideptName = input("Deptname")
    fee = int(input("ifee"))

    result1 = v2.getDoctorList(ideptName)
    result2 = v2.selectDoctor(fee)

    if len(result1) == 0:
        print("No Doctor Found")
    else:
        for i in result1:
            print(i.id, " ", i.name)

    if result2 is False:
        print("Returning orignal list")
        for i in doctorList:
            print(i.id, " ", i.name)

    else:
        doctorList.sort(key=lambda i: i.consultFee)
        for i in doctorList:
            print(i.id, " ", i.name)
