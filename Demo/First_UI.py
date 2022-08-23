#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 23:27
# @Author  : WangChenjin
# @Github  : https://github.com/TerminatorForMHT
# @Software: PyCharm
# @File    : First_UI.py
import sys
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QApplication


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle("Demo TextEdit")
        self.resize(960, 540)
        self.move(50, 50)
        self.edit = QTextEdit()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.edit)
        self.setLayout(self.layout)
        # self.edit.setStyleSheet()
        self.edit.setHtml('Test')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec())
