from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from DataBase import DataBase
class Ui_MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.DB = DataBase()
        self.MainWindow.setObjectName("self.MainWindow")
        self.MainWindow.resize(420, 500)

        self.centralwidget = QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.StudentList = QTextEdit(self.centralwidget)  # 학생명단 출력창
        self.StudentList.setReadOnly(True)  # 글자 입력 못하게 바꿈, 출력만 하게
        self.StudentList.setGeometry(QRect(10, 310, 401, 141))
        self.StudentList.setObjectName("StudentList")

        self.Input = QLineEdit(self.centralwidget)  # 학생 이름 추가 입력창
        self.Input.setGeometry(QRect(10, 270, 191, 20))  # x축, y축 -> 위치/ 가로, 세로
        self.Input.setObjectName("Input")

        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setGeometry(QRect(210, 270, 41, 23))
        self.addButton.setObjectName("addButton")  # add 인원
        self.addButton.clicked.connect(self.addbuttonClicked)

        self.delButton = QPushButton(self.centralwidget)
        self.delButton.setGeometry(QRect(255, 270, 41, 23))
        self.delButton.setObjectName("delButton")  # del 해당이름
        self.delButton.clicked.connect(self.delbuttonClicked)

        # self.show()

        #이 grid 뭔지 모르겠음
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QRect(10, 110, 401, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")  #

        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.Student6 = QPushButton(self.gridLayoutWidget)
        self.Student6.setObjectName("Student6")
        self.gridLayout.addWidget(self.Student6, 1, 1, 1, 1)
        self.Student2 = QPushButton(self.gridLayoutWidget)
        self.Student2.setObjectName("Student2")
        self.gridLayout.addWidget(self.Student2, 0, 1, 1, 1)
        self.Student8 = QPushButton(self.gridLayoutWidget)
        self.Student8.setObjectName("Student8")
        self.gridLayout.addWidget(self.Student8, 1, 3, 1, 1)
        self.Student4 = QPushButton(self.gridLayoutWidget)
        self.Student4.setObjectName("Student4")
        self.gridLayout.addWidget(self.Student4, 0, 3, 1, 1)
        self.Student7 = QPushButton(self.gridLayoutWidget)
        self.Student7.setObjectName("Student7")
        self.gridLayout.addWidget(self.Student7, 1, 2, 1, 1)
        self.Student3 = QPushButton(self.gridLayoutWidget)
        self.Student3.setObjectName("Student3")
        self.gridLayout.addWidget(self.Student3, 0, 2, 1, 1)
        self.Student5 = QPushButton(self.gridLayoutWidget)
        self.Student5.setObjectName("Student5")
        self.gridLayout.addWidget(self.Student5, 1, 0, 1, 1)
        self.Student1 = QPushButton(self.gridLayoutWidget)
        self.Student1.setObjectName("Student1")
        self.gridLayout.addWidget(self.Student1, 0, 0, 1, 1)
        self.Student_NULL = QPushButton(self.gridLayoutWidget)
        self.Student_NULL.setObjectName("Student_NULL")
        self.gridLayout.addWidget(self.Student_NULL, 2, 3, 1, 1)

        self.StartButton = QPushButton(self.gridLayoutWidget)
        self.StartButton.setObjectName("StartButton")
        self.gridLayout.addWidget(self.StartButton, 3, 0, 1, 1)
        self.StartButton.clicked.connect(self.startbuttonClicked)
        self.SurrenderButton = QPushButton(self.gridLayoutWidget)
        self.SurrenderButton.setObjectName("SurrenderButton")
        self.gridLayout.addWidget(self.SurrenderButton, 3, 1, 1, 1)

        self.TeacherSays = QTextEdit(self.centralwidget)
        self.TeacherSays.setReadOnly(True) #글자 입력 못하게 바꿈, 출력만 하게
        self.TeacherSays.setGeometry(QRect(129, 30, 161, 51))  # 선생님 호명
        self.TeacherSays.setObjectName("TeacherSays")

        self.Left_Time = QProgressBar(self.centralwidget)
        self.Left_Time.setGeometry(QRect(300, 40, 111, 23))
        self.Left_Time.setProperty("value", 100)
        self.Left_Time.setObjectName("Left_Time")  # 배터리=남은시간

        self.Score_label = QLabel(self.centralwidget)
        self.Score_label.setGeometry(QRect(300, 270, 31, 21))
        self.Score_label.setObjectName("Score_label")

        self.Score = QLabel(self.centralwidget)
        self.Score.setGeometry(QRect(370, 270, 10, 20))
        self.Score.setObjectName("Score")
    

        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.MainWindow.setWindowTitle("MainWindow")
        self.Student6.setText( "6")
        self.Student2.setText( "2")
        self.Student8.setText("8")
        self.Student4.setText("4")
        self.Student7.setText("7")
        self.Student3.setText("3")
        self.Student5.setText("5")
        self.Student1.setText("1")
        self.Student_NULL.setText("X") #호명한 학생이 없는 경우
        self.StartButton.setText("Game Start!")
        self.SurrenderButton.setText("Surrender")
        self.Score_label.setText("Score:")
        self.Score.setText("0")
        self.addButton.setText("Add")
        self.delButton.setText("Del")
        

        QMetaObject.connectSlotsByName(self.MainWindow)

        #score 비교시 Score_label ==5?이런식? 이거 어케함
        
    def showStudentList(self):
        self.StudentList.clear()
        self.StudentList.append(self.DB.getstudentlist())

    def addbuttonClicked(self):
        text = self.Input.text()
        text_ = text.split() # -> 이름 여러개 들어왔을 때
        for i in text_:
            self.DB.addstudent(i)
        self.showStudentList()
        self.Input.clear()

    def delbuttonClicked(self):
        self.DB.deletestudent(self.Input.text())
        self.showStudentList()
        self.Input.clear()

    def showTeacherSays(self):
        self.TeacherSays.clear()
        name = self.DB.setteachersays()
        self.TeacherSays.append(name)
        self.TeacherSays.setAlignment(Qt.AlignCenter)

    def startbuttonClicked(self):
        self.showTeacherSays()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())