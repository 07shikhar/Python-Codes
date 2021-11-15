class Sponsor:
    def __init__(self, name, company, subsidiaries, category):
        self.name = name
        self.company = company
        self.subsidiaries = subsidiaries
        self.category = category


def getSponsor(splst, icategroy):
    lst = []
    for i in splst:
        if i.category == icategroy:
            lst.append(i.name)

    if len(lst) == 0:
        return None
    else:
        return sorted(lst)


def maxSub(splst):
    nlst = []
    max = 0
    for i in splst:
        if len(i.subsidiaries) > max:
            max = len(i.subsidiaries)

    for i in splst:
        if max == len(i.subsidiaries):
            nlst.append(i.name)

    return nlst[0]


if __name__ == '__main__':
    splst = []
    n = int(input("range"))
    for i in range(n):
        name = input("name")
        company = input("company")
        subsidiaries = []
        m = int(input("range for sub"))
        for i in range(m):
            sub = input("enter sub")
            subsidiaries.append(sub)
        category = input("category")
        obj = Sponsor(name, company, subsidiaries, category)
        splst.append(obj)

    icategory = input("category to check")
    v1 = getSponsor(splst, icategory)
    if v1 is None:
        print("No record found")
    else:
        for i in v1:
            print(i)

    v2 = maxSub(splst)
    print(v2)


