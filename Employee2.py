class Employee:
    def __init__(self, ename, designation, salary, leaveBalance):
        self.ename = ename
        self.designation = designation
        self.salary = salary
        self.leaveBalance = leaveBalance


class Organization:
    def __init__(self, elst):
        self.elst = elst

    def checkLeaveEligibilty(self, inputName, inputType, number):
        for i in self.elst:
            if inputName == i.ename:
                for keys in i.leaveBalance.keys():
                    if inputType == keys:
                        for values in i.leaveBalance.values():
                            if number < i.leaveBalance[keys]:
                                i.leaveBalance[keys] = values - number
                                # print("{}:{}".format(keys, values))
                                return True
                            else:
                                return False

        # return "Not Found"


if __name__ == '__main__':
    elst = []
    n = int(input("range"))
    for i in range(n):
        ename = input("name")
        designation = input("designation")
        salary = int(input("salary"))
        leaveBalance = {}
        m = int(input("for dic"))
        for j in range(m):
            type = input("type")
            balance = int(input("balance"))
            leaveBalance[type] = balance

        obj = Employee(ename, designation, salary, leaveBalance)
        elst.append(obj)

    obj2 = Organization(elst)
    inputName = input("name to check")
    inputType = input("type to check")
    number = int(input("pages"))

    v1 = obj2.checkLeaveEligibilty(inputName, inputType, number)
    if v1 is True:
        print("Leave Granted")
        for i in elst:
            if inputName == i.ename:
                print(i.ename)
                for keys, values in i.leaveBalance.items():
                    print("{}:{}".format(keys, values))

    if v1 is False:
        print("Not granted")

    if v1 == "Not Found":
        print("Employee not found")
