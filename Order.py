class Order:
    def __init__(self, orderid, agentid, km, price, status="Received"):
        self.orderid = orderid
        self.agentid = agentid
        self.km = km
        self.price = price
        self.status = status

    def getDeliveryFee(self):
        fee = 0
        if self.km > 10:
            fee = self.price * 0.2

        elif 5 <= self.km <= 10:
            fee = self.price * 0.1

        elif self.km < 5:
            fee = self.price * 0.05

        return fee


class DeliveryPartner:
    def __init__(self, orderList):
        self.orderList = orderList

    def getMatchingOrders(self, number):
        for i in self.orderList:
            if i.status == "Received":
                if i.getDeliveryFee() <= number:
                    i.status = "Accepted"

    def getOrderToDeliver(self):
        lst = []
        for i in self.orderList:
            if i.status == "Accepted":
                i.status = "Out For Delivery"
                lst.append(i)

        if len(lst) == 0:
            return None
        else:
            return lst


if __name__ == '__main__':
    orderList = []
    n = int(input())
    for i in range(n):
        orderid = int(input())
        agentid = int(input())
        km = int(input())
        price = int(input())
        obj = Order(orderid, agentid, km, price)
        orderList.append(obj)

    obj1 = DeliveryPartner(orderList)
    number = int(input())
    obj1.getMatchingOrders(number)
    v2 = obj1.getOrderToDeliver()
    if v2 is None:
        print("No order to deliver")
    else:
        print("Details of order out for delivery")
        for i in v2:
            print(i.orderid, i.status, sep=" ")

    print("Order details:")
    orderList.sort(key=lambda i: i.getDeliveryFee(), reverse= True)
    for i in orderList:
        print(i.orderid, i.getDeliveryFee(), i.status, sep=" ")
