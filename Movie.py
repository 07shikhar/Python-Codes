class Movie:
    def __init__(self, movie_id, movie_name, ticket_cost, category='Default'):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.ticket_cost = ticket_cost
        self.category = category

    def assignPriceCategory(self):
        if 0 <= self.ticket_cost <= 150:
            self.category = 'General'

        if 150 < self.ticket_cost <= 250:
            self.category = 'Silver'

        if 250 < self.ticket_cost <= 350:
            self.category = 'Gold'

        if self.ticket_cost > 350:
            self.category = 'Platinum'


class MovieTicket:
    def __init__(self, customer_name, movie_name, viewerCount, totalTicketCost=0):
        self.customer_name = customer_name
        self.movie_name = movie_name
        self.viewerCount = viewerCount
        self.totalTicketCost = totalTicketCost


def catWiseCount(mObj):
    dic = {}
    for i in mObj:
        i.assignPriceCategory()
        if i.category not in dic.keys():
            dic[i.category] = 1
        else:
            dic[i.category] += 1
    return dic


def bookMovieTickcet(mObj, obj2):
    lst = []
    for i in mObj:
        if i.movie_name == obj2.movie_name:
            obj2.totalTicketCost = i.ticket_cost * obj2.viewerCount
            # lst.append([obj2.customer_name, obj2.totalTicketCost])
            lst.append(obj2)
    return lst


if __name__ == '__main__':
    mObj = []
    n = int(input())
    for i in range(n):
        id = int(input("id"))
        mname = input("movie")
        cost = int(input("cost"))
        obj = Movie(id, mname, cost)
        mObj.append(obj)

    cname = input("cname")
    mname = input("mc")
    vcount = int(input("vc"))
    obj2 = MovieTicket(cname, mname, vcount)

    v = catWiseCount(mObj)
    for i in v:
        print('{}:{}'.format(i, v[i]))

    v2 = bookMovieTickcet(mObj, obj2)

    for i in v2:
        # for j in i:
        #     print(j, end=" ")
        print(i.movie_name,i.totalTicketCost)
