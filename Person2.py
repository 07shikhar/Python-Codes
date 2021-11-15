class Employee:
    def __init__(self, eId, name, age, sName, salary):
        self.eId = eId
        self.name = name
        self.age = age
        self.sName = sName
        self.salary = salary


class Supevisor:
    def __init__(self, supervisorName, empList):
        self.supervisorName = supervisorName
        self.empList = empList

    def findEmployeeWithMaxAge(self):
        x = max(self.empList, key=lambda i: i.age)

        if x is None:
            return None
        else:
            return x

    def sortEmployeeBySalary(self):
        y = sorted(self.empList, key=lambda i: i.salary)

        if y is None:
            return None
        else:
            return y


if __name__ == '__main__':
    empList = []
    n = int(input())
    for i in range(n):
        eId = input()
        name = input()
        age = int(input())
        sName = input()
        salary = float(input())
        obj = Employee(eId, name, age, sName, salary)
        empList.append(obj)

    obj1 = Supevisor("ABC", empList)
    v1 = obj1.findEmployeeWithMaxAge()
    v2 = obj1.sortEmployeeBySalary()
    if v1 is None:
        print("No Data Found")
    else:
        print("{}\n{}\n{}\n{}\n{}".format(v1.eId, v1.name, v1.age, v1.sName, v1.salary))

    if v2 is None:
        print("No Data Found")
    else:
        for i in v2:
            print(i.salary)
