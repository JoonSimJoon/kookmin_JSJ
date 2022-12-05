import random

# namedb명단에서 랜덤으로 8명 뽑음
def pickStudent(list,num):
    pickStudent = random.sample(list, num)
    return pickStudent

class DataBase:
    def __init__(self):
        self.namedb = []
        self.scoredb = 0
        self.teachersays = []
        self.student_button=[]
        self.currentstage = -1
        self.pickStudent=[]

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
        self.teachersays = pickStudent(self.namedb,5)
        self.currentstage = 0
    
    def getTeachersays(self):
        name = self.teachersays[self.currentstage]
        self.currentstage+=1
        
        return name
    def setStudent_button(self):
        self.student_button = pickStudent(self.namedb,8)
    
    def getStudent_button(self):
        return self.student_button




