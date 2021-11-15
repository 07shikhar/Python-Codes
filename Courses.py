class Courses:
    def __init__(self, id, name, admin, quiz, handsOn):
        self.id = id
        self.name = name
        self.admin = admin
        self.quiz = quiz
        self.handsOn = handsOn


class MyClass:
    def __init__(self, cLst):
        self.cLst = cLst

    def findAverage(self, iAdmin):
        lst = []
        sum = 0
        avg = 0
        for i in self.cLst:
            if i.admin == iAdmin:
                lst.append(i.quiz)

        for i in lst:
            sum += i
            avg = sum / len(lst)

        if avg == 0:
            return None
        else:
            return avg

    def sortByHandsOn(self, number):
        mlst = []
        for i in self.cLst:
            if i.handson <= number:
                mlst.append(i)

        mlst.sort(key=lambda i: i.handsOn)
        if len(mlst) == 0:
            return None
        else:
            return mlst


if __name__ == '__main__':
    cLst = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        name = input("name")
        admin = input("admin")
        quiz = int(input("quiz"))
        handsOn = int(input("handsOn"))
        obj = Courses(id, name, admin, quiz, handsOn)
        cLst.append(obj)

    obj1 = MyClass(cLst)
    iAdmin = input("admin to check")

    v1 = obj1.findAverage(iAdmin)
    v2 = obj1.sortByHandsOn(number=int(input("pages")))
    if v1 is None:
        print("no")
    else:
        print(v1)

    if v2 is None:
        print("not found")
    else:
        for i in v2:
            print(i.id, i.name, sep="\n")
