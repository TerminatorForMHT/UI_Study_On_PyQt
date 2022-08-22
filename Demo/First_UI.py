#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 23:27
# @Author  : WangChenjin
# @Github  : https://github.com/TerminatorForMHT
# @Software: PyCharm
# @File    : First_UI.py

import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    first_app = QApplication(sys.argv)
    first_window = QWidget()
    first_window.resize(1920, 1280)
    first_window.move(50, 50)
    first_window.setWindowTitle('First App Window')
    first_window.show()
    sys.exit(first_app.exec())
