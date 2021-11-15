class Passenger:
    def __init__(self, name, age, distance):
        self.name = name
        self.age = age
        self.distance = distance


def calculateFare(plst, perkm):
    fare1 = 0
    fare2 = 0
    fare3 = 0

    for i in plst:
        if i.age <= 12 or i.age >= 60:
            fare1 += i.distance * perkm

        elif i.age >= 21 or i.age <= 59:
            fare2 += 0.12 + (i.distance * perkm)

        elif i.age > 12 or i.age <= 20:
            fare3 += 0.10 + (i.distance * perkm)

    totalFare = fare1 + fare2 + fare3
    return totalFare


def count(plst):
    count1 = 0
    for i in plst:
        if i.age >= 60 or i.age < 12:
            count1 += 1
    return count1


if __name__ == '__main__':
    plst = []
    n = int(input("range"))
    for i in range(n):
        name = input("name")
        age = int(input("age"))
        distance = int(input("distance"))
        obj = Passenger(name, age, distance)
        plst.append(obj)

    perkm = int(input("perkm"))

    r1 = calculateFare(plst, perkm)
    print(r1)
    r2 = count(plst)
    print(r2)
