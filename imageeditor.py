#!/usr/bin/env python3

import os
from PIL import Image

class Location:
    LEFTTOP = 0
    RIGHTTOP = 1
    LEFTBUTTON = 2
    RIGHTBUTTON = 3
    TOP = 4
    BUTTON = 5
    CENTER = 6

class ImageEditor:
    image = None
    mark = None
    imageWidth = 0
    imageHeight = 0
    markWidth = 0
    markHeight = 0
    imagePath = None

    def makeMark(self, loc):
        markX = 0
        markY = 0
        if loc == Location.RIGHTTOP:
            markX = self.imageWidth - self.markWidth
        elif loc == Location.LEFTBUTTON:
            markY = self.imageHeight - self.markHeight
        elif loc == Location.RIGHTBUTTON:
            markX = self.imageWidth - self.markWidth
            markY = self.imageHeight - self.markHeight
        elif loc == Location.TOP:
            markX = (self.imageWidth - self.markWidth) / 2
        elif loc == Location.BUTTON:
            markX = (self.imageWidth - self.markWidth) / 2
            markY = self.imageHeight - self.markHeight
        else:
            markX = (self.imageWidth - self.markWidth) / 2
            markY = (self.imageHeight - self.markHeight) / 2
        self.image.paste(self.mark,(int(markX),int(markY)),self.mark.convert('RGBA'))
        pathSplited, suffix = os.path.splitext(self.imagePath)
        self.image.save(pathSplited + "_WMM" + suffix)
        print(pathSplited + "_WMM" + suffix)

    def openImage(self, path):
        self.image = Image.open(path)
        self.imageWidth, self.imageHeight = self.image.size
        self.imagePath = path
        print(path)
        print(self.image.format, self.image.size, self.image.mode)
        print("图片加载成功！")

    def openMark(self, path):
        self.mark = Image.open(path)
        self.markWidth, self.markHeight = self.mark.size
        print(path)
        print(self.mark.format, self.mark.size, self.mark.mode)
        print("水印加载成功！")


