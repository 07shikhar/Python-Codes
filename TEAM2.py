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

    def findMinimumTeamById(self):
        min_obj = min(self.teamList, key=lambda i: i.id)
        if min_obj is None:
            return None
        else:
            return min_obj

    def sortById(self):
        y = sorted(self.teamList, key=lambda i: i.id)

        if len(y) == 0:
            return None
        else:
            return y


if __name__ == '__main__':
    count = int(input())
    teamList = []
    for i in range(count):
        owner = input()
        value = float(input())
        id = int(input())
        name = input()
        team = Team(owner, value, id, name)
        teamList.append(team)
    ex = League("ABC", teamList)
    x = ex.findMinimumTeamById()
    y = ex.sortById()
    if x is None:
        print("No Data Found")
    else:
        print(x.owner, x.value, x.id, x.name, sep= "\n")
    if y is None:
        print("No Data Found")
    else:
        for i in y:
            print(i.id)
