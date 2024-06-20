# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_infoCiOCpI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QCursor,
    QFont, QIcon)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QVBoxLayout, QWidget)

class BuyWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 500)
        MainWindow.setMinimumSize(QSize(900, 500))
        MainWindow.setMaximumSize(QSize(900, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.item_image = QFrame(self.centralwidget)
        self.item_image.setObjectName(u"item_image")
        self.item_image.setMinimumSize(QSize(500, 500))
        self.item_image.setMaximumSize(QSize(500, 500))
        self.item_image.setStyleSheet(u"border-radius: 12px;")
        self.item_image.setFrameShape(QFrame.Shape.StyledPanel)
        self.item_image.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.item_image)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.item_info = QWidget()
        self.item_info.setObjectName(u"item_info")
        self.item_info.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_9 = QGridLayout(self.item_info)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.scrollArea = QScrollArea(self.item_info)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 374, 703))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(125, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.add_chart = QPushButton(self.frame_4)
        self.add_chart.setObjectName(u"add_chart")
        self.add_chart.setMinimumSize(QSize(30, 30))
        self.add_chart.setMaximumSize(QSize(30, 30))
        self.add_chart.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_chart.setStyleSheet(u"border-radius: 12px;")
        icon = QIcon()
        icon.addFile(u"./views/res/icons/icons8-add-shopping-cart-384.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_chart.setIcon(icon)
        self.add_chart.setIconSize(QSize(22, 22))

        self.gridLayout_6.addWidget(self.add_chart, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_4, 1, 0, 1, 3)

        self.names = QLabel(self.scrollAreaWidgetContents)
        self.names.setObjectName(u"names")
        self.names.setMinimumSize(QSize(0, 70))
        self.names.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(20)
        font.setBold(True)
        self.names.setFont(font)
        self.names.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.names.setScaledContents(True)
        self.names.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.names.setWordWrap(True)

        self.gridLayout_4.addWidget(self.names, 0, 0, 1, 3)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.frame_2.setFont(font1)
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.comments = QListWidget(self.frame_5)
        self.comments.setObjectName(u"comments")
        self.comments.setMinimumSize(QSize(0, 0))
        self.comments.setMaximumSize(QSize(16777215, 16777215))
        self.comments.setFrameShape(QFrame.Shape.NoFrame)

        self.gridLayout_8.addWidget(self.comments, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_5, 2, 0, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_5.setFont(font2)

        self.gridLayout_7.addWidget(self.label_5, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 8, 0, 1, 3)

        self.category = QPushButton(self.scrollAreaWidgetContents)
        self.category.setObjectName(u"category")
        self.category.setMinimumSize(QSize(80, 25))
        self.category.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        self.category.setFont(font3)
        self.category.setCursor(QCursor(Qt.PointingHandCursor))
        self.category.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"padding-left: 10;\n"
"padding-right: 10;")

        self.gridLayout_4.addWidget(self.category, 5, 0, 1, 1)

        self.description = QLabel(self.scrollAreaWidgetContents)
        self.description.setObjectName(u"description")
        self.description.setMinimumSize(QSize(0, 40))
        self.description.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Light"])
        font4.setPointSize(10)
        font4.setItalic(True)
        self.description.setFont(font4)
        self.description.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.description.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.description.setWordWrap(True)

        self.gridLayout_4.addWidget(self.description, 2, 0, 1, 3)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 120))
        self.frame.setMaximumSize(QSize(16777215, 120))
        self.frame.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.variaton1 = QRadioButton(self.frame)
        self.variaton1.setObjectName(u"variaton1")
        self.variaton1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.variaton1, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 4, 0, 1, 1)

        self.variation3 = QRadioButton(self.frame)
        self.variation3.setObjectName(u"variation3")
        self.variation3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.variation3, 4, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 2)

        self.variation2 = QRadioButton(self.frame)
        self.variation2.setObjectName(u"variation2")
        self.variation2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.variation2, 3, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 6, 0, 1, 3)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(12)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.harga_diskon = QLabel(self.frame_3)
        self.harga_diskon.setObjectName(u"harga_diskon")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setStrikeOut(True)
        self.harga_diskon.setFont(font5)
        self.harga_diskon.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_5.addWidget(self.harga_diskon, 0, 0, 1, 1)

        self.presentase_diskon = QLabel(self.frame_3)
        self.presentase_diskon.setObjectName(u"presentase_diskon")
        self.presentase_diskon.setMinimumSize(QSize(80, 25))
        self.presentase_diskon.setMaximumSize(QSize(80, 25))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.presentase_diskon.setFont(font6)
        self.presentase_diskon.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius: 10px;")
        self.presentase_diskon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.presentase_diskon, 0, 2, 1, 1)

        self.harga_item = QLabel(self.frame_3)
        self.harga_item.setObjectName(u"harga_item")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(15)
        font7.setBold(True)
        self.harga_item.setFont(font7)
        self.harga_item.setStyleSheet(u"color: rgb(0, 255, 255);")

        self.gridLayout_5.addWidget(self.harga_item, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(86, 47, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 3, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 4, 0, 1, 3)

        self.frame_14 = QFrame(self.scrollAreaWidgetContents)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 50))
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_14)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(0)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_14)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout_18.addWidget(self.label_2, 0, 0, 1, 1)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_15)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(4, 4, 4, 4)
        self.purchase_amount = QSpinBox(self.frame_15)
        self.purchase_amount.setObjectName(u"purchase_amount")
        self.purchase_amount.setMinimumSize(QSize(0, 30))
        font8 = QFont()
        font8.setBold(True)
        self.purchase_amount.setFont(font8)

        self.gridLayout_19.addWidget(self.purchase_amount, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.frame_15, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_14, 7, 0, 1, 3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_9.addWidget(self.scrollArea, 0, 0, 2, 2)

        self.pushButton = QPushButton(self.item_info)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        self.pushButton.setFont(font8)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.gridLayout_9.addWidget(self.pushButton, 2, 0, 1, 2)

        self.stackedWidget.addWidget(self.item_info)
        self.metode_pembayaran = QWidget()
        self.metode_pembayaran.setObjectName(u"metode_pembayaran")
        self.metode_pembayaran.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QGridLayout(self.metode_pembayaran)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea_2 = QScrollArea(self.metode_pembayaran)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 374, 512))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_7 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        self.frame_7.setFont(font9)
        self.frame_7.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 22))
        self.label.setFont(font2)

        self.gridLayout_12.addWidget(self.label, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 60))
        self.frame_8.setMaximumSize(QSize(16777215, 60))
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_8)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 9, 0, 0)
        self.buy_address = QLabel(self.frame_8)
        self.buy_address.setObjectName(u"buy_address")
        font10 = QFont()
        font10.setFamilies([u"Segoe UI Light"])
        font10.setItalic(True)
        self.buy_address.setFont(font10)
        self.buy_address.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_13.addWidget(self.buy_address, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_8, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_7, 2, 0, 1, 1)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 70))
        self.frame_9.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_9)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout_15.addWidget(self.label_6, 0, 0, 1, 1)

        self.buy_payment = QComboBox(self.frame_9)
        self.buy_payment.setObjectName(u"buy_payment")
        self.buy_payment.setMinimumSize(QSize(0, 30))
        self.buy_payment.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_15.addWidget(self.buy_payment, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_9, 3, 0, 1, 1)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 50))
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        self.frame_10.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_10)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalSpacer_6 = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        font11 = QFont()
        font11.setFamilies([u"Segoe UI Black"])
        font11.setPointSize(12)
        self.label_4.setFont(font11)

        self.gridLayout_14.addWidget(self.label_4, 0, 2, 1, 1)

        self.payment_back = QPushButton(self.frame_10)
        self.payment_back.setObjectName(u"payment_back")
        self.payment_back.setMinimumSize(QSize(70, 30))
        self.payment_back.setMaximumSize(QSize(70, 30))
        self.payment_back.setFont(font8)
        self.payment_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.payment_back.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        icon1 = QIcon()
        icon1.addFile(u"./views/res/icons/icons8-back-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.payment_back.setIcon(icon1)
        self.payment_back.setIconSize(QSize(20, 20))

        self.gridLayout_14.addWidget(self.payment_back, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(120, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_7, 0, 3, 1, 1)


        self.gridLayout_10.addWidget(self.frame_10, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 130))
        self.frame_6.setMaximumSize(QSize(16777215, 130))
        self.frame_6.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.buy_img = QFrame(self.frame_6)
        self.buy_img.setObjectName(u"buy_img")
        self.buy_img.setMinimumSize(QSize(110, 0))
        self.buy_img.setMaximumSize(QSize(110, 16777215))
        self.buy_img.setFrameShape(QFrame.Shape.StyledPanel)
        self.buy_img.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_11.addWidget(self.buy_img, 1, 0, 3, 1)

        self.buy_amount = QLabel(self.frame_6)
        self.buy_amount.setObjectName(u"buy_amount")
        self.buy_amount.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_11.addWidget(self.buy_amount, 3, 1, 1, 1)

        self.buy_variation = QLabel(self.frame_6)
        self.buy_variation.setObjectName(u"buy_variation")
        font12 = QFont()
        font12.setPointSize(8)
        self.buy_variation.setFont(font12)
        self.buy_variation.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_11.addWidget(self.buy_variation, 2, 1, 1, 1)

        self.buy_name = QLabel(self.frame_6)
        self.buy_name.setObjectName(u"buy_name")
        self.buy_name.setMinimumSize(QSize(0, 40))
        self.buy_name.setMaximumSize(QSize(16777215, 40))
        font13 = QFont()
        font13.setFamilies([u"Segoe UI Black"])
        font13.setPointSize(10)
        font13.setBold(True)
        self.buy_name.setFont(font13)
        self.buy_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.buy_name.setWordWrap(True)

        self.gridLayout_11.addWidget(self.buy_name, 1, 1, 1, 1)


        self.gridLayout_10.addWidget(self.frame_6, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 120))
        self.frame_11.setMaximumSize(QSize(16777215, 120))
        self.frame_11.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_11)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout_16.addWidget(self.label_7, 0, 0, 1, 3)

        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        font14 = QFont()
        font14.setFamilies([u"Segoe UI Variable Text"])
        font14.setItalic(True)
        self.label_8.setFont(font14)

        self.gridLayout_16.addWidget(self.label_8, 1, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(195, 19, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_8, 1, 1, 1, 1)

        self.shipping_cost = QLabel(self.frame_11)
        self.shipping_cost.setObjectName(u"shipping_cost")

        self.gridLayout_16.addWidget(self.shipping_cost, 1, 2, 1, 1)

        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font14)

        self.gridLayout_16.addWidget(self.label_10, 2, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(195, 19, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_9, 2, 1, 1, 1)

        self.admin_fees = QLabel(self.frame_11)
        self.admin_fees.setObjectName(u"admin_fees")

        self.gridLayout_16.addWidget(self.admin_fees, 2, 2, 1, 1)

        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font14)

        self.gridLayout_16.addWidget(self.label_12, 3, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(195, 19, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_10, 3, 1, 1, 1)

        self.total_cost = QLabel(self.frame_11)
        self.total_cost.setObjectName(u"total_cost")

        self.gridLayout_16.addWidget(self.total_cost, 3, 2, 1, 1)


        self.gridLayout_10.addWidget(self.frame_11, 4, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.metode_pembayaran)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        self.pushButton_3.setMaximumSize(QSize(16777215, 30))
        self.pushButton_3.setFont(font8)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.metode_pembayaran)
        self.sucess = QWidget()
        self.sucess.setObjectName(u"sucess")
        self.sucess.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.sucess)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_12 = QFrame(self.sucess)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 150))
        self.frame_12.setStyleSheet(u"background-color: transparent;")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sucess_anim = QLabel(self.frame_12)
        self.sucess_anim.setObjectName(u"sucess_anim")
        self.sucess_anim.setMinimumSize(QSize(130, 130))
        self.sucess_anim.setMaximumSize(QSize(130, 130))
        self.sucess_anim.setScaledContents(True)
        self.sucess_anim.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.sucess_anim, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.sucess)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 80))
        self.frame_13.setStyleSheet(u"background-color: transparent;")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_13)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        font15 = QFont()
        font15.setFamilies([u"Segoe UI Black"])
        font15.setPointSize(16)
        font15.setBold(True)
        self.label_15.setFont(font15)
        self.label_15.setStyleSheet(u"color: rgb(85, 255, 0);")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_16 = QLabel(self.frame_13)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.label_16, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_13)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.sucess)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_chart.setText("")
        self.names.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Comments", None))
        self.category.setText(QCoreApplication.translate("MainWindow", u"CATEGORY", None))
        self.description.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.variaton1.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.variation3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Variation", None))
        self.variation2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.harga_diskon.setText(QCoreApplication.translate("MainWindow", u"Rp 130.000", None))
        self.presentase_diskon.setText(QCoreApplication.translate("MainWindow", u"8% OFF", None))
        self.harga_item.setText(QCoreApplication.translate("MainWindow", u"Rp 100.000", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Purchase Amount", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.buy_address.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Payment Method", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PAYMENT", None))
        self.payment_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.buy_amount.setText(QCoreApplication.translate("MainWindow", u"\u00d7 1", None))
        self.buy_variation.setText(QCoreApplication.translate("MainWindow", u"[ VARIATION ]", None))
        self.buy_name.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Total Payment", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Shipping Costs", None))
        self.shipping_cost.setText(QCoreApplication.translate("MainWindow", u"Rp 10.000", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Admin Fees", None))
        self.admin_fees.setText(QCoreApplication.translate("MainWindow", u"Rp 2000", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Total Cost", None))
        self.total_cost.setText(QCoreApplication.translate("MainWindow", u"Rp 0", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.sucess_anim.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"PURCHASE SUCCESSFUL !", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"YOU CAN CLOSE THIS WINDOW!", None))
    # retranslateUi

