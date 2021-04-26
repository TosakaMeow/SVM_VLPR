# -*- coding: utf-8 -*-
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Recognition import PlateRecognition
import cv2
import sys, os, xlwt
import numpy as np
import Function


class Ui_MainWindow(object):

    def __init__(self):
        self.RowLength = 0
        self.Data = [['文件名称', '录入时间', '车牌号码', '车牌类型', '识别耗时', '车牌信息']]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1213, 670)
        MainWindow.setFixedSize(1213, 670)  # 设置窗体固定大小
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.enterTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.enterTimeLabel.setGeometry(QtCore.QRect(20, 200, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enterTimeLabel.setFont(font)
        self.enterTimeLabel.setObjectName("enterTimeLabel")
        self.enterTime = QtWidgets.QTextBrowser(self.centralwidget)
        self.enterTime.setGeometry(QtCore.QRect(100, 200, 256, 31))
        self.enterTime.setObjectName("enterTime")
        self.leaveTime = QtWidgets.QTextBrowser(self.centralwidget)
        self.leaveTime.setGeometry(QtCore.QRect(100, 250, 256, 31))
        self.leaveTime.setObjectName("leaveTime")
        self.leaveTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.leaveTimeLabel.setGeometry(QtCore.QRect(20, 250, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leaveTimeLabel.setFont(font)
        self.leaveTimeLabel.setObjectName("leaveTimeLabel")
        self.kinds = QtWidgets.QTextBrowser(self.centralwidget)
        self.kinds.setGeometry(QtCore.QRect(100, 300, 256, 31))
        self.kinds.setObjectName("kinds")
        self.kindsLabel = QtWidgets.QLabel(self.centralwidget)
        self.kindsLabel.setGeometry(QtCore.QRect(20, 300, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kindsLabel.setFont(font)
        self.kindsLabel.setObjectName("kindsLabel")
        self.cost = QtWidgets.QTextBrowser(self.centralwidget)
        self.cost.setGeometry(QtCore.QRect(100, 340, 256, 31))
        self.cost.setObjectName("cost")
        self.costLabel = QtWidgets.QLabel(self.centralwidget)
        self.costLabel.setGeometry(QtCore.QRect(20, 340, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.costLabel.setFont(font)
        self.costLabel.setObjectName("costLabel")
        self.parkingInfo = QtWidgets.QLabel(self.centralwidget)
        self.parkingInfo.setGeometry(QtCore.QRect(120, 140, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.parkingInfo.setFont(font)
        self.parkingInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.parkingInfo.setObjectName("parkingInfo")
        self.realTimeInfo = QtWidgets.QLabel(self.centralwidget)
        self.realTimeInfo.setGeometry(QtCore.QRect(120, 390, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.realTimeInfo.setFont(font)
        self.realTimeInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.realTimeInfo.setObjectName("realTimeInfo")
        self.parkingRemaining = QtWidgets.QTextBrowser(self.centralwidget)
        self.parkingRemaining.setGeometry(QtCore.QRect(100, 430, 256, 31))
        self.parkingRemaining.setObjectName("parkingRemaining")
        self.parkingRemainingLabel = QtWidgets.QLabel(self.centralwidget)
        self.parkingRemainingLabel.setGeometry(QtCore.QRect(20, 430, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parkingRemainingLabel.setFont(font)
        self.parkingRemainingLabel.setObjectName("parkingRemainingLabel")
        self.specialParking = QtWidgets.QTextBrowser(self.centralwidget)
        self.specialParking.setGeometry(QtCore.QRect(100, 480, 256, 31))
        self.specialParking.setObjectName("specialParking")
        self.specialparkingLabel = QtWidgets.QLabel(self.centralwidget)
        self.specialparkingLabel.setGeometry(QtCore.QRect(20, 480, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.specialparkingLabel.setFont(font)
        self.specialparkingLabel.setObjectName("specialparkingLabel")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(130, 530, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.refresh.setFont(font)
        self.refresh.setObjectName("refresh")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(690, 10, 511, 531))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 509, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_0 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_0.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_0.setFont(font)
        self.label_0.setObjectName("label_0")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 40, 481, 450))
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 10, 671, 130))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 669, 180))
        self.scrollAreaWidgetContents_1.setObjectName("scrollAreaWidgetContents_1")
        self.label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_1)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_1)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 651, 580))  # 581))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setColumnWidth(0, 140)  # 设置1列的宽度
        self.tableWidget.setColumnWidth(1, 130)  # 设置2列的宽度
        self.tableWidget.setColumnWidth(2, 65)  # 设置3列的宽度
        self.tableWidget.setColumnWidth(3, 75)  # 设置4列的宽度
        self.tableWidget.setColumnWidth(4, 65)  # 设置5列的宽度
        self.tableWidget.setColumnWidth(5, 174)  # 设置6列的宽度

        self.tableWidget.setHorizontalHeaderLabels(["图片名称", "录入时间", "识别耗时", "车牌号码", "车牌类型", "车牌信息"])
        self.tableWidget.setRowCount(self.RowLength)
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头)
        # self.tableWidget.setStyleSheet("selection-background-color:blue")
        # self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.raise_()
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_1)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(690, 510, 341, 131))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 339, 129))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 321, 81))
        self.label_3.setObjectName("label_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_4.setGeometry(QtCore.QRect(1040, 510, 161, 130))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 159, 130))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 50, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.__openimage)  # 设置点击事件
        self.pushButton_2.clicked.connect(self.__writeFiles)  # 设置点击事件
        self.refresh.clicked.connect(self.realTimeParking)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.ProjectPath = os.getcwd()  # 获取当前工程文件位置

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "智能停车场管理系统"))
        self.label_0.setText(_translate("MainWindow", "车辆抓拍："))
        self.label.setText(_translate("MainWindow", ""))
        self.label_1.setText(_translate("MainWindow", "识别结果："))
        self.label_2.setText(_translate("MainWindow", "车牌区域："))
        self.label_3.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "打开文件"))
        self.pushButton_2.setText(_translate("MainWindow", "导出数据"))
        self.label_4.setText(_translate("MainWindow", "命令："))
        self.enterTimeLabel.setText(_translate("MainWindow", "入场时间："))
        self.leaveTimeLabel.setText(_translate("MainWindow", "出场时间："))
        self.kindsLabel.setText(_translate("MainWindow", "车辆类型："))
        self.costLabel.setText(_translate("MainWindow", "计费："))
        self.parkingInfo.setText(_translate("MainWindow", "车辆停车信息"))
        self.realTimeInfo.setText(_translate("MainWindow", "停车场实时信息"))
        self.parkingRemainingLabel.setText(_translate("MainWindow", "车位数量："))
        self.specialparkingLabel.setText(_translate("MainWindow", "特殊车位："))
        self.refresh.setText(_translate("MainWindow", "刷新信息"))
        self.scrollAreaWidgetContents_1.show()

    # 识别
    def __vlpr(self, path):
        PR = PlateRecognition()
        result = PR.VLPR(path)
        return result

    def __show(self, result, FileName):
        # 显示表格
        self.RowLength = self.RowLength + 2
        if self.RowLength > 18:
            self.tableWidget.setColumnWidth(5, 157)
        self.tableWidget.setRowCount(self.RowLength)
        self.tableWidget.setItem(1, 0, QTableWidgetItem(FileName))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(result['InputTime']))
        self.tableWidget.setItem(1, 2, QTableWidgetItem(str(result['UseTime']) + '秒'))
        self.tableWidget.setItem(1, 3, QTableWidgetItem(result['Number']))
        self.tableWidget.setItem(1, 4, QTableWidgetItem(result['Type']))
        if result['Type'] == '蓝色牌照':
            self.tableWidget.item(1, 4).setBackground(QBrush(QColor(3, 128, 255)))
            self.kinds.setText("普通车")
            car_kinds = "普通车"
        elif result['Type'] == '绿色牌照':
            self.tableWidget.item(1, 4).setBackground(QBrush(QColor(98, 198, 148)))
            self.kinds.setText("新能源汽车")
            car_kinds = "新能源汽车"
        elif result['Type'] == '黄色牌照':
            self.tableWidget.item(1, 4).setBackground(QBrush(QColor(242, 202, 9)))
            self.kinds.setText("大型车")
            car_kinds = "大型车"
        self.tableWidget.setItem(1, 5, QTableWidgetItem(result['From']))

        # 显示识别到的车牌位置
        size = (int(self.label_3.width()), int(self.label_3.height()))
        shrink = cv2.resize(result['Picture'], size, interpolation=cv2.INTER_AREA)
        shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
        self.QtImg = QtGui.QImage(shrink[:], shrink.shape[1], shrink.shape[0], shrink.shape[1] * 3,
                                  QtGui.QImage.Format_RGB888)
        self.label_3.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))

        info = Function.enterStation(result['Number'], car_kinds)  # 登记入场信息
        if info == 0:
            localtime = time.asctime(time.localtime(time.time()))
            self.enterTime.setText(localtime)
            self.leaveTime.setText('进入停车场')
            self.cost.setText('0')
            message = Function.Diversion(car_kinds)
            message = '请前往 ' + message + ' 区进行停车'
            QMessageBox.information(None, "提示", message)  #

        else:
            localtime = time.asctime(time.localtime(time.time()))
            self.enterTime.setText(info[3])
            self.leaveTime.setText(localtime)
            a = info[0]
            a = int(a)
            b = time.asctime(time.localtime(time.time()))
            b = time.mktime(time.strptime(b, "%a %b %d %H:%M:%S %Y"))
            b = int(b)
            self.cost.setText(str((b - a) / 720))
            Function.collect(result['Number'], car_kinds, str((b - a)), cost=str((b - a) / 720))    # 离场汇总
            Function.deleteInfo(result['Number'])   # 删除临时表中的信息

    def __writexls(self, DATA, path):  # 保存数据
        wb = xlwt.Workbook();
        ws = wb.add_sheet('Data');
        # DATA.insert(0, ['文件名称','录入时间', '车牌号码', '车牌类型', '识别耗时', '车牌信息'])
        for i, Data in enumerate(DATA):
            for j, data in enumerate(Data):
                ws.write(i, j, data)
        wb.save(path)
        QMessageBox.information(None, "成功", "数据已保存！", QMessageBox.Yes)  #

    def __writecsv(self, DATA, path):
        f = open(path, 'w')
        # DATA.insert(0, ['文件名称','录入时间', '车牌号码', '车牌类型', '识别耗时', '车牌信息'])
        for data in DATA:
            f.write((',').join(data) + '\n')
        f.close()
        QMessageBox.information(None, "成功", "数据已保存！", QMessageBox.Yes)

    def __writeFiles(self):
        path, filetype = QFileDialog.getSaveFileName(None, "另存为", self.ProjectPath,
                                                     "Excel 工作簿(*.xls);;CSV (逗号分隔)(*.csv)")
        if path == "":  # 未选择
            return
        if filetype == 'Excel 工作簿(*.xls)':
            self.__writexls(self.Data, path)
        elif filetype == 'CSV (逗号分隔)(*.csv)':
            self.__writecsv(self.Data, path)

    def __openimage(self):
        path, filetype = QFileDialog.getOpenFileName(None, "选择文件", self.ProjectPath,
                                                     "JPEG Image (*.jpg);;PNG Image (*.png);;JFIF Image (*.jfif)")  # ;;All Files (*)
        if path == "":  # 未选择文件
            return
        filename = path.split('/')[-1]

        # 尺寸适配
        size = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR).shape
        if size[0] / size[1] > 1.0907:
            w = size[1] * self.label.height() / size[0]
            h = self.label.height()
            w = int(w)
            h = int(h)
            jpg = QtGui.QPixmap(path).scaled(w, h)
        elif size[0] / size[1] < 1.0907:
            w = self.label.width()
            h = size[0] * self.label.width() / size[1]
            w = int(w)
            h = int(h)
            jpg = QtGui.QPixmap(path).scaled(w, h)
        else:
            jpg = QtGui.QPixmap(path).scaled(self.label.width(), self.label.height())

        self.label.setPixmap(jpg)
        result = self.__vlpr(path)
        if result is not None:
            self.Data.append(
                [filename, result['InputTime'], result['Number'], result['Type'], str(result['UseTime']) + '秒',
                 result['From']])
            self.__show(result, filename)




        else:
            QMessageBox.warning(None, "Error", "无法识别此图像！", QMessageBox.Yes)

    def realTimeParking(self):
        r = Function.refreshParking()
        self.parkingRemaining.setText(str(r[0]))
        self.specialParking.setText(r[1])



class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)



def mainF():
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    myWin.setWindowTitle("业务处理系统")
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())

