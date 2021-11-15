class Blood:
    def __init__(self, bloodGroup, unitInHand):
        self.bloodGroup = bloodGroup
        self.unitInHand = unitInHand


class BloodBank:
    def __init__(self, bloodList):
        self.bloodlist = bloodList

    def isBloodAvailable(self, inputbloodGroup, number):

        for i in self.bloodlist:
            if i.bloodGroup == inputbloodGroup:
                if i.unitInHand >= number:
                    return True
                else:
                    return False
            # else:
            #     continue

    def findMinBloodStock(self):
        blst = []
        nw = min(self.bloodlist, key=lambda i: i.unitInHand)
        for i in self.bloodlist:
            if nw.unitInHand == i.unitInHand:
                blst.append(i)

        return blst


if __name__ == '__main__':
    bloodList = []
    n = int(input("Enter range"))
    for i in range(n):
        bloodGroup = input("group")
        unitInHand = int(input("unit in hand"))
        obj = Blood(bloodGroup, unitInHand)
        bloodList.append(obj)

    obj2 = BloodBank(bloodList)
    ibloodGroup = input("blood group to check")
    number = int(input("Number"))
    result1 = obj2.isBloodAvailable(ibloodGroup, number)
    result2 = obj2.findMinBloodStock()

    if result1 is True:
        print("Available")

    else:
        print("Unavailable")

    for i in result2:
        print(i.bloodGroup)
