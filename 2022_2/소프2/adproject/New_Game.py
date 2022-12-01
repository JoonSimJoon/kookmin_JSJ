from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from DataBase import DataBase
class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.DB = DataBase()
        self.resize(420, 500)
        self.setWindowTitle("MainWindow")

        self.centralwidget = QWidget()

        self.StudentList = QTextEdit(self.centralwidget)  # 학생명단 출력창
        self.StudentList.setReadOnly(True)  # 글자 입력 못하게 바꿈, 출력만 하게
        self.StudentList.setGeometry(QRect(10, 310, 401, 141))

        self.Input = QLineEdit(self.centralwidget)  # 학생 이름 추가 입력창
        self.Input.setGeometry(QRect(10, 270, 191, 20))  # x축, y축 -> 위치/ 가로, 세로

        addButton = QPushButton(self.centralwidget)
        addButton.setGeometry(QRect(210, 270, 41, 23))
        addButton.setText("Add") # add 인원
        addButton.clicked.connect(self.addbuttonClicked)

        delButton = QPushButton(self.centralwidget)
        delButton.setGeometry(QRect(255, 270, 41, 23))
        delButton.setText("Del") # del 해당이름
        delButton.clicked.connect(self.delbuttonClicked)

        # self.show()

        #이 grid 뭔지 모르겠음
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QRect(10, 110, 401, 141))

        gridLayout = QGridLayout(self.gridLayoutWidget)
        gridLayout.setContentsMargins(0, 0, 0, 0)

        #self.StudentButtons 
        for i in range(8):
            new_button = QPushButton(self.gridLayoutWidget)
            new_button.setText(str(i+1))
            gridLayout.addWidget(new_button, int(i/4), i%4, 1, 1)


        Student_NULL = QPushButton(self.gridLayoutWidget)
        Student_NULL.setText("X")         #호명한 학생이 없는 경우
        gridLayout.addWidget(Student_NULL, 2, 3, 1, 1)

        StartButton = QPushButton(self.gridLayoutWidget)
        gridLayout.addWidget(StartButton, 3, 0, 1, 1)
        StartButton.setText("Game Start!")
        StartButton.clicked.connect(self.startbuttonClicked)

        SurrenderButton = QPushButton(self.gridLayoutWidget)
        SurrenderButton.setText("Surrender")
        gridLayout.addWidget(SurrenderButton, 3, 1, 1, 1)

        self.TeacherSays = QTextEdit(self.centralwidget)
        self.TeacherSays.setReadOnly(True) #글자 입력 못하게 바꿈, 출력만 하게
        self.TeacherSays.setGeometry(QRect(129, 30, 161, 51))  # 선생님 호명

        self.Left_Time = QProgressBar(self.centralwidget)
        self.Left_Time.setGeometry(QRect(300, 40, 111, 23))
        self.Left_Time.setProperty("value", 100)  # 배터리=남은시간

        Score_label = QLabel(self.centralwidget)
        Score_label.setText("Score:")
        Score_label.setGeometry(QRect(320, 270,50, 21))

        self.Score = QLabel(self.centralwidget)
        self.Score.setText("0")
        self.Score.setGeometry(QRect(390, 270, 10, 20))
    

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar()
        self.menubar.setGeometry(QRect(0, 0, 420, 21))
        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

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