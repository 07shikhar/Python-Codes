class Student:
    def __init__(self, id, year, percentage, name):
        self.id = id
        self.year = year
        self.percentage = percentage
        self.name = name


class Department:
    def __init__(self, slst):
        self.slst = slst

    def findMinStuByPer(self):
        x = min(self.slst, key=lambda i: i.percentage)
        return x

    def sortStudents(self):
        y = sorted(self.slst, key=lambda i: i.percentage)
        return y


if __name__ == '__main__':
    slst = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        year = int(input("year"))
        percentage = int(input("percentage"))
        name = input("name")
        obj = Student(id, year, percentage, name)
        slst.append(obj)

    obj2 = Department(slst)
    v1 = obj2.findMinStuByPer()
    print(v1.name)
    v2 = obj2.sortStudents()
    for i in v2:
        print(i.percentage)
