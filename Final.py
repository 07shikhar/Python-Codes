class Boutique:
    def __init__(self, bid, bname, btype, brating, points):
        self.bid = bid
        self.bname = bname
        self.btype = btype
        self.brating = brating
        self.points = points


class OnlineBoutique:
    def __init__(self, bdict):
        self.bdict = bdict

    def getBoutique(self, lowerlimit, upperlimit, extrapoints, type):
        lst1 = []
        self.lowerlimit = lowerlimit
        self.upperlimit = upperlimit
        self.extrapoints = extrapoints
        self.type = type
        for keys, values in self.bdict.items():
            if keys == type:
                for i in values:
                    if lowerlimit <= i.brating <= upperlimit:
                        i.points = extrapoints + i.points
                        lst1.append([i.points, i.bname, i.bid])
                lst1.sort()
                return (lst1)


if __name__ == "__main__":
    n = int(input("Enter length"))
    bdic = {}
    for i in range(n):
        bid = input("Enter id")
        bname = input("Enter name")
        btype = input("Enter type")
        brating = int(input("Enter cost"))
        points = int(input("Enter points"))

        obj = Boutique(bid, bname, btype, brating, points)
        if obj.btype in bdic.keys():
            bdic[obj.btype].append(obj)

        else:
            bdic[obj.btype] = [obj]

    lower = float(input("Enter lower limit"))
    upper = float(input("Enter upper limit"))
    extra = int(input("Enter extra points"))
    type = input("Enter type to append")
    obj1 = OnlineBoutique(bdic)
    values = obj1.getBoutique(lower, upper, extra, type)

    if len(values) == 0:
        print("No boutique")

    else:
        for i in values:
            for j in i:
                print(j)
    # vest = obj1.getBoutique(lower, upper, extra, type)
