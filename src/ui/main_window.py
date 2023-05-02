# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 617)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"border-color: rgb(119, 118, 123);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(119, 118, 123);\n"
"border-color: rgb(119, 118, 123);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_det = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.radioButton_det.setFont(font)
        self.radioButton_det.setStyleSheet("QRadioButton\n"
"{font-size: 18px;\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(:/images/icons/button-off.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    \n"
"    image: url(:/images/icons/button-on.png);\n"
"}\n"
"\n"
"QRadioButton::disabled{\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.radioButton_det.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Zimbabwe))
        self.radioButton_det.setChecked(True)
        self.radioButton_det.setObjectName("radioButton_det")
        self.verticalLayout_4.addWidget(self.radioButton_det)
        self.radioButton_seg = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_seg.setFont(font)
        self.radioButton_seg.setStyleSheet("QRadioButton\n"
"{font-size: 18px;\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(:/images/icons/button-off.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    \n"
"    image: url(:/images/icons/button-on.png);\n"
"}\n"
"\n"
"QRadioButton::disabled{\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.radioButton_seg.setObjectName("radioButton_seg")
        self.verticalLayout_4.addWidget(self.radioButton_seg)
        self.radioButton_pose = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_pose.setFont(font)
        self.radioButton_pose.setStyleSheet("QRadioButton\n"
"{font-size: 18px;\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(:/images/icons/button-off.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    \n"
"    image: url(:/images/icons/button-on.png);\n"
"}\n"
"\n"
"QRadioButton::disabled{\n"
"background-color:  #bf513b;\n"
"}")
        self.radioButton_pose.setObjectName("radioButton_pose")
        self.verticalLayout_4.addWidget(self.radioButton_pose)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_model = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_model.setAutoFillBackground(False)
        self.comboBox_model.setStyleSheet("QComboBox QAbstractItemView {\n"
"font-size: 16px;\n"
"outline:none;\n"
"border:none;}\n"
"\n"
"QComboBox{\n"
"font-size: 16px;\n"
"color: rgb(218, 218, 218);\n"
"border-width:0px;\n"
"border-color:white;\n"
"border-style:solid;\n"
"background-color: rgba(200, 200, 200,50);}\n"
"\n"
"QComboBox::drop-down {\n"
"margin-top:1;\n"
"height:20;\n"
"color: rgb(218, 218, 218);\n"
"background-color: rgba(200, 200, 200,50);\n"
"border-image: url(:/images/icons/roll_down.png);\n"
"}\n"
"\n"
"QComboBox::disabled{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.comboBox_model.setCurrentText("YOLOv8n")
        self.comboBox_model.setObjectName("comboBox_model")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_model)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_file = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_file.sizePolicy().hasHeightForWidth())
        self.pushButton_file.setSizePolicy(sizePolicy)
        self.pushButton_file.setStyleSheet("QPushButton{\n"
"    image: url(:/images/icons/video.png);\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(200, 200, 200,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{\n"
"                     image: url(:/images/icons/video.png);\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        self.pushButton_file.setText("")
        self.pushButton_file.setObjectName("pushButton_file")
        self.horizontalLayout_3.addWidget(self.pushButton_file)
        self.pushButton_cam = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cam.sizePolicy().hasHeightForWidth())
        self.pushButton_cam.setSizePolicy(sizePolicy)
        self.pushButton_cam.setStyleSheet("QPushButton{\n"
"    image: url(:/images/icons/camera_on.png);\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(200, 200, 200,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}url(:/images/icons/camera_on.png)")
        self.pushButton_cam.setText("")
        self.pushButton_cam.setObjectName("pushButton_cam")
        self.horizontalLayout_3.addWidget(self.pushButton_cam)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.doubleSpinBox_conf = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_conf.setStyleSheet("QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/images/icons/botton_down.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/images/icons/botton_down.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/images/icons/botton_up.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/images/icons/botton_up.png);}")
        self.doubleSpinBox_conf.setMaximum(1.0)
        self.doubleSpinBox_conf.setSingleStep(0.01)
        self.doubleSpinBox_conf.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox_conf.setProperty("value", 0.3)
        self.doubleSpinBox_conf.setObjectName("doubleSpinBox_conf")
        self.horizontalLayout_5.addWidget(self.doubleSpinBox_conf)
        self.horizontalSlider_conf = QtWidgets.QSlider(self.groupBox_4)
        self.horizontalSlider_conf.setStyleSheet("QSlider{\n"
"border-color: #bcbcbc;\n"
"color:#d9d9d9;\n"
"}\n"
"QSlider::groove:horizontal {                                \n"
"     border: 1px solid #999999;                             \n"
"     height: 3px;                                           \n"
"    margin: 0px 0;                                         \n"
"     left: 5px; right: 5px; \n"
" }\n"
"QSlider::handle:horizontal {                               \n"
"     border: 0px ; \n"
"     border-image: url(:/images/icons/point.png);\n"
"     width:15px;\n"
"     margin: -7px -7px -7px -7px;                  \n"
"} \n"
"QSlider::add-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9); \n"
"\n"
"}\n"
"QSlider::sub-page:horizontal{                               \n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);                     \n"
"}")
        self.horizontalSlider_conf.setMaximum(99)
        self.horizontalSlider_conf.setSingleStep(1)
        self.horizontalSlider_conf.setPageStep(99)
        self.horizontalSlider_conf.setProperty("value", 30)
        self.horizontalSlider_conf.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_conf.setObjectName("horizontalSlider_conf")
        self.horizontalLayout_5.addWidget(self.horizontalSlider_conf)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.doubleSpinBox_iou = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_iou.setStyleSheet("QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/images/icons/botton_down.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/images/icons/botton_down.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/images/icons/botton_up.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/images/icons/botton_up.png);}")
        self.doubleSpinBox_iou.setMaximum(1.0)
        self.doubleSpinBox_iou.setSingleStep(0.01)
        self.doubleSpinBox_iou.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox_iou.setProperty("value", 0.45)
        self.doubleSpinBox_iou.setObjectName("doubleSpinBox_iou")
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_iou)
        self.horizontalSlider_iou = QtWidgets.QSlider(self.groupBox_5)
        self.horizontalSlider_iou.setStyleSheet("QSlider{\n"
"border-color: #bcbcbc;\n"
"color:#d9d9d9;\n"
"}\n"
"QSlider::groove:horizontal {                                \n"
"     border: 1px solid #999999;                             \n"
"     height: 3px;                                           \n"
"    margin: 0px 0;                                         \n"
"     left: 5px; right: 5px; \n"
" }\n"
"QSlider::handle:horizontal {                               \n"
"     border: 0px ; \n"
"     border-image: url(:/images/icons/point.png);\n"
"     width:15px;\n"
"     margin: -7px -7px -7px -7px;                  \n"
"} \n"
"QSlider::add-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9); \n"
"\n"
"}\n"
"QSlider::sub-page:horizontal{                               \n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);                     \n"
"}")
        self.horizontalSlider_iou.setProperty("value", 45)
        self.horizontalSlider_iou.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_iou.setObjectName("horizontalSlider_iou")
        self.horizontalLayout_6.addWidget(self.horizontalSlider_iou)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.doubleSpinBox_interval = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_interval.setStyleSheet("QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/images/icons/botton_down.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/images/icons/botton_down.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/images/icons/botton_up.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/images/icons/botton_up.png);}")
        self.doubleSpinBox_interval.setDecimals(0)
        self.doubleSpinBox_interval.setMaximum(10.0)
        self.doubleSpinBox_interval.setObjectName("doubleSpinBox_interval")
        self.horizontalLayout_7.addWidget(self.doubleSpinBox_interval)
        self.horizontalSlider_interval = QtWidgets.QSlider(self.groupBox_6)
        self.horizontalSlider_interval.setStyleSheet("QSlider{\n"
"border-color: #bcbcbc;\n"
"color:#d9d9d9;\n"
"}\n"
"QSlider::groove:horizontal {                                \n"
"     border: 1px solid #999999;                             \n"
"     height: 3px;                                           \n"
"    margin: 0px 0;                                         \n"
"     left: 5px; right: 5px; \n"
" }\n"
"QSlider::handle:horizontal {                               \n"
"     border: 0px ; \n"
"     border-image: url(:/images/icons/point.png);\n"
"     width:15px;\n"
"     margin: -7px -7px -7px -7px;                  \n"
"} \n"
"QSlider::add-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:1 #d9d9d9, stop:2 #d9d9d9, stop:3 #d9d9d9, stop:4 #d9d9d9, stop:5 #d9d9d9); \n"
"\n"
"}\n"
"QSlider::sub-page:horizontal{                               \n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);                     \n"
"}")
        self.horizontalSlider_interval.setMaximum(10)
        self.horizontalSlider_interval.setPageStep(1)
        self.horizontalSlider_interval.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_interval.setObjectName("horizontalSlider_interval")
        self.horizontalLayout_7.addWidget(self.horizontalSlider_interval)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_display = QtWidgets.QLabel(self.centralwidget)
        self.label_display.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_display.setText("")
        self.label_display.setObjectName("label_display")
        self.verticalLayout_3.addWidget(self.label_display)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_play = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_play.sizePolicy().hasHeightForWidth())
        self.pushButton_play.setSizePolicy(sizePolicy)
        self.pushButton_play.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_play.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);\n"
