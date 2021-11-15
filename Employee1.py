class Employee:
    def __init__(self, id, name, ageInRole, status="In Service"):
        self.id = id
        self.name = name
        self.ageInRole = ageInRole
        self.status = status


class Organization:
    def __init__(self, elst):
        self.elst = elst

    def updateStatus(self, noy):
        for i in self.elst:
            if i.ageInRole > noy:
                i.status = "Retirement Due"

    def countEmployees(self):
        count = 0
        for i in self.elst:
            if i.status == "Retirement Due":
                count += 1

        if count == 0:
            return None
        else:
            return count


if __name__ == '__main__':
    elst = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        name = input("name")
        ageInRole = int(input("age in role"))
        obj = Employee(id, name, ageInRole)
        elst.append(obj)

    obj2 = Organization(elst)
    noy = int(input("noy"))
    obj2.updateStatus(noy)
    v2 = obj2.countEmployees()
    print("Count of employees updated = {}".format(v2))
    for i in elst:
        print(i.id, i.name, i.status)
