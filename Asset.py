class Asset:
    def __init__(self, id, name, type, location, status):
        self.id = id
        self.name = name
        self.type = type
        self.location = location
        self.status = status


class Manager:
    def __init__(self, alst):
        self.alst = alst

    def countAssetBAsedOnType(self):
        dic = {}
        for i in self.alst:
            if i.type not in dic.keys():
                dic[i.type] = 1
            else:
                dic[i.type] += 1

        return dic

    def allocateAssets(self, ilocation):
        count = 0
        for i in self.alst:
            x = i.location.split(sep=",")
            y = i.location.split(sep="-")
            for j in x:
                for k in y:
                    if ilocation == j or ilocation == k:
                        if i.status == "unallocated":
                            i.status = "allocated"
                            count += 1

        return count


if __name__ == '__main__':
    alst = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        name = input("name")
        type = input("type")
        location = input("location")
        status = input("status")
        obj = Asset(id, name, type, location, status)
        alst.append(obj)

    obj1 = Manager(alst)
    ilocation = input("location to check")
    v1 = obj1.countAssetBAsedOnType()
    for i in v1:
        print(i, v1[i])

    v2 = obj1.allocateAssets(ilocation)
    if v2 == 0:
        print("No asset found")
    else:
        print("Number of assets update: {}".format(v2))
    for i in alst:
        print(i.id, i.status, sep=" ")
