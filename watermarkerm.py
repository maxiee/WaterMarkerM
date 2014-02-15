#!/usr/bin/env python3

import sys,os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from imageeditor import ImageEditor, Location

class MainWindow(QWidget):
    imageEditor = ImageEditor()

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        layoutImage = QHBoxLayout()
        layoutWater = QHBoxLayout()
        layoutLocGen = QHBoxLayout()
        layoutMain = QVBoxLayout()
        #layoutImage布局
        btnImageOpen = QPushButton("打开图片",self)
        self.labelImageName = QLabel()
        layoutImage.addWidget(btnImageOpen)
        layoutImage.addWidget(self.labelImageName)
        #layoutWater布局
        btnWaterOpen = QPushButton("打开水印",self)
        self.labelWaterName = QLabel()
        layoutWater.addWidget(btnWaterOpen)
        layoutWater.addWidget(self.labelWaterName)
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
        #链接信号槽
        self.connect(btnImageOpen, SIGNAL("clicked()"), self.onImageOpenClicked)
        self.connect(btnWaterOpen, SIGNAL("clicked()"), self.onWaterOpenClicked)
        self.connect(btnGenerate, SIGNAL("clicked()"), self.onGenerateClicked)

    #定义槽函数
    @pyqtSlot()
    def onImageOpenClicked(self):
        path = QFileDialog.getOpenFileName(self, "打开图片", "~/")
        self.labelImageName.setText(os.path.split(path)[1])
        self.imageEditor.openImage(path)

    @pyqtSlot()
    def onWaterOpenClicked(self):
        path = QFileDialog.getOpenFileName(self, "打开水印", "~/")
        self.labelWaterName.setText(os.path.split(path)[1])
        self.imageEditor.openMark(path)

    @pyqtSlot()
    def onGenerateClicked(self):
        self.imageEditor.makeMark(Location.RIGHTBUTTON)
        print("成功！")

if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setApplicationName("WaterMarkerM")
    w = MainWindow()
    w.show()
    App.exec_()