"}")
        self.pushButton_play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/pause.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/run.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/pause.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/run.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/pause.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/run.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_play.setIcon(icon1)
        self.pushButton_play.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_play.setCheckable(True)
        self.pushButton_play.setObjectName("pushButton_play")
        self.horizontalLayout_8.addWidget(self.pushButton_play)
        self.progressBar_play = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_play.sizePolicy().hasHeightForWidth())
        self.progressBar_play.setSizePolicy(sizePolicy)
        self.progressBar_play.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar_play.setStyleSheet("QProgressBar{ \n"
"color: rgb(255, 255, 255); \n"
"font:12pt;\n"
" border-radius:2px; \n"
"text-align:center; \n"
"border:none; \n"
"background-color: rgba(215, 215, 215,100);} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background: rgba(55, 55, 55, 200);}")
        self.progressBar_play.setMaximum(1000)
        self.progressBar_play.setProperty("value", 0)
        self.progressBar_play.setFormat("")
        self.progressBar_play.setObjectName("progressBar_play")
        self.horizontalLayout_8.addWidget(self.progressBar_play)
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_stop.sizePolicy().hasHeightForWidth())
        self.pushButton_stop.setSizePolicy(sizePolicy)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_stop.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.pushButton_stop.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_stop.setIcon(icon2)
        self.pushButton_stop.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout_8.addWidget(self.pushButton_stop)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 12)
        self.horizontalLayout_8.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.tableWidget_results = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_results.sizePolicy().hasHeightForWidth())
        self.tableWidget_results.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget_results.setFont(font)
        self.tableWidget_results.setAutoFillBackground(True)
        self.tableWidget_results.setStyleSheet("")
        self.tableWidget_results.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_results.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_results.setObjectName("tableWidget_results")
        self.tableWidget_results.setColumnCount(4)
        self.tableWidget_results.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_results.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_results.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_results.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_results.setHorizontalHeaderItem(3, item)
        self.tableWidget_results.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_results.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_results.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.tableWidget_results)
        self.verticalLayout_3.setStretch(0, 15)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 11)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 16px;\n"
