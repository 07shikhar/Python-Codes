class Document:
    def __init__(self, id, name, details):
        self.id = id
        self.name = name
        self.details = details


class Archive:
    def __init__(self, aid, list):
        self.aid, self.list = aid, list

    def date(self):
        ans = {}
        for i in self.list:
            k = i.details.split(",")
            for j in k:
                if len(j) == 10 and j[2] == '/' and j[5] == '/':
                    if i.id not in ans.keys():
                        ans[i.id] = j
                    else:
                        continue

        return ans

    def count(self, string):
        c = 0
        for i in self.list:
            k = i.name.split(".")
            for j in k:
                if j == string:
                    c += 1
        return c


if __name__ == '__main__':
    n = int(input("n"))
    li = []
    for i in range(n):
        a = int(input("id"))
        b = input("name")
        c = input("details")
        obj = Document(a, b, c)
    obj1 = Archive(11, li)
    string = input("to check")
    k = obj1.date()
    if len(k) > 0:
        for i in k:
            print(i, k[i])
    y = obj1.count(string)
    print("document count = ", y)
