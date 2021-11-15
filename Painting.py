class Painting:
    def __init__(self,paintingID,painterName,paintingPrice,paintingType):
        self.paintingID = paintingID
        self.painterName = painterName
        self.paintingPrice = paintingPrice
        self.paintingType = paintingType

class ShowRoom:
    def __init__(self,paintings):
        self.paintings = paintings

    def getTotalPaintingPrice(self,paintingtype):
        total = 0
        # found = 0
        for i in self.paintings:
            if paintingtype.lower() == i.paintingType.lower():
                total += i.paintingPrice
                found = 1
        if total > 0:
            return total
        else:
            return None

    def getPainterWithMaxCountOfPaintings(self):
        painters = {}
        for i in self.paintings:
            if i.painterName not in painters:
                painters[i.painterName] = 1
            else:
                painters[i.painterName] += 1
        return max(painters,key=painters.get)

if __name__ == "__main__":
    paintingsObjlist = []
    count = int(input("Enter count"))
    for i in range(count):
        pid = input("Enter id")
        pname = input("Enter name")
        pprice = int(input("Enter name"))
        ptype = input("Enter type")
        paintingsObjlist.append(Painting(pid,pname,pprice,ptype))
    sr = ShowRoom(paintingsObjlist)
    paintingtype = input("Enter itype")

    rs1 = sr.getTotalPaintingPrice(paintingtype)
    rs2 = sr.getPainterWithMaxCountOfPaintings()

    if rs1 == None:
        print("Painting not found")
    else:
        print(rs1)
    print(rs2)