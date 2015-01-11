#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import service
import sys
from PyQt4.QtCore import SIGNAL, QObject
from PyQt4.QtGui import QPushButton, QGroupBox, QRadioButton
from PyQt4.QtGui import QMainWindow, QApplication, QWidget, QVBoxLayout


class AppWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("add a word to Lingualeo")
        self.gb = QGroupBox("Variants")
        email = config.auth.get('email')
        password = config.auth.get('password')
        self.lingualeo = service.Lingualeo(email, password)
        self.lingualeo.auth()
        translates = self.get_translates()
        self.rbs = []
        i = 0
        for each in translates["twords"]:
            self.rbs.append(
                QRadioButton(
                    each[0].decode('utf8'), self.gb
                )
            )
            self.rbs[i].setDisabled(each[1])
            i += 1
        self.rbs[0].setChecked(1)

        self.main_widget = QWidget(self)
        main_layout = QVBoxLayout(self.main_widget)
        for each in self.rbs:
            main_layout.addWidget(each)

        self.addb = QPushButton()
        self.addb.setObjectName("add")
        self.addb.setText("Add")
        main_layout.addWidget(self.addb)
        self.setCentralWidget(self.main_widget)

        QObject.connect(self.addb, SIGNAL("clicked()"), self.add_word)

    def get_translates(self):
        word = sys.argv[1]
        self.word = word.lower()
        translate = self.lingualeo.get_translates(self.word)
        return translate

    def add_word(self):
        for each in self.rbs:
            if each.isChecked():
                print(each.text().toUtf8())
                self.lingualeo.add_word(self.word, each.text().toUtf8())


app = QApplication(sys.argv)
aw = AppWindow()
aw.show()
app.exec_()
