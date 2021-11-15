class Book:
    def __init__(self, id, name, subject, price):
        self.id = id
        self.name = name
        self.subject = subject
        self.price = price


class Library:
    def __init__(self, libName, blst):
        self.libName = libName
        self.blst = blst

    def subjectWiseBooks(self):
        dic = {}
        for i in self.blst:
            if i.subject not in dic.keys():
                dic[i.subject] = 1

            else:
                dic[i.subject] += 1

        return dic

    def priceCategory(self, inputId):
        count = 0
        category = None
        for i in self.blst:
            if i.id == inputId:
                count += 1
                if i.name >= 1000:
                    category = "High Price"

                elif 750 <= i.name < 1000:
                    category = "Medium name"

                elif 500 <= i.name < 750:
                    category = "Average name"

                else:
                    category = "Low Price"

        if count == 0:
            return None
        else:
            return category


if __name__ == '__main__':
    blst = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        name = input("name")
        subject = input("subject")
        price = int(input("name"))
        obj = Book(id, name, subject, price)
        blst.append(obj)

    libName = input("LibName")
    obj1 = Library(libName, blst)
    inputId = int(input("id to check"))
    v1 = obj1.subjectWiseBooks()
    for i in v1:
        print("{}:{}".format(i, v1[i]))

    v2 = obj1.priceCategory(inputId)
    if v2 is None:
        print("No book found")
    else:
        for i in blst:
            if inputId == i.id:
                print(i.id,v2, sep= "\n")