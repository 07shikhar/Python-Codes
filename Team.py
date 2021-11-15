class Team:
    def __init__(self, owner, value, id, name):
        self.owner = owner
        self.value = value
        self.id = id
        self.name = name


class League:
    def __init__(self, leagueName, teamList):
        self.leagueName = leagueName
        self.teamList = teamList

    def minId(self):
        x = min(self.teamList, key=lambda i: i.id)

        if x is None:
            return None
        else:
            return x

    def sortById(self):
        y = sorted(self.teamList, key=lambda i: i.id)

        if len(y) == 0:
            return None
        else:
            return y


if __name__ == '__main__':
    teamList = []
    n = int(input("range"))
    for i in range(n):
        owner = input("owner")
        value = float(input("value"))
        id = int(input("id"))
        name = input("name")
        obj = Team(owner, value, id, name)
        teamList.append(obj)

    obj1 = League("abc", teamList)
    v1 = obj1.minId()
    v2 = obj1.sortById()
    if v1 is None:
        print("No data found")
    else:
        print(v1.owner, v1.value, v1.id, v1.name, sep= "\n")

    if v2 is None:
        print("No data found")
    else:
        for i in v2:
            print(i.id)

