import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      btnAdmin = QPushButton('관리자로 로그인', self)
      btnAdmin.move(400,350)
      btnAdmin.resize(200,50)
      #btnAdmin.clicked.connect(QCoreApplication.instance().quit)
      btnStaff = QPushButton('직원으로 로그인', self)
      btnStaff.move(400,420)
      btnStaff.resize(200,50)
      self.setWindowTitle('RASZAS')
      self.setWindowIcon(QIcon('RASZASIcon.JPG'))
      self.setGeometry(300, 300, 300, 200)
      self.resize(1000,500)
      
      self.show()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())