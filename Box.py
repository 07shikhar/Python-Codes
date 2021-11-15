class Box:
    def __init__(self, id, l, b, h, status="Available"):
        self.id = id
        self.l = l
        self.b = b
        self.h = h
        self.status = status

    def getVolume(self):
        volume = self.l * self.b * self.h
        return volume


class Shipping:
    def __init__(self, blst):
        self.blst = blst

    def findBoxesToPAck(self, ivolume):
        for i in self.blst:
            if i.status == "Available":
                if i.getVolume() <= ivolume:
                    i.status = "Packaged"

    def findBoxToShip(self, number):
        y = None
        count = 0
        sum = 0
        lst = []
        mlst = []
        for i in self.blst:
            if i.status == "Packaged":
                count += 1
                sum += i.getVolume()
                mlst.append(i)
            else:
                continue

        if len(mlst) > 0:
            y = max(mlst, key=lambda i: i.getVolume())
            lst.append(y)

        for i in mlst:
            sum2 = sum - y.getVolume()
            num2 = number - y.getVolume()
            y.status = "Sent"
            if i.status == "Sent":
                continue
            elif sum2 <= num2:
                if i.status == "Packaged":
                    num2 -= i.getVolume()
                    i.status = "Sent"
                    lst.append(i)
            elif i.getVolume() <= num2:
                if i.status == "Packaged":
                    i.status = "Sent"
                    lst.append(i)

        x = sorted(lst, key=lambda i: i.getVolume(), reverse=True)

        if count == 0:
            return None

        else:
            return x


if __name__ == '__main__':
    blst = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        l = int(input("length"))
        b = int(input("breadth"))
        h = int(input("height"))
        obj = Box(id, l, b, h)
        blst.append(obj)

    obj1 = Shipping(blst)
    ivolume = int(input("volume to check"))
    obj1.findBoxesToPAck(ivolume)
    number = int(input("capacity"))
    v1 = obj1.findBoxToShip(number)
    if v1 is None:
        print("No box to ship")
    else:
        print("Id of boxes Shipped:")
        for i in v1:
            print(i.id, i.status, sep=" ")
    print("The Box Details")
    for i in sorted(blst, key=lambda i: i.getVolume(), reverse=True):
        print(i.id, i.getVolume(), i.status, sep=" ")
