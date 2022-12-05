from PyQt5.QtWidgets import *
import QToolButton

class App(QMainWindow):
    def __init__(self): 
        super().__init__() 
        
        self.title = "계산기"
        self.setWindowTitle(self.title)
        self.left = 100
        self.top = 200
        self.width = 400
        self.height = 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    calc = App()
    app.exec_()