"    font-weight: light;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_status.setText("")
        self.label_status.setObjectName("label_status")
        self.verticalLayout.addWidget(self.label_status)
        self.verticalLayout.setStretch(0, 9)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YOLOv8 GUI"))
        self.groupBox.setTitle(_translate("MainWindow", "Tasks"))
        self.radioButton_det.setText(_translate("MainWindow", "Detection"))
        self.radioButton_seg.setText(_translate("MainWindow", "Segmentation"))
        self.radioButton_pose.setText(_translate("MainWindow", "Pose Estimation"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Models"))
        self.comboBox_model.setItemText(0, _translate("MainWindow", "YOLOv8n"))
        self.comboBox_model.setItemText(1, _translate("MainWindow", "YOLOv8s"))
        self.comboBox_model.setItemText(2, _translate("MainWindow", "YOLOv8m"))
        self.comboBox_model.setItemText(3, _translate("MainWindow", "YOLOv8l"))
        self.comboBox_model.setItemText(4, _translate("MainWindow", "YOLOv8x"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Inputs"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Confidence"))
        self.groupBox_5.setTitle(_translate("MainWindow", "IoU"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Frame Interval"))
        item = self.tableWidget_results.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_results.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Class"))
        item = self.tableWidget_results.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Confidence"))
        item = self.tableWidget_results.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "BBox"))

from src.ui import apprcc_rc
