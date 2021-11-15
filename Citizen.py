class Citizen:
    def __init__(self, id, name, age, profession, isWarrior, city):
        self.id = id
        self.name = name
        self.age = age
        self.profession = profession
        self.isWarrior = isWarrior
        self.city = city


dic1 = {}
dic2 = {}


class Health:
    def __init__(self, clst):
        self.clst = clst

    def getHighestCity(self):
        # dic1 = {}
        # dic2 = {}

        for i in self.clst:
            if i.isWarrior.lower() == 'true':
                if i.city not in dic1.keys():
                    dic1[i.city] = 1
                else:
                    dic1[i.city] += 1
            elif i.isWarrior.lower() != 'true':
                if i.city not in dic1.keys():
                    dic1[i.city] = 0
                else:
                    dic1[i.city] += 0
            if i.age > 60:
                if i.city not in dic2.keys():
                    dic2[i.city] = 1
                else:
                    dic2[i.city] += 1
            elif i.age < 60:
                if i.city not in dic2.keys():
                    dic2[i.city] = 0
                else:
                    dic2[i.city] += 0

        max1 = max(dic1, key=lambda i: dic1[i])
        max2 = max(dic2, key=lambda i: dic2[i])
        return max1, max2

    def cityWiseRequirement(self):
        # dic1 = {}
        # dic2 = {}
        dic3 = {}

        # for i in self.clst:
        #     if i.isWarrior.lower() == 'true':
        #         if i.city not in dic1.keys():
        #             dic1[i.city] = 1
        #         else:
        #             dic1[i.city] += 1
        #     else:
        #         dic1[i.city] = 0
        #     if i.age > 60:
        #         if i.city not in dic2.keys():
        #             dic2[i.city] = 1
        #         else:
        #             dic2[i.city] += 1
        #     else:
        #         dic2[i.city] = 0

        for keys, values in dic1.items():
            if keys not in dic3.keys():
                dic3[keys] = [values]

        for i, j in dic2.items():
            if i in dic3.keys():
                dic3[i].append(j)

        return dic3


if __name__ == '__main__':
    clst = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        name = input("name")
        age = int(input("age"))
        profession = input("profession")
        isWarrior = input("warrior?")
        city = input("city")
        obj = Citizen(id, name, age, profession, isWarrior, city)
        clst.append(obj)

    obj1 = Health(clst)
    v1 = obj1.getHighestCity()
    print(v1)

    v2 = obj1.cityWiseRequirement()
    for i in v2:
        print("{}:{}".format(i, v2[i]))
