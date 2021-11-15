class ServiceCentre:
    def __init__(self, name, branch, amount, availOnline):
        self.name = name
        self.branch = branch
        self.amount = amount
        self.availOnline = availOnline


class MyClass:
    def __init__(self, slst):
        self.slst = slst

    def findAvg(self):

        sum = 0
        count = 0
        avg = 0

        for i in self.slst:
            if i.availOnline == "True":
                count += 1
                sum += i.amount
                avg = sum / count

        if avg == 0:
            return None
        else:
            return avg

    def ServiceCentres(self, istr):
        lst = []
        for i in self.slst:
            if istr == i.branch[0]:
                lst.append(i)
        x = sorted(lst, key=lambda i: i.amount, reverse=True)
        nw = sorted(self.slst, key=lambda i: i.amount, reverse=True)

        for j in nw:
            if j in x:
                continue
            else:
                x.append(j)

        return x


if __name__ == '__main__':
    slst = []
    n = int(input("range"))
    for i in range(n):
        name = input("name")
        branch = input("branch")
        amount = int(input("amount"))
        availOnline = input("avail")
        obj = ServiceCentre(name, branch, amount, availOnline)
        slst.append(obj)

    obj2 = MyClass(slst)
    v1 = obj2.findAvg()
    istr = input("char")
    v2 = obj2.ServiceCentres(istr)

    print(v1)
    for i in v2:
        print(i.name, i.amount, sep="\n")
