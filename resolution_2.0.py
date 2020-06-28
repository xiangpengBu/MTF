# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resolution_2.0.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QMainWindow, QGraphicsPixmapItem, QGraphicsView, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import numpy as np
import os
import sys
import time
from PyQt5.QtGui import QPen, QBrush
from scipy import interpolate
from scipy.optimize import curve_fit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_3.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.pic_display)
        self.pushButton_2.clicked.connect(self.pic_capture)
        self.pushButton_5.clicked.connect(self.pic_fit)
        self.pushButton_4.clicked.connect(self.pic_clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "分辨力测试"))
        self.pushButton_3.setText(_translate("MainWindow", "读入"))
        self.pushButton_2.setText(_translate("MainWindow", "截取"))
        self.pushButton_5.setText(_translate("MainWindow", "拟合"))
        self.pushButton_4.setText(_translate("MainWindow", "复位"))
        self.pushButton.setText(_translate("MainWindow", "关闭"))


class PicShow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(PicShow, self).__init__(parent)
        #  self.pushButton.clicked.connect(pic_show.original_pic())
        self.setupUi(self)
        self.name1 = []
        self.name2 = []
        self.result = []
        self.result_1 = []
        self.a = []
        self.b = []
        # self.scene = QGraphicsScene()  # 创建场景
        # self.graphicsView.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        #
        # self.graphicsView.setSceneRect(0, 0, self.graphicsView.viewport().width(), self.graphicsView.height())
        # self.graphicsView.setScene(self.scene)

    def pic_display(self):

        # self.name1.append(float(self.lineEdit_2.text()))
        # text_0 = str(self.lineEdit.text())
        # text_2 = str(self.lineEdit_2.text())
        # text_3 = str(self.lineEdit_3.text())
        # path = text_0 + "/" + text_2 + "." + text_3
        file_name = QFileDialog.getOpenFileName(self, "Open File", "./", "All Files (*) ;;bmp (*.bmp)")
        path = file_name[0]
        (filepath, tempfilename) = os.path.split(path)
        (filename, extension) = os.path.splitext(tempfilename)

        if filename:
            # print(file_name)
            self.name1.append(float(filename))
            pic = cv2.imread(path)
            size = pic.shape
            img_s = cv2.resize(pic, (int(size[1] / 2), int(size[0] / 2)), interpolation=cv2.INTER_AREA)

            self.img_gray = cv2.cvtColor(img_s, cv2.COLOR_BGR2GRAY)  # 转为灰度图
            w, h = self.img_gray.shape[0:2]
            pic1 = cv2.cvtColor(self.img_gray, cv2.COLOR_BGR2RGB)  # 转换通道
            frame = QImage(pic1, h, w, h * 3, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
            self.scene = QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.graphicsView.setScene(self.scene)
            self.scene.mousePressEvent = self.myMousePressEvent
            # print(self.name1)
        else:
            self.textBrowser.append("please select the file")  # 在指定的区域显示提示信息
            self.cursot = self.textBrowser.textCursor()
            self.textBrowser.moveCursor(self.cursot.End)

    def myMousePressEvent(self, mouseEvent):

        point = str(mouseEvent.scenePos())
        # pen = QPen(QtCore.Qt.black)
        # brush = QBrush(QtCore.Qt.black)
        x = mouseEvent.scenePos().x()
        y = mouseEvent.scenePos().y()
        #
        # self.addEllipse(x, y, 4, 4, pen, brush)
        # print(x, y)
        self.a.append(int(x))
        self.b.append(int(y))
        self.textBrowser.append(point)  # 在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)

    def pic_capture(self):

        pixel_data = np.array(self.img_gray)
        # print (pixel_data)
        # print(self.a, self.b)
        # if self.a[0] >= self.a[1]:
        #     self.a[0], self.a[1] = self.a[1], self.a[0]
        if self.a[-2] >= self.a[-1]:
            self.a[-2], self.a[-1] = self.a[-1], self.a[-2]
        # if self.b[0] >= self.b[1]:
        #     self.b[0], self.b[1] = self.b[1], self.b[0]
        if self.b[-2] >= self.b[-1]:
            self.b[-2], self.b[-1] = self.b[-1], self.b[-2]

        # data_1 = pixel_data[self.b[0]:self.b[1], self.a[0]:self.a[1]]
        data_2 = pixel_data[self.b[-2]:self.b[-1], self.a[-2]:self.a[-1]]
        # print(data_1, data_2)
        # print(self.a[0], self.a[1], self.a[-1], self.a[-2], self.b[0], self.b[1], self.b[-2], self.b[-1])
        # data_1_ave = round(np.mean(data_1), 1)
        # data_2_ave = round(np.mean(data_2), 1)
        # print(data_1_ave, data_2_ave)
        # dev = round(abs(data_2_ave - data_1_ave), 1)
        dev = round((np.max(data_2) - np.min(data_2)), 1)
        self.textBrowser.append(str(dev))  # 在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)

        self.result.append(dev)
        self.a = []
        self.b = []



    def pic_fit(self):
        # # print(self.result)
        # for j in self.result:
        #     j = float((j - np.min(self.result)) / (np.max(self.result) - np.min(self.result)))
        #     self.result_1.append(round(j, 3))
        # print(self.result_1)
        for i in self.name1:
            i = round((0.5 / i), 1)
            self.name2.append(i)
        x = np.array(self.name2)
        y = np.array(self.result)
        # xnew = np.linspace(x.min(), x.max(), 300)
        # power_smooth = spline(x, y, xnew)
        # print(x, y)
        # xnew = np.linspace(np.min(x), np.max(x), 2000)

        # 实现函数
        # func = interpolate.interp1d(x, y, kind='quadratic')

        # x.sort(reverse=True)
        # print(x)
        popt, pcov = curve_fit(self.func, x, y)
        # print(popt)
        # a = popt[0]
        popt[1] = np.min(x)
        # u = popt[1]
        # sig = popt[2]
        curvex = np.linspace(np.min(x), np.max(x), 100)
        # print(curvex)
        yvals = self.func(curvex, *popt)  # 拟合y值
        # print(yvals)

        for i in yvals:
            i = (i - np.min(yvals)) / (np.max(yvals) - np.min(yvals))
            self.result_1.append(round(i, 4))

        # ynew = func(xnew)
        # print(xnew, ynew)
        # plt.plot(xnew, ynew)
        plt.xlim(np.min(x), np.max(x))
        plt.title("MTF")
        plt.xlabel('(LP/1000)/mm')
        plt.ylabel('y')
        plt.plot(curvex, self.result_1)
        plt.show()
        self.result = []
        self.result_1 = []
        self.name1 = []
        self.name2 = []

    def pic_clear(self):

        self.textBrowser.clear()

    def func(self, x, a, u, sig, offset):
        return a * (np.exp(-(x - u) ** 2 / (2 * sig ** 2))) + offset


def main():

    app = QApplication(sys.argv)
    pic = PicShow()
    pic.show()
    app.exec_()


if __name__ == '__main__':

    main()