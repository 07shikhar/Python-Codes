class Question:
    def __init__(self, id, marked, score, status="Not Answered"):
        self.id = id
        self.marked = marked
        self.score = score
        self.status = status


class Student:
    def __init__(self, rid, qlst):
        self.rid = rid
        self.qlst = qlst

    def evaluateQuestions(self, answerKey):
        count1 = 0
        count2 = 0
        for i in self.qlst:
            for key in answerKey.keys():
                if i.id == key:
                    # for value in answerKey.values():
                    if i.marked == answerKey[key]:  # or if i.marked == value
                        i.status = "Correct"
                        count1 += 1
                    elif i.marked != answerKey[key]:
                        i.status = "Incorrect"
                        count2 += 1
        return count1, count2

    def findGrade(self):
        totalScore = 0
        grade = None
        for i in self.qlst:
            if i.status == "Correct":
                totalScore += i.score

        if totalScore >= 80:
            grade = 'A'

        elif 70 <= totalScore < 80:
            grade = 'B'

        elif 60 <= totalScore < 70:
            grade = 'C'

        else:
            grade = 'F'

        return grade


if __name__ == '__main__':
    qlst = []
    n = int(input("range"))
    for i in range(n):
        id = int(input("id"))
        marked = int(input("marked"))
        score = int(input("score"))
        obj = Question(id, marked, score)
        qlst.append(obj)

    answerKey = {}
    m = int(input("range for dic"))
    for i in range(m):
        qid = int(input("id"))
        correctoption = int(input("Correct"))
        answerKey[qid] = correctoption

    rid = int(input("rid"))
    obj2 = Student(rid, qlst)
    v1 = obj2.evaluateQuestions(answerKey)
    print("Correct are {} and Incorrect are {}".format(v1[0], v1[1]))
    for i in qlst:
        print(i.id, i.status)

    v1 = obj2.findGrade()
    print(v1)
