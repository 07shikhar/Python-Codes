class Tool:
    def __init__(self, id, type, timesUsed, dateUsed):
        self.id = id
        self.type = type
        self.timesUsed = timesUsed
        self.dateUsed = dateUsed


class ToolManager:
    def __init__(self, toolList):
        self.toolList = toolList

    def assignTool(self, iType, iDate):
        lst = []
        count1 = 0
        count = 0
        for i in self.toolList:
            count1 += 1
            if i.type.lower() == iType.lower():
                lst.append(i)

        x = min(lst, key=lambda i: i.timesUsed)
        a = x.dateUsed.split("/")
        b = iDate.split("/")
        if int(b[1]) - int(a[1]) > 2:
            count += 1
            x.timesUsed += 1
            x.dateUsed = iDate

        if count == 0 or count1 == 0:
            return None
        else:
            return x

    def getToolsByType(self):
        dic = {}
        for i in self.toolList:
            if i.type.lower() not in dic.keys():
                dic[i.type.lower()] = 1
            else:
                dic[i.type.lower()] += 1

        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return sorted_dic


if __name__ == '__main__':
    toolList = []
    n = int(input())
    for i in range(n):
        id = int(input())
        type = input()
        timesUsed = int(input())
        dateUsed = input()
        obj = Tool(id, type, timesUsed, dateUsed)
        toolList.append(obj)

    obj1 = ToolManager(toolList)
    iType = input()
    iDate = input()
    v1 = obj1.assignTool(iType, iDate)
    v2 = obj1.getToolsByType()
    if v1 is None:
        print("No tool found")
    else:
        print(v1.id, v1.type.upper(), v1.timesUsed, sep=" ")

    for i in v2:
        print(i[0].upper(), i[1])
