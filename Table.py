class Table:
    def __init__(self, tableNo, waiterName, status):
        self.tableNo = tableNo
        self.waiterName = waiterName
        self.status = status


def findWaiterWiseTotalNoOfTables(tlst):
    dic = {}
    for i in tlst:
        if i.waiterName not in dic.keys():
            dic[i.waiterName] = 1

        else:
            dic[i.waiterName] += 1

    return dic


def findWaiterNameByTableNo(tlst, number):
    # count = 0
    for i in tlst:
        if i.tableNo == number:
            return i.waiterName
            # count +=1
    # return None


if __name__ == '__main__':
    tlst = []
    n = int(input("Range"))
    for i in range(n):
        tableNo = int(input('Table no'))
        waiterName = input("name")
        status = input("status")
        obj = Table(tableNo, waiterName, status)
        tlst.append(obj)

    number = int(input("pages to check"))

    result1 = findWaiterWiseTotalNoOfTables(tlst)

    for i in sorted(result1):
        print("{}-{}".format(i, result1[i]))

    result2 = findWaiterNameByTableNo(tlst, number)

    if result2 is None:
        print("Not found")

    else:
        print(result2)
