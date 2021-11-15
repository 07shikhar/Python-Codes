class Property:
    def __init__(self, property_type, property_value, max_bid_price):
        self.property_type = property_type
        self.property_value = property_value
        self.max_bid_price = max_bid_price


class Tender:
    def __init__(self, buyerName, propertyType, bidPrice):
        self.buyerName = buyerName
        self.propertyType = propertyType
        self.bidPrice = bidPrice


def bidProperty(propertyList, tenderList):
    names = []
    for i in propertyList:  # 3
        for j in tenderList:
            if j.propertyType.lower() == i.property_type.lower():
                if i.property_value <= j.bidPrice <= i.max_bid_price:
                    propertyList.remove(i)
                    names.append(j)

    m = max(names, key=lambda i: i.bidPrice)

    return m


if __name__ == '__main__':
    propertyList = []  # 1
    tenderList = []
    n = eval(input("range"))
    for i in range(n):
        property_type = input("type")
        property_value = eval(input("valie"))
        max_bid_price = eval(input("max bid"))
        propertyList.append(Property(property_type, property_value, max_bid_price))

    m = eval(input("range for yender"))
    for i in range(m):
        buyerName = input("name")
        propertyType = input("type")
        bidPrice = eval(input("bof name"))
        tenderList.append(Tender(buyerName, propertyType, bidPrice))

    finalList = bidProperty(propertyList, tenderList)  # 2
    print(finalList.buyerName)
    for item in propertyList:
        print(item.property_type)
