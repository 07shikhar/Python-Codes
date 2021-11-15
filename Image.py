class Image:
    def __init__(self, id, name, x, y, type):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.type = type

    def apply_filter(self, number):
        self.x += self.x*number/100
        self.y += self.y*number/100


class Album:
    def __init__(self, al_name, iLst):
        self.al_name = al_name
        self.iLst = iLst

    def cal_coord(self, per, iType):
        lst = []
        for i in self.iLst:
            if i.type.lower() == iType.lower():
                i.apply_filter(per)
                lst.append(i)

        if len(lst) == 0:
            return None
        else:
            return sorted(lst, key=lambda x: x.name)


if __name__ == '__main__':
    iLst = []
    n = int(input())
    for i in range(n):
        id = int(input())
        name = input()
        x = int(input())
        y = int(input())
        type = input()
        obj = Image(id, name, x, y, type)
        iLst.append(obj)

    obj1 = Album("ABC", iLst)
    iType = input()
    per = int(input())

    v1 = obj1.cal_coord(per, iType)
    if v1 is None:
        print("Image Not Found")

    else:
        for i in v1:
            print(i.name, i.x, i.y, sep= " ")
