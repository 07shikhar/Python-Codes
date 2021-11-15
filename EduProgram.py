class EduProgram:
    def __init__(self, name, sponsor, peopleAttended, stillAvailable, withCountry):
        self.name = name
        self.sponsor = sponsor
        self.peopleAttended = peopleAttended
        self.stillAvailable = stillAvailable
        self.withCountry = withCountry


class MyClass:
    def __init__(self, eplst):
        self.eplst = eplst

    def findClassification(self):
        oplk = None
        count = 0
        for i in self.eplst:

            if i.stillAvailable.lower() == i.withCountry.lower() == "true":
                count += 1
                if i.peopleAttended >= 1000:
                    oplk = "Ever Green"

                elif 500 <= i.peopleAttended < 1000:
                    oplk = "Golden"

                elif i.peopleAttended < 500:
                    oplk = "Emerging Star"

        if count == 0:
            return "No one found"

        else:
            return oplk

    def findProgramBySponsor(self, inputNAme):
        lst = []
        for i in self.eplst:
            if i.sponsor == inputNAme:
                lst.append(i)

        if len(lst) == 0:
            return None
        else:
            return sorted(lst, key=lambda i: i.peopleAttended)


if __name__ == '__main__':
    eplst = []
    n = int(input("range"))
    for i in range(n):
        name = input("enter name")
        sponsor = input("sponsor")
        peopleAttended = int(input("people"))
        stillAvailable = input("available?")
        withCountry = input("country?")
        obj = EduProgram(name, sponsor, peopleAttended, stillAvailable, withCountry)
        eplst.append(obj)

    obj2 = MyClass(eplst)
    v1 = obj2.findClassification()
    inputName = input("name to check")
    v2 = obj2.findProgramBySponsor(inputName)
    print(v1)
    for i in v2:
        print(i.name, i.peopleAttended, sep="\n")
