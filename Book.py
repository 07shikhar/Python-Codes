class Book:
    def __init__(self, bookid, bookTitle, authorName, bookType, bookPrice, status):
        self.bookid = bookid
        self.bookTitle = bookTitle
        self.authorName = authorName
        self.bookType = bookType
        self.bookPrice = bookPrice
        self.status = status


class Library:
    def __init__(self, lst):
        self.lst = lst

    def issuebook(self, btitle, btype):
        self.btitle = btitle
        self.btype = btype

        for i in self.lst:
            if btype.lower() == i.bookType.lower():
                if btitle.lower() == i.bookTitle.lower():

                    if i.status == "available":
                        i.status = "unavailable"

                if i.status == "unavailable":
                    return True

                else:
                    return False

    def costliestBook(self, inputAuthor):
        # self.inputAuthor = inputAuthor
        # dic = {}
        #
        # preresult = None

        olst = []

        for i in self.lst:
            if i.authorName == inputAuthor:
                olst.append(i)

        nw = max(olst, key=lambda x: x.bookPrice)
        return nw

        #     if i.authorName not in dic:
        #         dic[i.authorName] = [i.bookPrice]
        #     else:
        #         dic[i.authorName].append(i.bookPrice)
        #
        # for values in dic.values():
        #     for i in values:
        #
        #         if i > max:
        #
        #             max = i
        #             preresult = obj


if __name__ == "__main__":
    n = int(input("Enter length"))
    lst = []
    for i in range(n):
        bookid = int(input("Enter id"))
        bookTitle = input("Enter title")
        authorName = input("Enter book name")
        bookType = input("Enter book type")
        bookPrice = int(input("Enter book name"))
        status = input("Enter status")
        obj = Book(bookid, bookTitle, authorName, bookType, bookPrice, status)
        lst.append(obj)

    obj1 = Library(lst)

    btitle = input("Enter title")
    btype = input("Enter type")
    a = obj1.issuebook(btitle, btype)
    print(a)

    inputAuthor = input("Enter name of author")
    result = obj1.costliestBook(inputAuthor)
    if result is None:
        print("No book found")
    else:
        print(result.bookTitle)
