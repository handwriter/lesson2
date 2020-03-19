import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from design import Ui_Form



class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.printer)

    def printer(self):
        text = ', '.join([self.buttonGroup.checkedButton().text(), self.buttonGroup_2.checkedButton().text(),
                          self.buttonGroup_3.checkedButton().text()])
        self.label.setText(text)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
