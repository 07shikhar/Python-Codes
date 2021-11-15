# finallist=[]
# class Boutique:
#     def __init__(self,boutiqueid,boutiquename,boutiquetype,boutiquerating,points):
#         self.boutiqueid=boutiqueid
#         self.boutiquename=boutiquename
#         self.boutiquetype=boutiquetype
#         self.boutiquerating=boutiquerating
#         self.points=points
# class OnlineBoutique:
#     def __init__(self,p):
#         self.p=p
#     def getBoutique(self,lowrating,highrating,point,type):
#         for i in self.p:
#             if type.lower()==i.boutiquetype.lower():
#                 if lowrating<=i.boutiquerating and highrating>=i.boutiquerating:
#                     r=0
#                     r=point+i.points
#                     finallist.append([i.boutiqueid,i.boutiquename,r])
#         if len(finallist)>=1:
#             finallist.sort(reverse=True)
#             for i in range(len(finallist)):
#                 print(finallist[i][0],finallist[i][1],finallist[i][2])
#         else:
#             print("No boutique found")
#
# if __name__=="__main__":
#     n=int(input())
#     p=[]
#     for i in range(n):
#         boutiqueid=int(input())
#         boutiquename=str(input())
#         boutiquetype=str(input())
#         boutiquerating=float(input())
#         points=int(input())
#         obj=Boutique(boutiqueid,boutiquename,boutiquetype,boutiquerating,points)
#         p.append(obj)
#     lowrating=float(input())
#     highrating=float(input())
#     point=int(input())
#     type=str(input())
#     obj1=OnlineBoutique(p)
#     obj1.getBoutique(lowrating,highrating,point,type)
p = []


class Boutique:
    def __init__(self, name, btype, price, origin):
        self.name = name
        self.btype = btype
        self.price = price
        self.origin = origin


class Online:

    def __init__(self, dic):
        self.dic = dic

    def getitems(self, rest, itype):
        for keys, values in dic.items():
            if itype == t:
                for i in rest:
                    if pr > 40:
                        p.append(n)


                # m = dic.get(itype)
                # p.append(n)
                # p.append(pr)
                # for i in values:
                #     p.append(n)
                #     print(p)

        else:
            pass


if __name__ == "__main__":
    n = int(input("Enter length"))
    dic = {}
    rest = []
    for i in range(n):
        n = input("Enter name")
        t = input("Enter type")
        pr = int(input("Enter name"))
        o = input("Enter origin")
        obj = Boutique(n, t, pr, o)
        rest.append([n, t, pr, o])

        if t in dic:
            dic[t].append(n)


        else:
            dic[t] = [n]
    print(dic)

    obj2 = Online(dic)
    q = input('Enter type to search')
    obj2.getitems(rest, q)
    if len(p) == 0:
        print("no value")
    else:
        print(p)
