import logging
import threading
import time
import random
from  PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer
from PyQt5.QtCore import *
import files_rc
import pandas as pd
import warnings

import requests
import urllib
import urllib.request
import os
import json
import base64
import sqlite3

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os
import glob

folder_path = ''
category_name = ''
no_image = 0
upload_image = 0
cat = {}

warnings.filterwarnings("ignore", category=DeprecationWarning)

conn = sqlite3.connect('test.db')
select = "SELECT * FROM history"
cursor = conn.execute(select)
record = cursor.fetchone()

logo = record[0]
watermark = record[1]
output = record[2]
category = record[4]
quotes_csv = record[5]
creden = record[6]
image_url = record[8]
username = record[9]
passowrd = record[10]
fontFamily = record[11]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.setMinimumSize(QtCore.QSize(800, 700))
        # MainWindow.setMaximumSize(QtCore.QSize(800, 700))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 73, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 61, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 32, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 73, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 61, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 32, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 73, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 61, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 32, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(27, 29, 35, 160);\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setStyleSheet("")
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_center = QtWidgets.QFrame(self.frame_main)
        self.frame_center.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_content_right = QtWidgets.QFrame(self.frame_center)
        self.frame_content_right.setStyleSheet("background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_right.setObjectName("frame_content_right")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_content = QtWidgets.QFrame(self.frame_content_right)
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_content)
        self.stackedWidget.setStyleSheet("background: transparent;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_18 = QtWidgets.QFrame(self.page_4)
        self.frame_18.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 20px;")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_39 = QtWidgets.QFrame(self.frame_18)
        self.frame_39.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_39.setStyleSheet("border-color: rgb(2, 2, 2);")
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_39)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_45 = QtWidgets.QFrame(self.frame_39)
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.frame_45)
        self.verticalLayout_46.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.label_15 = QtWidgets.QLabel(self.frame_45)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_46.addWidget(self.label_15)
        self.verticalLayout_3.addWidget(self.frame_45)
        self.frame_41 = QtWidgets.QFrame(self.frame_39)
        self.frame_41.setStyleSheet("background-color: rgb(68, 34, 60);")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_41)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_11 = QtWidgets.QFrame(self.frame_41)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_16 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_25.addWidget(self.label_16)
        self.comboBox = QtWidgets.QComboBox(self.frame_11)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_25.addWidget(self.comboBox)
        self.horizontalLayout_14.addWidget(self.frame_11)
        self.verticalLayout_3.addWidget(self.frame_41)
        self.frame_71 = QtWidgets.QFrame(self.frame_39)
        self.frame_71.setStyleSheet("background-color: rgb(35, 40, 49);")
        self.frame_71.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_71.setObjectName("frame_71")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_71)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.frame_71)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_42 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_5.addWidget(self.label_42)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_10.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_10.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_5.addWidget(self.lineEdit_10)
        self.horizontalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frame_71)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_6.addWidget(self.pushButton_2)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(self.frame_71)
        self.frame_42 = QtWidgets.QFrame(self.frame_39)
        self.frame_42.setStyleSheet("background-color: rgb(68, 34, 60);")
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_42)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frame_14 = QtWidgets.QFrame(self.frame_42)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_18 = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_16.addWidget(self.label_18)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_14)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_16.addWidget(self.lineEdit_4)
        self.horizontalLayout_16.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.frame_42)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_15.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_15.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_15.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_14.addWidget(self.pushButton_15)
        self.horizontalLayout_16.addWidget(self.frame_13)
        self.verticalLayout_3.addWidget(self.frame_42)
        self.frame_72 = QtWidgets.QFrame(self.frame_39)
        self.frame_72.setStyleSheet("background-color: rgb(35, 40, 49);")
        self.frame_72.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_72.setObjectName("frame_72")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_72)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_15 = QtWidgets.QFrame(self.frame_72)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_15)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_11.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setReadOnly(False)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_25.addWidget(self.lineEdit_11)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_16.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_16.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_16.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_25.addWidget(self.pushButton_16)
        self.horizontalLayout_17.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_72)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_49 = QtWidgets.QLabel(self.frame_16)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.verticalLayout_28.addWidget(self.label_49)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_16)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_14.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_14.setText("")
        self.lineEdit_14.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setReadOnly(False)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.verticalLayout_28.addWidget(self.lineEdit_14)
        self.horizontalLayout_17.addWidget(self.frame_16)
        self.verticalLayout_3.addWidget(self.frame_72)
        self.frame_44 = QtWidgets.QFrame(self.frame_39)
        self.frame_44.setStyleSheet("background-color: rgb(68, 34, 60);")
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_44)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_44)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_25 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_8.addWidget(self.label_25)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_8.addWidget(self.lineEdit_2)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_44)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_26 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_10.addWidget(self.label_26)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_10.addWidget(self.lineEdit_5)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.verticalLayout_3.addWidget(self.frame_44)
        self.frame_46 = QtWidgets.QFrame(self.frame_39)
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_46)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_46)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_46)
        self.pushButton_13.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_13.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_13.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout.addWidget(self.pushButton_13)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_46)
        self.pushButton_10.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_10.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_46)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_3.addWidget(self.frame_46)
        self.horizontalLayout_19.addWidget(self.frame_39)
        self.verticalLayout_23.addWidget(self.frame_18)
        self.stackedWidget.addWidget(self.page_4)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_19 = QtWidgets.QFrame(self.page)
        self.frame_19.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 20px;")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.frame_40 = QtWidgets.QFrame(self.frame_19)
        self.frame_40.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_40.setStyleSheet("border-color: rgb(2, 2, 2);")
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_40)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_47 = QtWidgets.QFrame(self.frame_40)
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.frame_47)
        self.verticalLayout_47.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.label_17 = QtWidgets.QLabel(self.frame_47)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_47.addWidget(self.label_17)
        self.verticalLayout_11.addWidget(self.frame_47)
        self.frame_73 = QtWidgets.QFrame(self.frame_40)
        self.frame_73.setStyleSheet("background-color: rgb(35, 40, 49);")
        self.frame_73.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_73.setObjectName("frame_73")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_73)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.frame_73)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_44 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_13.addWidget(self.label_44)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_12.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_12.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_13.addWidget(self.lineEdit_12)
        self.horizontalLayout_5.addWidget(self.frame_5)
        self.verticalLayout_11.addWidget(self.frame_73)
        self.frame_48 = QtWidgets.QFrame(self.frame_40)
        self.frame_48.setStyleSheet("background-color: rgb(68, 34, 60);")
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.frame_48)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.label_20 = QtWidgets.QLabel(self.frame_48)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_49.addWidget(self.label_20)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_48)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_49.addWidget(self.lineEdit_6)
        self.verticalLayout_11.addWidget(self.frame_48)
        self.frame_74 = QtWidgets.QFrame(self.frame_40)
        self.frame_74.setStyleSheet("background-color: rgb(35, 40, 49);")
        self.frame_74.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_74.setObjectName("frame_74")
        self.verticalLayout_74 = QtWidgets.QVBoxLayout(self.frame_74)
        self.verticalLayout_74.setObjectName("verticalLayout_74")
        self.label_45 = QtWidgets.QLabel(self.frame_74)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_74.addWidget(self.label_45)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_74)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_13.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_13.setText("")
        self.lineEdit_13.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setReadOnly(False)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_74.addWidget(self.lineEdit_13)
        self.verticalLayout_11.addWidget(self.frame_74)
        self.frame_49 = QtWidgets.QFrame(self.frame_40)
        self.frame_49.setStyleSheet("background-color: rgb(68, 34, 60);")
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_49)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.frame_49)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_27 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_15.addWidget(self.label_27)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setText(creden)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_15.addWidget(self.lineEdit_3)
        self.horizontalLayout_8.addWidget(self.frame_7)
        self.verticalLayout_11.addWidget(self.frame_49)
        self.frame_50 = QtWidgets.QFrame(self.frame_40)
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_50)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_50)
        self.pushButton_8.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_9.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_50)
        self.pushButton_7.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_9.addWidget(self.pushButton_7)
        self.verticalLayout_11.addWidget(self.frame_50)
        self.horizontalLayout_21.addWidget(self.frame_40)
        self.verticalLayout_17.addWidget(self.frame_19)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_21 = QtWidgets.QFrame(self.page_3)
        self.frame_21.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 20px;")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_58 = QtWidgets.QFrame(self.frame_21)
        self.frame_58.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_58.setStyleSheet("border-color: rgb(2, 2, 2);")
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_58)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_59 = QtWidgets.QFrame(self.frame_58)
        self.frame_59.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.frame_59)
        self.verticalLayout_51.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.label_22 = QtWidgets.QLabel(self.frame_59)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_51.addWidget(self.label_22)
        self.verticalLayout_7.addWidget(self.frame_59)
        self.frame_76 = QtWidgets.QFrame(self.frame_58)
        self.frame_76.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_76.setStyleSheet("background-color: rgb(68, 34, 60);")
        self.frame_76.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_76.setObjectName("frame_76")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_76)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_9 = QtWidgets.QFrame(self.frame_76)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_47 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_20.addWidget(self.label_47)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_16.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_16.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.verticalLayout_20.addWidget(self.lineEdit_16)
        self.horizontalLayout_11.addWidget(self.frame_9)
        self.verticalLayout_7.addWidget(self.frame_76)
        self.frame_63 = QtWidgets.QFrame(self.frame_58)
        self.frame_63.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_63.setObjectName("frame_63")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_63)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_63)
        self.pushButton_12.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_12.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_13.addWidget(self.pushButton_12)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_63)
        self.pushButton_11.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_11.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_13.addWidget(self.pushButton_11)
        self.verticalLayout_7.addWidget(self.frame_63)
        self.horizontalLayout_23.addWidget(self.frame_58)
        self.verticalLayout_24.addWidget(self.frame_21)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_20 = QtWidgets.QFrame(self.page_2)
        self.frame_20.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 20px;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame_51 = QtWidgets.QFrame(self.frame_20)
        self.frame_51.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_51.setStyleSheet("border-color: rgb(2, 2, 2);")
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_51)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_54 = QtWidgets.QFrame(self.frame_51)
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.frame_54)
        self.verticalLayout_50.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.label_21 = QtWidgets.QLabel(self.frame_54)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_50.addWidget(self.label_21)
        self.verticalLayout_12.addWidget(self.frame_54)
        self.frame_77 = QtWidgets.QFrame(self.frame_51)
        self.frame_77.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_77.setStyleSheet("background-color: rgb(68, 34, 60);")
        self.frame_77.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_77.setObjectName("frame_77")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_77)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_10 = QtWidgets.QFrame(self.frame_77)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_48 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.verticalLayout_21.addWidget(self.label_48)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_17.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_17.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.verticalLayout_21.addWidget(self.lineEdit_17)
        self.horizontalLayout_15.addWidget(self.frame_10)
        self.frame_12 = QtWidgets.QFrame(self.frame_77)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_14.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_14.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_14.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_26.addWidget(self.pushButton_14)
        self.horizontalLayout_15.addWidget(self.frame_12)
        self.verticalLayout_12.addWidget(self.frame_77)
        self.frame_75 = QtWidgets.QFrame(self.frame_51)
        self.frame_75.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_75.setStyleSheet("background-color: rgb(35, 40, 49);")
        self.frame_75.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_75.setObjectName("frame_75")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_75)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_6 = QtWidgets.QFrame(self.frame_75)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_46 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_18.addWidget(self.label_46)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_15.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_15.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout_18.addWidget(self.lineEdit_15)
        self.horizontalLayout_10.addWidget(self.frame_6)
        self.frame_8 = QtWidgets.QFrame(self.frame_75)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_19.addWidget(self.pushButton_5)
        self.horizontalLayout_10.addWidget(self.frame_8)
        self.verticalLayout_12.addWidget(self.frame_75)
        self.frame_17 = QtWidgets.QFrame(self.frame_51)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.frame_22 = QtWidgets.QFrame(self.frame_17)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_50 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.verticalLayout_29.addWidget(self.label_50)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_22)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_18.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_18.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.verticalLayout_29.addWidget(self.lineEdit_18)
        self.horizontalLayout_18.addWidget(self.frame_22)
        self.frame_23 = QtWidgets.QFrame(self.frame_17)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_51 = QtWidgets.QLabel(self.frame_23)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.verticalLayout_30.addWidget(self.label_51)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame_23)
        self.lineEdit_19.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_19.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_19.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.verticalLayout_30.addWidget(self.lineEdit_19)
        self.horizontalLayout_18.addWidget(self.frame_23)
        self.verticalLayout_12.addWidget(self.frame_17)
        self.frame_24 = QtWidgets.QFrame(self.frame_51)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.frame_25 = QtWidgets.QFrame(self.frame_24)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_52 = QtWidgets.QLabel(self.frame_25)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.verticalLayout_31.addWidget(self.label_52)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame_25)
        self.lineEdit_20.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_20.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_20.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setPlaceholderText("")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.verticalLayout_31.addWidget(self.lineEdit_20)
        self.horizontalLayout_24.addWidget(self.frame_25)
        self.frame_27 = QtWidgets.QFrame(self.frame_24)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_54 = QtWidgets.QLabel(self.frame_27)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.verticalLayout_33.addWidget(self.label_54)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame_27)
        self.lineEdit_21.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_21.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_21.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_21.setPlaceholderText("")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.verticalLayout_33.addWidget(self.lineEdit_21)
        self.horizontalLayout_24.addWidget(self.frame_27)
        self.frame_26 = QtWidgets.QFrame(self.frame_24)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_53 = QtWidgets.QLabel(self.frame_26)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.verticalLayout_32.addWidget(self.label_53)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_26)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_32.addWidget(self.comboBox_2)
        self.horizontalLayout_24.addWidget(self.frame_26)
        self.verticalLayout_12.addWidget(self.frame_24)
        self.frame_62 = QtWidgets.QFrame(self.frame_51)
        self.frame_62.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_62.setObjectName("frame_62")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_62)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_62)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_12.addWidget(self.pushButton_6)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_62)
        self.pushButton_9.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_9.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_12.addWidget(self.pushButton_9)
        self.verticalLayout_12.addWidget(self.frame_62)
        self.horizontalLayout_22.addWidget(self.frame_51)
        self.verticalLayout_22.addWidget(self.frame_20)
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_61 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.frame_52 = QtWidgets.QFrame(self.page_5)
        self.frame_52.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 20px;")
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_52)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame_53 = QtWidgets.QFrame(self.frame_52)
        self.frame_53.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_53.setStyleSheet("border-color: rgb(2, 2, 2);")
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.frame_53)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.frame_55 = QtWidgets.QFrame(self.frame_53)
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.frame_55)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.label_35 = QtWidgets.QLabel(self.frame_55)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_55.addWidget(self.label_35)
        self.verticalLayout_52.addWidget(self.frame_55)
        self.frame_56 = QtWidgets.QFrame(self.frame_53)
        self.frame_56.setStyleSheet("background-color: rgb(68, 34, 60);")
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout(self.frame_56)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.label_36 = QtWidgets.QLabel(self.frame_56)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_56.addWidget(self.label_36)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_56)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_8.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_56.addWidget(self.lineEdit_8)
        self.verticalLayout_52.addWidget(self.frame_56)
        self.frame_57 = QtWidgets.QFrame(self.frame_53)
        self.frame_57.setStyleSheet("background-color: rgb(35, 40, 49);")
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.verticalLayout_57 = QtWidgets.QVBoxLayout(self.frame_57)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.label_37 = QtWidgets.QLabel(self.frame_57)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_57.addWidget(self.label_37)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_57)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_9.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_9.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_57.addWidget(self.lineEdit_9)
        self.verticalLayout_52.addWidget(self.frame_57)
        self.frame_61 = QtWidgets.QFrame(self.frame_53)
        self.frame_61.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.verticalLayout_60 = QtWidgets.QVBoxLayout(self.frame_61)
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_61)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(57, 65, 80);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(68, 34, 60);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_60.addWidget(self.pushButton_4)
        self.verticalLayout_52.addWidget(self.frame_61, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_20.addWidget(self.frame_53)
        self.verticalLayout_61.addWidget(self.frame_52)
        self.stackedWidget.addWidget(self.page_5)
        self.verticalLayout_9.addWidget(self.stackedWidget, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addWidget(self.frame_content)
        self.frame_grip = QtWidgets.QFrame(self.frame_content_right)
        self.frame_grip.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_grip.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_grip.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_label_bottom = QtWidgets.QFrame(self.frame_grip)
        self.frame_label_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_bottom.setObjectName("frame_label_bottom")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_credits = QtWidgets.QLabel(self.frame_label_bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_credits.setText("")
        self.label_credits.setObjectName("label_credits")
        self.horizontalLayout_7.addWidget(self.label_credits)
        self.label_version = QtWidgets.QLabel(self.frame_label_bottom)
        self.label_version.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_version.setFont(font)
        self.label_version.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_version.setText("")
        self.label_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_version.setObjectName("label_version")
        self.horizontalLayout_7.addWidget(self.label_version)
        self.horizontalLayout_6.addWidget(self.frame_label_bottom)
        self.frame_size_grip = QtWidgets.QFrame(self.frame_grip)
        self.frame_size_grip.setMaximumSize(QtCore.QSize(20, 20))
        self.frame_size_grip.setStyleSheet("QSizeGrip {\n"
"    background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.horizontalLayout_6.addWidget(self.frame_size_grip)
        self.verticalLayout_4.addWidget(self.frame_grip)
        self.horizontalLayout_2.addWidget(self.frame_content_right)
        self.verticalLayout.addWidget(self.frame_center)
        self.verticalLayout_2.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow): 
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Multi Quotes Multi Images Editor</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "Category Name"))
        
        # output
        self.label_42.setText(_translate("MainWindow", "Output Folder"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "C/abc/image"))
        self.lineEdit_10.setText(_translate('MainWindow',output))
        
        # input
        self.pushButton_2.setText(_translate("MainWindow", "Select Folder"))
        self.label_18.setText(_translate("MainWindow", "Image Folder"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "C/abc/image folder"))

        # Select quotes csv file
        self.pushButton_15.setText(_translate("MainWindow", "Select Folder"))
        self.lineEdit_11.setPlaceholderText(_translate("MainWindow", "Quote file link"))
        self.lineEdit_11.setText(_translate("MainWindow",quotes_csv))
        self.pushButton_16.setText(_translate("MainWindow", "Select Quote"))

        # Image name
        self.label_49.setText(_translate("MainWindow", "Image Name"))
        self.lineEdit_14.setPlaceholderText(_translate("MainWindow", "Image Name"))

        # Image count
        self.label_25.setText(_translate("MainWindow", "Number Of Images Found"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_26.setText(_translate("MainWindow", "Uploaded Images"))
        self.lineEdit_5.setText(_translate("MainWindow", "0"))

        # Buttons
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "10"))
        self.pushButton.setText(_translate("MainWindow", "Set Site"))
        self.pushButton_13.setText(_translate("MainWindow", "Create cate"))
        self.pushButton_10.setText(_translate("MainWindow", "Select Logo"))
        self.pushButton_3.setText(_translate("MainWindow", "Start"))

        # Wordpress credentials
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p>site credentials</p></body></html>"))
        self.label_44.setText(_translate("MainWindow", "Wordpress Website Link"))
        self.lineEdit_12.setPlaceholderText(_translate("MainWindow", "https://immagini-buongiorno.com"))
        self.lineEdit_12.setText(_translate("MainWindow", str(image_url)))
        self.label_20.setText(_translate("MainWindow", "User Name"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "User name"))
        self.lineEdit_6.setText(_translate("MainWindow", str(username)))
        self.label_45.setText(_translate("MainWindow", "User Password"))
        self.lineEdit_13.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_13.setText(_translate("MainWindow", str(passowrd)))
        self.label_27.setText(_translate("MainWindow", "API Encode Credential"))
        self.pushButton_8.setText(_translate("MainWindow", "Back"))
        self.pushButton_7.setText(_translate("MainWindow", "Save"))

        # Create Category of image
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">Create Category of Images</span></p></body></html>"))
        self.label_47.setText(_translate("MainWindow", "Category Name"))
        self.lineEdit_16.setPlaceholderText(_translate("MainWindow", "Category Name"))
        self.pushButton_12.setText(_translate("MainWindow", "Back"))
        self.pushButton_11.setText(_translate("MainWindow", "Create Category"))

        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">Set Logo Image</span></p></body></html>"))
        
        # Select Logo
        self.label_48.setText(_translate("MainWindow", "Select Logo Image* (should be .PNG file)"))
        self.lineEdit_17.setPlaceholderText(_translate("MainWindow", "image.png"))
        self.lineEdit_17.setText(_translate("MainWindow", logo))
        self.pushButton_14.setText(_translate("MainWindow", "Select Logo"))
        
        # Select Watermark
        self.label_46.setText(_translate("MainWindow", "Select Watermark Image* (should be .PNG file)"))
        self.lineEdit_15.setPlaceholderText(_translate("MainWindow", "image.png"))
        self.lineEdit_15.setText(_translate("MainWindow", watermark))
        self.pushButton_5.setText(_translate("MainWindow", "Select Logo"))


        self.label_50.setText(_translate("MainWindow", "Background Image Width px"))
        self.lineEdit_18.setText(_translate("MainWindow", "0"))
        self.lineEdit_18.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_51.setText(_translate("MainWindow", "Background Image Height px"))
        self.lineEdit_19.setText(_translate("MainWindow", "0"))
        self.lineEdit_19.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_52.setText(_translate("MainWindow", "Quote Font Size"))
        self.lineEdit_20.setText(_translate("MainWindow", "0"))
        self.label_54.setText(_translate("MainWindow", "Quote Width px"))
        self.lineEdit_21.setText(_translate("MainWindow", "0"))
        self.label_53.setText(_translate("MainWindow", "Quote Font Family Style"))
        self.pushButton_6.setText(_translate("MainWindow", "Back"))
        self.pushButton_9.setText(_translate("MainWindow", "Save"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p>Login</p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "Email"))
        self.label_37.setText(_translate("MainWindow", "Password"))
        self.pushButton_4.setText(_translate("MainWindow", "Login"))
        
        
