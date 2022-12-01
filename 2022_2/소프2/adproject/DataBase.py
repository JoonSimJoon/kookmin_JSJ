import random

class DataBase:
    def __init__(self):
        self.namedb = []
        self.scoredb = 0
        self.teachersays = []
        self.currentstage = -1

    def getstudentlist(self):
        studentlist = ""
        for i in self.namedb:
            studentlist = studentlist + " " + i
        return studentlist

    def addstudent(self, studentname):
        self.namedb.append(studentname)

    def deletestudent(self, studentname):
        for i in self.namedb:
            if i == studentname:
                self.namedb.remove(i)

    def setteachersays(self):
        self.teachersays.append(random.choice(self.namedb))
        self.currentstage += 1
        return self.teachersays[self.currentstage]
