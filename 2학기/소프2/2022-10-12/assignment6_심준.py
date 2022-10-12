from audioop import add, reverse
import pickle #package import
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        #self.resize(600,400)
        layout = QVBoxLayout()

        Hlayout1 = QHBoxLayout()
        name_label = QLabel("Name: ")
        self.name_line = QLineEdit("",self)
        age_label = QLabel("Age: ")
        self.age_line = QLineEdit("",self)
        score_label = QLabel("Score: ")
        self.score_line = QLineEdit("",self)
        Hlayout1.addWidget(name_label)
        Hlayout1.addWidget(self.name_line)
        Hlayout1.addWidget(age_label)
        Hlayout1.addWidget(self.age_line)
        Hlayout1.addWidget(score_label)
        Hlayout1.addWidget(self.score_line)
        
        layout.addLayout(Hlayout1)

        Hlayout2 = QHBoxLayout()
        amount_label = QLabel("Amount: ")
        self.amount_line = QLineEdit("",self)
        key_label = QLabel("Key: ")
        self.key_combobox = QComboBox(self)
        self.key_combobox.addItem("Name")
        self.key_combobox.addItem("Score")
        self.key_combobox.addItem("Age")
        Hlayout2.addStretch(1)
        Hlayout2.addWidget(amount_label)
        Hlayout2.addWidget(self.amount_line)
        Hlayout2.addWidget(key_label)
        Hlayout2.addWidget(self.key_combobox)
        
        layout.addLayout(Hlayout2)

        Hlayout3 = QHBoxLayout()
        add_button = QPushButton("Add",self)
        add_button.clicked.connect(self.addquery)
        del_button = QPushButton("Del",self)
        del_button.clicked.connect(self.delquery)
        find_button = QPushButton("Find",self)
        find_button.clicked.connect(self.findquery)
        inc_button = QPushButton("Inc",self)
        inc_button.clicked.connect(self.incquery)
        show_button = QPushButton("Show",self)
        show_button.clicked.connect(self.showScoreDB)
        Hlayout3.addStretch(1)
        Hlayout3.addWidget(add_button)
        Hlayout3.addWidget(del_button)
        Hlayout3.addWidget(find_button)
        Hlayout3.addWidget(inc_button)
        Hlayout3.addWidget(show_button)
        
        layout.addLayout(Hlayout3)

        Vlayout1 = QVBoxLayout()
        result_label = QLabel("Result:")
        self.result_text = QTextEdit(self)
        Vlayout1.addWidget(result_label)
        Vlayout1.addWidget(self.result_text)

        layout.addLayout(Vlayout1)

        self.setLayout(layout)
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return
        try:
            self.scoredb =  pickle.load(fH)
            for p in self.scoredb: #scdb 안에 있는 인자 하나하나씩 읽기
            #print(p)
                p['Age'] = int(p['Age']) #Age int로 형식 변환
                p['Score'] = int(p['Score']) #Sore int로 형식 변환
                #print(type(p['Name']),type(p['Age']),type(p['Score']))
                #self.result_text.insertPlainText("Age: " + p['Age'] + "\t" + "Name: " + p['Name'] + "\t" + "Score: " + p['Score'])
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        self.result_text.clear()
        for p in sorted(self.scoredb, key = lambda person:person[self.key_combobox.currentText()]): #scdb 안에 있는 인자 하나하나씩 읽기
            #print(p)
                self.result_text.insertPlainText("Age: " + str(p['Age']) + "\t" + "Name: " + p['Name'] + "\t\t" + "Score: " + str(p['Score']) + "\n")
    
    def addquery(self):
        record = {'Name': self.name_line.text(), 'Age':int(self.age_line.text()), 'Score':int(self.score_line.text())}
        self.scoredb+=[record]
        self.showScoreDB()

    def delquery(self):
        dellist = []
        for i in range(len(self.scoredb)): #scdb 안에 있는 인자 하나하나씩 읽기
            p = self.scoredb[i]   
            if p['Name'] == self.name_line.text(): # p안에 Name이라는 key의 value가 parse[1]과 일치한다면 삭제
                dellist.append(i)
                #self.scoredb.remove(p) #scdb 안에 있는 p라는 value 삭제   
        dellist.reverse()
        for i in dellist:
            self.scoredb.remove(self.scoredb[i])
        self.showScoreDB()

    def findquery(self):
        self.result_text.clear()
        for p in self.scoredb: #scdb 안에 있는 인자 하나하나씩 읽기
            if p['Name'] == self.name_line.text():
                self.result_text.insertPlainText("Age: " + str(p['Age']) + "\t" + "Name: " + p['Name'] + "\t\t" + "Score: " + str(p['Score']) + "\n")

    def incquery(self):
        for p in self.scoredb: #scdb 안에 있는 인자 하나하나씩 읽기
            if p['Name'] == self.name_line.text():
                p['Score']+=int(self.amount_line.text())
                if(p['Score']>100):
                    p['Score']=100
        self.showScoreDB()

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
