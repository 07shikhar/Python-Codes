class College:
    def __init__(self, id, name, city, rating):
        self.id = id
        self.name = name
        self.city = city
        self.rating = rating


class University:
    def __init__(self, universityName, collegeCollection):
        self.universityName = universityName
        self.collegeCollection = collegeCollection

    def findCollegeByCity(self, iCity):
        lst = []
        for i in self.collegeCollection:
            if i.city.lower() == iCity.lower():
                lst.append(i)

        if len(lst) == 0:
            return None
        else:
            return lst

    def sortCollegeByRating(self):
        x = sorted(self.collegeCollection, key=lambda i: i.rating)

        if len(x) == 0:
            return None
        else:
            return x


if __name__ == '__main__':
    collegeCollection = []
    n = int(input())
    for i in range(n):
        id = int(input())
        name = input()
        city = input()
        rating = float(input())
        obj = College(id, name, city, rating)
        collegeCollection.append(obj)

    obj1 = University("abc", collegeCollection)
    iCity = input()
    v1 = obj1.findCollegeByCity(iCity)
    v2 = obj1.sortCollegeByRating()
    if v1 is None:
        print("No data found")
    else:
        for i in v1:
            print(i.id, i.name, i.city, i.rating, sep="\n")

    if v2 is None:
        print("No data found")
    else:
        for i in v2:
            print(i.id)