class MainWindow(QMainWindow):
    global keywords
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setWindowTitle('Form Filler')
        self.ui.setupUi(self)
        self.get_category()
        self.ui.pushButton_2.clicked.connect(self.select_input_folder)
        self.ui.pushButton_15.clicked.connect(self.select_output_folder)
        self.ui.pushButton_16.clicked.connect(self.select_quote_csv)
        self.ui.pushButton_3.clicked.connect(self.thread_start)
        self.ui.pushButton.clicked.connect(self.set_cred_page)
        self.ui.pushButton_8.clicked.connect(self.back_page)
        self.ui.pushButton_7.clicked.connect(self.save_cred)
        self.ui.pushButton_10.clicked.connect(self.set_logo_page)
        self.ui.pushButton_6.clicked.connect(self.back_page)
        self.ui.pushButton_9.clicked.connect(self.save_logo)
        self.ui.pushButton_14.clicked.connect(self.select_logo)
        self.ui.pushButton_5.clicked.connect(self.select_watermark_logo)
        self.ui.pushButton_13.clicked.connect(self.create_tag_page)
        self.ui.pushButton_12.clicked.connect(self.back_page)
        self.ui.pushButton_11.clicked.connect(self.create_cate)
        
        
        self.show()
    
    def get_category(self):
        try:
            global cat
            url_cat = self.ui.lineEdit_12.text()
            creden = self.ui.lineEdit_3.text()
            self.ui.comboBox.clear()
            url = url_cat+"/wp-json/wp/v2/categories?per_page=100"

            payload={}
            headers = {
              'Authorization': 'Basic '+creden
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            cat_res = response.json()
    #         print(cat_res)
            for i in range(len(cat_res)):
                data1 = {
                    cat_res[i]['name']: cat_res[i]['id']
                }
                cat.update(data1)
                self.ui.comboBox.addItem(cat_res[i]['name'])
    #         print(cat)
            for key, value in cat.items():
                if value == int(category):
                        print("----")
                        print(value)
                        self.ui.comboBox.setCurrentText(key)
        except Exception as e:
            print(e)
            pass
        
    def set_cred_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        
    def set_logo_page(self):
        # Create a list to store the image file paths
        font_fam = []

        # Loop through all files in the folder
        for file_path in os.listdir("font style"):
            # Check if the file is an image
            if file_path.endswith(".ttf"):
                # Add the file path to the list of image paths
                self.ui.comboBox_2.addItem(file_path)
#                 
            
        self.ui.stackedWidget.setCurrentIndex(3)
        
    def create_tag_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def back_page(self):
        self.get_category()
        self.ui.stackedWidget.setCurrentIndex(0)
        
    def create_cate(self):
        api_link = self.ui.lineEdit_12.text()
        tag_name = self.ui.lineEdit_16.text()
        link_url = api_link+"/wp-json/wp/v2/categories"
        creden = self.ui.lineEdit_3.text()
        
        url = link_url

        payload = json.dumps({
          "name": tag_name
        })
        headers = {
          'Authorization': 'Basic '+creden,
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code==201:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Category has been created")
            msg.setWindowTitle("Save")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Something error is there try again later")
            msg.setWindowTitle("Error")
            msg.exec_()
        
    def save_logo(self):
        image = self.ui.lineEdit_15.text()
        water_mark = self.ui.lineEdit_15.text()
        if image=='' or water_mark=='':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Logo image not found")
            msg.setWindowTitle("error")
            msg.exec_()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Image have been updated")
        msg.setWindowTitle("Saved")
        msg.exec_()
    
    def select_quote_csv(self):
        watermark_name = QFileDialog.getOpenFileName(self, 'Open file',"","*.csv")
        print(watermark_name[0])
        self.ui.lineEdit_11.setText(watermark_name[0])

    def select_input_folder(self):
        global folder_path
        input_folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.ui.lineEdit_10.setText(input_folderpath)
        
    def select_output_folder(self):
        global folder_path
        output_folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.ui.lineEdit_4.setText(output_folderpath)
    
    def select_logo(self):
        logo_name = QFileDialog.getOpenFileName(self, 'Open file',"","*.png")
        print(logo_name[0])
        self.ui.lineEdit_17.setText(logo_name[0])
        
    def select_watermark_logo(self):
        watermark_name = QFileDialog.getOpenFileName(self, 'Open file',"","*.png")
        print(watermark_name[0])
        self.ui.lineEdit_15.setText(watermark_name[0])
    
    def run_scrapper(self):
        self.ui.pushButton_3.setText("Running")
        conn = sqlite3.connect('test.db')
        output_folderpath = self.ui.lineEdit_10.text()
        input_folderpath = self.ui.lineEdit_4.text()
        category = self.ui.comboBox.currentText()
        font_family = self.ui.comboBox_2.currentText()
        categ = cat[category]
        print("-------")
        print(categ)
        back_widht = int(self.ui.lineEdit_18.text())
        back_height = int(self.ui.lineEdit_19.text())
        quote_font = int(self.ui.lineEdit_20.text())
        #save_path = folderpath+'/'+category
        name = self.ui.lineEdit_14.text()
        quote = self.ui.lineEdit_11.text()
        quote_wid = self.ui.lineEdit_21.text()
        #no_img = int(self.ui.lineEdit_2.text())
        image_url = self.ui.lineEdit_12.text()
        #post_url = self.ui.lineEdit_12.text()
        creden = self.ui.lineEdit_3.text()
        logo1 = self.ui.lineEdit_17.text()
        waterm = self.ui.lineEdit_15.text()
        # load quotes csv
        df = pd.read_csv(quote)

        data = [logo1, waterm, output_folderpath, input_folderpath, categ, quote, creden, font_family]
        self.update_record(data, conn)

        
        
        print("*********************")

        image_paths = []

        # Loop through all files in the folder
        for file_path in glob.glob(os.path.join(input_folderpath, "*")):
            # Check if the file is an image
            if file_path.endswith(".jpg") or file_path.endswith(".png") or file_path.endswith(".jpeg"):
                # Add the file path to the list of image paths
                image_paths.append(file_path)

        

        # Loop through all image paths
        print(len(image_paths))
        no_img = len(image_paths)
        self.ui.lineEdit_2.setText(str(no_img))
        for i in range(len(image_paths)):
            for j, row in df.iterrows():
                # Open the image
                image = Image.open(image_paths[i])

                if(back_widht != 0 and back_height != 0):
                        image = image.resize((back_widht, back_height)) 

                width, height = image.size
                
                # width = width-400
                # Set the text for the quote
                if waterm != "":
                        watermark = Image.open(waterm)
                        half_opacity = watermark.resize((int(width), int(width*0.28)))
        #             
                        r, g, b, a = half_opacity.split()
                        x = 1
                        y = int(image.height/2)
                        half_opacity_width, half_opacity_height = half_opacity.size
                        x = int((width-half_opacity_width)/2)
                        y = int((height-half_opacity_height)/2)
                        image.paste(a, (x, y), a)
                
                # img_resized = image.resize((back_widht, back_height))
                img_resized = image

                enhancer = ImageEnhance.Brightness(img_resized)
                half_opacity = enhancer.enhance(0.85)
                
                width, height = img_resized.size

                ################# New line break code #################
                
                
                draw = ImageDraw.Draw(half_opacity)
                
                # font = ImageFont.truetype('font style/'+font_family, quote_font)
                # Calculate Font size 
                font_size = (width*height)*0.00014
                font_family = fontFamily if font_family == "" else font_family 
                font = ImageFont.truetype('font style/'+font_family, int(font_size))

                # Define the quote
                
                # Define the maximum width for each line
                # max_width = int(quote_wid)
                max_width = int(image.width - 50)

                # Create a draw object
                draw = ImageDraw.Draw(half_opacity)
                images123 = half_opacity

                # Calculate the height of each line
                
                # quote = "You've gotta dance like there's nobody watching,Love like you'll never be hurt."
                quote = row['quote']
                line_height = font.getsize(quote)[1]

                # Split the quote into multiple lines based on the maximum width
                lines = []
                line = ""
                for word in quote.split():
                   if draw.textsize(line + word, font=font)[0] > max_width:
                        lines.append(line)
                        line = ""
                   line += word + " "
                lines.append(line)

                # Set the starting y-coordinate for drawing the quote
                y = (half_opacity.height - (line_height * len(lines))) // 2

                # Draw each line of the quote
                for line in lines:
                        line_width = font.getsize(line)[0]
                        x = (half_opacity.width - line_width) // 2
                        draw.text((x, y), line, font=font, fill=(255, 255, 255))
                        y += line_height
                
                ################# New line break code End #################
                
                if logo1!="":                
                        logo = Image.open(logo1).convert("RGBA")

                        # Resize the logo to 0.05% of its original size
                        he = half_opacity.width * 0.18
                        he1 = he*0.28
                        logo = logo.resize((int(half_opacity.width * 0.18), int(he1)))

                        # Calculate the position to place the logo
                        x = half_opacity.width - logo.width - 10
                        y = half_opacity.height - logo.height - 10
                        

                        # Paste the logo on the background image
                        half_opacity.paste(logo, (x, y), logo)
                file_name, file_extension = os.path.splitext(image_paths[i])
                file_name = name+str(i)+str(j)
                name_ext = f"{os.path.basename(file_name)}{file_extension}"
                output_path = os.path.join(output_folderpath, name_ext)
                half_opacity.save(output_path)
                # num = int(self.ui.lineEdit_5.text())
                # num+=1
                # self.ui.lineEdit_5.setText(str(num))
                
                ############### Here is the Comment Code of Wordpress API ####################
                
                reqUrl = image_url+"/wp-json/wp/v2/media?alt_text="+file_name

                headersList = {
                "Cache-Control": "no-cache",
                "Content-Disposition": "attachment; filename="+name_ext,
                "Authorization": "Basic "+creden,
                "Content-Type": "application/octet-stream"
                }
                with open(output_folderpath+"/"+name_ext, 'rb') as f:
                        payload = f.read()
        #             

                response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
                time.sleep(2)
        #             
                tag = response.json()
        #                    

                ######### Tag Create Api ###############
                
                print("create tag")
                url2 = image_url+"/wp-json/wp/v2/tags"

                payload2 = json.dumps({
                "name": file_name
                })
                headers = {
                'Authorization': 'Basic '+creden,
                'Content-Type': 'application/json'
                }

                response3 = requests.request("POST", url2, headers=headers, data=payload2)
                tag_name = response3.json()
                print(tag_name['name'])

                #########  Post Create Api #############
                print("post image")
                
                reqUrl1 = image_url+"/wp-json/wp/v2/posts"

                headersList1 = {
                "Accept": "*/*",
                "Content-Type": "application/json",
                "Authorization": "Basic "+creden
                }
                print(f"tag_id = {tag_name['id']}")
                print(f"{tag['id']}, {tag['guid']['rendered']}")
                payload1 = json.dumps({
                "title": file_name,
                "status":"publish",
                "categories" : categ,
                "featured_media": tag['id'],
                "content" : "<a style='text-align: center;display: table;background: black;margin: auto;padding: 3px;color: white !important;border-radius: 7px;padding-right: 14px !important;padding-left: 14px !important; border: 2px solid red;box-shadow:0px 0px 0px 4px black;font-weight: 800 !important;' href="+tag['guid']['rendered']+" target='_blank' download>Download</a>",
                "tags" : [tag_name['id']]
                })

                response = requests.request("POST", reqUrl1, data=payload1,  headers=headersList1)
                print(response.status_code)
                if response.status_code==201:
                        num = int(self.ui.lineEdit_5.text())
                        num+=1
                        self.ui.lineEdit_5.setText(str(num))
                        print("saved")

        #         print(response.text)
        self.ui.pushButton_3.setText("Start")
        
    def thread_start(self):
        folderpath = self.ui.lineEdit_10.text()
        category = self.ui.comboBox.currentText()
        name = self.ui.lineEdit_4.text()
        no_img = self.ui.lineEdit_2.text()
        search_key = self.ui.lineEdit_11.text()
        creden = self.ui.lineEdit_3.text()
        if (search_key=='' or folderpath=='' or category=='' or name=='' or creden==''):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Required all input fields or check api encode credential or logo image")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        x = threading.Thread(target=self.run_scrapper)
        x.start()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Search Images & Updating on server")
        msg.setWindowTitle("Updating")
        msg.exec_()
        
    def save_cred(self):
        image_url = self.ui.lineEdit_12.text()
        user_name = self.ui.lineEdit_6.text()
        password = self.ui.lineEdit_13.text()

        print(image_url)
        print(user_name)
        print(password)

        if image_url=='' or user_name=='' or password=='':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please fill all required input field..")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            userpass = user_name+':'+password
            b54Val = base64.b64encode(userpass.encode()).decode()
            print(b54Val)
            self.ui.lineEdit_3.setText(b54Val)
            
    def image_check(self, url):
        select = "SELECT IMAGE_ID_PK from COMPANY WHERE IMAGE_URL=?"
        cursor = conn.execute(select, [url])
        if len(curson)==0:
            return 0
        else:
            return 1
        
    def image_save(self, name, url):
        try:
            insert = "INSERT INTO COMPANY (IMAGE_NAME, IMAGE_URL) VALUES (?, ?)"
            cursor = conn.execute(insert, [name, url]);
            return "save"
        except:
            return "not save"

    def update_record(self, data, conn):
        image_url = self.ui.lineEdit_12.text()
        user_name = self.ui.lineEdit_6.text()
        password = self.ui.lineEdit_13.text()

        if data[7] == "":
                data[7] = fontFamily

        update_query = "UPDATE history SET Logo=?, Watermark=?, Output=?, Input=?, Category=?, Quotes=?, cred=?, image_url=?, username=?, password=?, font=? WHERE id=?"
        data_tuple = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], image_url ,user_name, password, data[7], 1)
        cursor = conn.execute(update_query, data_tuple)
        conn.commit()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
