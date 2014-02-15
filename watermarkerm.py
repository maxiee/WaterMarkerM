#!/usr/bin/env python3

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        layoutImage = QHBoxLayout()
        layoutWater = QHBoxLayout()
        layoutLocGen = QHBoxLayout()
        layoutMain = QVBoxLayout()
        #layoutImage布局
        btnImageOpen = QPushButton("打开图片",self)
        labelImageName = QLabel()
        layoutImage.addWidget(btnImageOpen)
        layoutImage.addWidget(labelImageName)
        #layoutWater布局
        btnWaterOpen = QPushButton("打开水印",self)
        labelWaterName = QLabel()
        layoutWater.addWidget(btnWaterOpen)
        layoutWater.addWidget(labelWaterName)
        #layoutLocGen布局
        labelLocation = QLabel("水印位置:")
        comboLocation = QComboBox()
        comboLocation.addItems(("左上","右上","左下","右下","上方","下方","中央"))
        btnGenerate = QPushButton("生成",self)
        layoutLocGen.addWidget(labelLocation)
        layoutLocGen.addWidget(comboLocation)
        layoutLocGen.addWidget(btnGenerate)
        #layoutMain布局
        layoutMain.addLayout(layoutImage)
        layoutMain.addLayout(layoutWater)
        layoutMain.addLayout(layoutLocGen)
        self.setLayout(layoutMain)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setApplicationName("WaterMarkerM")
    w = MainWindow()
    w.show()
    App.exec_()
