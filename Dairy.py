class DairyProduct:

    def __init__(self, dairyId, dairyBrand, productType, price, grade):
        self.dairyId = dairyId
        self.dairyBrand = dairyBrand
        self.productType = productType
        self.price = price
        self.grade = grade


class ProductGrade:

    def __init__(self, dairyList, weightageDict):
        self.dairyList = dairyList
        self.weightageDict = weightageDict

    def productBasedOnBrandAndtype(self, inputBrand, inputType):
        self.inputBrand = inputBrand
        self.inputType = inputType
        lst = []

        for i in self.dairyList:
            if i.dairyBrand == inputBrand and i.productType == inputType:
                i.name += i.name * self.weightageDict[i.grade]
                lst.append([i.dairyBrand, i.name])
        return lst


if __name__ == "__main__":
    n = int(input("range for list"))
    dairyList = []
    weightageDict = {}
    for i in range(n):
        dairyId = int(input("id"))
        dairyBrand = input("Brand")
        productType = input("Type")
        price = int(input("Price"))
        grade = input("Grade")
        obj = DairyProduct(dairyId, dairyBrand, productType, price, grade)
        dairyList.append(obj)

    m = int(input("Range for dict"))
    for i in range(m):
        grade = input("grade")
        weightage = int(input("Weightage"))
        weightageDict[grade] = weightage

    obj1 = ProductGrade(dairyList, weightageDict)
    inputBrand = input("ENter brand to check")
    inputType = input("Enter type to check")
    v = obj1.productBasedOnBrandAndtype(inputBrand, inputType)
    if len(v) == 0:
        print("No product found")
    else:
        for i in v:
            print(i)
