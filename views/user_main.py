# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_mainsTLjjZ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QCursor,
    QFont, QIcon)
from PySide6.QtWidgets import (QAbstractScrollArea, QFrame, QGridLayout,
    QLabel, QLineEdit, QListWidget, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QWidget)

class user_MainWindow(object):
    def setupUi(self, user_MainWindow):
        if not user_MainWindow.objectName():
            user_MainWindow.setObjectName(u"user_MainWindow")
        user_MainWindow.resize(1020, 600)
        user_MainWindow.setMinimumSize(QSize(1020, 600))
        self.centralwidget = QWidget(user_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1020, 600))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mini_sidebar = QFrame(self.centralwidget)
        self.mini_sidebar.setObjectName(u"mini_sidebar")
        self.mini_sidebar.setMinimumSize(QSize(55, 0))
        self.mini_sidebar.setMaximumSize(QSize(55, 16777215))
        self.mini_sidebar.setStyleSheet(u"background-color: rgb(239, 40, 91);\n"
"border-bottom-right-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.mini_sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.mini_sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.mini_sidebar)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setContentsMargins(8, 11, 9, 9)
        self.mini_btn_logout = QPushButton(self.mini_sidebar)
        self.mini_btn_logout.setObjectName(u"mini_btn_logout")
        self.mini_btn_logout.setMinimumSize(QSize(40, 40))
        self.mini_btn_logout.setMaximumSize(QSize(40, 40))
        self.mini_btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.mini_btn_logout.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"./views/res/icons/icons8-log-out-384.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"./views/res/icons/icons8-colors-log-out-384.png", QSize(), QIcon.Normal, QIcon.On)
        self.mini_btn_logout.setIcon(icon)
        self.mini_btn_logout.setIconSize(QSize(25, 25))
        self.mini_btn_logout.setCheckable(False)
        self.mini_btn_logout.setAutoRepeat(False)
        self.mini_btn_logout.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.mini_btn_logout, 11, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 9, 0, 1, 1)

        self.mini_btn_order = QPushButton(self.mini_sidebar)
        self.mini_btn_order.setObjectName(u"mini_btn_order")
        self.mini_btn_order.setMinimumSize(QSize(40, 40))
        self.mini_btn_order.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setBold(True)
        self.mini_btn_order.setFont(font)
        self.mini_btn_order.setCursor(QCursor(Qt.PointingHandCursor))
        self.mini_btn_order.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./views/res/icons/icons8-box-500.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u"./views/res/icons/icons8-colors-box-500.png", QSize(), QIcon.Normal, QIcon.On)
        self.mini_btn_order.setIcon(icon1)
        self.mini_btn_order.setIconSize(QSize(25, 25))
        self.mini_btn_order.setCheckable(True)
        self.mini_btn_order.setChecked(False)

        self.gridLayout_5.addWidget(self.mini_btn_order, 7, 0, 1, 1)

        self.logo_2 = QFrame(self.mini_sidebar)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setMinimumSize(QSize(40, 40))
        self.logo_2.setMaximumSize(QSize(40, 40))
        self.logo_2.setStyleSheet(u"border-image: url(./views/res/images/logo.jpeg);\n"
"border-radius: 10px;")
        self.logo_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.logo_2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_5.addWidget(self.logo_2, 1, 0, 1, 1)

        self.mini_btn_search = QPushButton(self.mini_sidebar)
        self.mini_btn_search.setObjectName(u"mini_btn_search")
        self.mini_btn_search.setMinimumSize(QSize(40, 40))
        self.mini_btn_search.setMaximumSize(QSize(40, 40))
        self.mini_btn_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.mini_btn_search.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"./views/res/icons/icons8-search-500.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u"./views/res/icons/icons8-colors-search-500.png", QSize(), QIcon.Normal, QIcon.On)
        self.mini_btn_search.setIcon(icon2)
        self.mini_btn_search.setIconSize(QSize(25, 25))
        self.mini_btn_search.setCheckable(True)

        self.gridLayout_5.addWidget(self.mini_btn_search, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.mini_btn_settings = QPushButton(self.mini_sidebar)
        self.mini_btn_settings.setObjectName(u"mini_btn_settings")
        self.mini_btn_settings.setMinimumSize(QSize(40, 40))
        self.mini_btn_settings.setMaximumSize(QSize(40, 40))
        self.mini_btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.mini_btn_settings.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"./views/res/icons/icons8-setting-500.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u"./views/res/icons/icons8-colors-setting-500.png", QSize(), QIcon.Normal, QIcon.On)
        self.mini_btn_settings.setIcon(icon3)
        self.mini_btn_settings.setIconSize(QSize(25, 25))
        self.mini_btn_settings.setCheckable(True)

        self.gridLayout_5.addWidget(self.mini_btn_settings, 10, 0, 1, 1)

        self.mini_btn_discount = QPushButton(self.mini_sidebar)
        self.mini_btn_discount.setObjectName(u"mini_btn_discount")
        self.mini_btn_discount.setMinimumSize(QSize(40, 40))
        self.mini_btn_discount.setMaximumSize(QSize(40, 40))
        self.mini_btn_discount.setCursor(QCursor(Qt.PointingHandCursor))
        self.mini_btn_discount.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"./views/res/icons/icons8-discount-500.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u"./views/res/icons/icons8-colors-discount-500.png", QSize(), QIcon.Normal, QIcon.On)
        self.mini_btn_discount.setIcon(icon4)
        self.mini_btn_discount.setIconSize(QSize(25, 25))
        self.mini_btn_discount.setCheckable(True)

        self.gridLayout_5.addWidget(self.mini_btn_discount, 5, 0, 1, 1)

        self.mini_btn_home = QPushButton(self.mini_sidebar)
        self.mini_btn_home.setObjectName(u"mini_btn_home")
        self.mini_btn_home.setMinimumSize(QSize(40, 40))
        self.mini_btn_home.setMaximumSize(QSize(40, 40))
        self.mini_btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.mini_btn_home.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"./views/res/icons/icons8-home-500.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u"./views/res/icons/icons8-colors-home-500.png", QSize(), QIcon.Normal, QIcon.On)
        self.mini_btn_home.setIcon(icon5)
        self.mini_btn_home.setIconSize(QSize(25, 25))
        self.mini_btn_home.setCheckable(True)
        self.mini_btn_home.setChecked(True)

        self.gridLayout_5.addWidget(self.mini_btn_home, 3, 0, 1, 1)

        self.mini_btn_new = QPushButton(self.mini_sidebar)
        self.mini_btn_new.setObjectName(u"mini_btn_new")
        self.mini_btn_new.setMinimumSize(QSize(40, 40))
        self.mini_btn_new.setMaximumSize(QSize(16777215, 40))
        self.mini_btn_new.setFont(font)
        self.mini_btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.mini_btn_new.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"./views/res/icons/icons8-new-500.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u"./views/res/icons/icons8-colors-new-500.png", QSize(), QIcon.Normal, QIcon.On)
        self.mini_btn_new.setIcon(icon6)
        self.mini_btn_new.setIconSize(QSize(25, 25))
        self.mini_btn_new.setCheckable(True)
        self.mini_btn_new.setChecked(False)

        self.gridLayout_5.addWidget(self.mini_btn_new, 6, 0, 1, 1)


        self.gridLayout_2.addWidget(self.mini_sidebar, 0, 0, 2, 1)

        self.big_sidebar = QFrame(self.centralwidget)
        self.big_sidebar.setObjectName(u"big_sidebar")
        self.big_sidebar.setMinimumSize(QSize(180, 0))
        self.big_sidebar.setMaximumSize(QSize(180, 16777215))
        self.big_sidebar.setStyleSheet(u"background-color: rgb(239, 40, 91);\n"
"border-bottom-right-radius: 0px;\n"
"border-top-right-radius: 0px;")
        self.big_sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.big_sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.big_sidebar)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setVerticalSpacing(10)
        self.gridLayout_8.setContentsMargins(8, 11, 0, 9)
        self.frame_6 = QFrame(self.big_sidebar)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(8)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.frame_6)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(40, 40))
        self.logo.setMaximumSize(QSize(40, 40))
        self.logo.setStyleSheet(u"border-image: url(./views/res/images/logo.jpeg);\n"
"border-radius: 10px;")
        self.logo.setFrameShape(QFrame.Shape.StyledPanel)
        self.logo.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_9.addWidget(self.logo, 0, 0, 1, 1)

        self.shop_name = QLabel(self.frame_6)
        self.shop_name.setObjectName(u"shop_name")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.shop_name.setFont(font1)
        self.shop_name.setStyleSheet(u"color: rgb(245, 235, 223);")

        self.gridLayout_9.addWidget(self.shop_name, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame_6, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.big_btn_logout = QPushButton(self.big_sidebar)
        self.big_btn_logout.setObjectName(u"big_btn_logout")
        self.big_btn_logout.setMinimumSize(QSize(40, 40))
        self.big_btn_logout.setMaximumSize(QSize(16777215, 40))
        self.big_btn_logout.setFont(font)
        self.big_btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.big_btn_logout.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 10;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-right-width: 0px;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(236, 41, 89);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.big_btn_logout.setIcon(icon)
        self.big_btn_logout.setIconSize(QSize(25, 25))
        self.big_btn_logout.setCheckable(False)
        self.big_btn_logout.setAutoRepeat(False)
        self.big_btn_logout.setAutoExclusive(False)

        self.gridLayout_8.addWidget(self.big_btn_logout, 9, 0, 1, 1)

        self.big_btn_discount = QPushButton(self.big_sidebar)
        self.big_btn_discount.setObjectName(u"big_btn_discount")
        self.big_btn_discount.setMinimumSize(QSize(40, 40))
        self.big_btn_discount.setMaximumSize(QSize(16777215, 40))
        self.big_btn_discount.setFont(font)
        self.big_btn_discount.setCursor(QCursor(Qt.PointingHandCursor))
        self.big_btn_discount.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 10;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-right-width: 0px;\n"
"}\n"
"QPushButton:checked {\n"
"	color: rgb(236, 41, 89);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.big_btn_discount.setIcon(icon4)
        self.big_btn_discount.setIconSize(QSize(25, 25))
        self.big_btn_discount.setCheckable(True)

        self.gridLayout_8.addWidget(self.big_btn_discount, 4, 0, 1, 1)

        self.big_btn_search = QPushButton(self.big_sidebar)
        self.big_btn_search.setObjectName(u"big_btn_search")
        self.big_btn_search.setMinimumSize(QSize(40, 40))
        self.big_btn_search.setMaximumSize(QSize(16777215, 40))
        self.big_btn_search.setFont(font)
        self.big_btn_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.big_btn_search.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 10;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-right-width: 0px;\n"
"}\n"
"QPushButton:checked {\n"
"	color: rgb(236, 41, 89);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.big_btn_search.setIcon(icon2)
        self.big_btn_search.setIconSize(QSize(25, 25))
        self.big_btn_search.setCheckable(True)

        self.gridLayout_8.addWidget(self.big_btn_search, 3, 0, 1, 1)

        self.big_btn_settings = QPushButton(self.big_sidebar)
        self.big_btn_settings.setObjectName(u"big_btn_settings")
        self.big_btn_settings.setMinimumSize(QSize(40, 40))
        self.big_btn_settings.setMaximumSize(QSize(16777215, 40))
        self.big_btn_settings.setFont(font)
        self.big_btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.big_btn_settings.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 10;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-right-width: 0px;\n"
"}\n"
"QPushButton:checked {\n"
"	color: rgb(236, 41, 89);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.big_btn_settings.setIcon(icon3)
        self.big_btn_settings.setIconSize(QSize(25, 25))
        self.big_btn_settings.setCheckable(True)

        self.gridLayout_8.addWidget(self.big_btn_settings, 8, 0, 1, 1)

        self.big_btn_new = QPushButton(self.big_sidebar)
        self.big_btn_new.setObjectName(u"big_btn_new")
        self.big_btn_new.setMinimumSize(QSize(40, 40))
        self.big_btn_new.setMaximumSize(QSize(16777215, 40))
        self.big_btn_new.setFont(font)
        self.big_btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.big_btn_new.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 10;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-right-width: 0px;\n"
"}\n"
"QPushButton:checked {\n"
"	color: rgb(236, 41, 89);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.big_btn_new.setIcon(icon6)
        self.big_btn_new.setIconSize(QSize(25, 25))
        self.big_btn_new.setCheckable(True)

        self.gridLayout_8.addWidget(self.big_btn_new, 5, 0, 1, 1)

        self.big_btn_order = QPushButton(self.big_sidebar)
        self.big_btn_order.setObjectName(u"big_btn_order")
        self.big_btn_order.setMinimumSize(QSize(40, 40))
        self.big_btn_order.setMaximumSize(QSize(16777215, 40))
        self.big_btn_order.setFont(font)
        self.big_btn_order.setCursor(QCursor(Qt.PointingHandCursor))
        self.big_btn_order.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 10;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-right-width: 0px;\n"
"}\n"
"QPushButton:checked {\n"
"	color: rgb(236, 41, 89);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.big_btn_order.setIcon(icon1)
        self.big_btn_order.setIconSize(QSize(25, 25))
        self.big_btn_order.setCheckable(True)

        self.gridLayout_8.addWidget(self.big_btn_order, 6, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.big_btn_home = QPushButton(self.big_sidebar)
        self.big_btn_home.setObjectName(u"big_btn_home")
        self.big_btn_home.setMinimumSize(QSize(40, 40))
        self.big_btn_home.setMaximumSize(QSize(16777215, 40))
        self.big_btn_home.setFont(font)
        self.big_btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.big_btn_home.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
"	color: rgb(0, 0, 0);\n"
"	padding-left: 10;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-right-width: 0px;\n"
"}\n"
"QPushButton:checked {\n"
"	color: rgb(236, 41, 89);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.big_btn_home.setIcon(icon5)
        self.big_btn_home.setIconSize(QSize(25, 25))
        self.big_btn_home.setCheckable(True)
        self.big_btn_home.setChecked(True)

        self.gridLayout_8.addWidget(self.big_btn_home, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.big_sidebar, 0, 1, 2, 1)

        self.navbar = QFrame(self.centralwidget)
        self.navbar.setObjectName(u"navbar")
        self.navbar.setMinimumSize(QSize(0, 60))
        self.navbar.setStyleSheet(u"background-color: rgb(21, 134, 231);\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.navbar.setFrameShape(QFrame.Shape.StyledPanel)
        self.navbar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.navbar)
        self.gridLayout_7.setSpacing(12)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.welcome_frame = QFrame(self.navbar)
        self.welcome_frame.setObjectName(u"welcome_frame")
        self.welcome_frame.setMinimumSize(QSize(100, 0))
        self.welcome_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.welcome_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.welcome_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(9)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.welcome_frame)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Black"])
        font2.setPointSize(8)
        font2.setBold(True)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color: rgb(245, 235, 223);")

        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)

        self.welcome_txt = QLabel(self.welcome_frame)
        self.welcome_txt.setObjectName(u"welcome_txt")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.welcome_txt.setFont(font3)
        self.welcome_txt.setStyleSheet(u"color: rgb(245, 235, 223);")

        self.gridLayout_4.addWidget(self.welcome_txt, 0, 0, 1, 1)

        self.wave_anim = QLabel(self.welcome_frame)
        self.wave_anim.setObjectName(u"wave_anim")
        self.wave_anim.setMinimumSize(QSize(40, 40))
        self.wave_anim.setMaximumSize(QSize(40, 40))

        self.gridLayout_4.addWidget(self.wave_anim, 0, 1, 2, 1)


        self.gridLayout_7.addWidget(self.welcome_frame, 0, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.navbar)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(40, 40))
        self.pushButton_10.setMaximumSize(QSize(40, 40))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"./views/res/icons/icons8-menu-500.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u"./views/res/icons/icons8-back-500.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_10.setIcon(icon7)
        self.pushButton_10.setIconSize(QSize(25, 25))
        self.pushButton_10.setCheckable(True)

        self.gridLayout_7.addWidget(self.pushButton_10, 0, 0, 1, 1)

        self.money = QLabel(self.navbar)
        self.money.setObjectName(u"money")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.money.setFont(font4)
        self.money.setStyleSheet(u"color: rgb(245, 235, 223);")
        self.money.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.money, 0, 3, 1, 1)

        self.profile_img = QFrame(self.navbar)
        self.profile_img.setObjectName(u"profile_img")
        self.profile_img.setMinimumSize(QSize(40, 40))
        self.profile_img.setMaximumSize(QSize(40, 40))
        self.profile_img.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"")
        self.profile_img.setFrameShape(QFrame.Shape.StyledPanel)
        self.profile_img.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.profile_img)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.profiile = QPushButton(self.profile_img)
        self.profiile.setObjectName(u"profiile")
        self.profiile.setMinimumSize(QSize(38, 38))
        self.profiile.setMaximumSize(QSize(38, 38))
        self.profiile.setCursor(QCursor(Qt.PointingHandCursor))
        self.profiile.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 18px;")

        self.gridLayout_6.addWidget(self.profiile, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.profile_img, 0, 6, 1, 1)

        self.btn_wallet = QPushButton(self.navbar)
        self.btn_wallet.setObjectName(u"btn_wallet")
        self.btn_wallet.setMinimumSize(QSize(40, 40))
        self.btn_wallet.setMaximumSize(QSize(40, 40))
        font5 = QFont()
        font5.setPointSize(5)
        self.btn_wallet.setFont(font5)
        self.btn_wallet.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"./views/res/icons/icons8-wallet-500.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u"./views/res/icons/icons8-colors-wallet-500.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_wallet.setIcon(icon8)
        self.btn_wallet.setIconSize(QSize(25, 25))
        self.btn_wallet.setCheckable(True)

        self.gridLayout_7.addWidget(self.btn_wallet, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.chart = QPushButton(self.navbar)
        self.chart.setObjectName(u"chart")
        self.chart.setMinimumSize(QSize(40, 40))
        self.chart.setMaximumSize(QSize(40, 40))
        self.chart.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u"./views/res/icons/icons8-shop-500.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u"./views/res/icons/icons8-shop-500 (1).png", QSize(), QIcon.Normal, QIcon.On)
        self.chart.setIcon(icon9)
        self.chart.setIconSize(QSize(25, 25))
        self.chart.setCheckable(True)

        self.gridLayout_7.addWidget(self.chart, 0, 5, 1, 1)


        self.gridLayout_2.addWidget(self.navbar, 0, 2, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(785, 0))
        self.home.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.home)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.home)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(785, 0))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.main_home = QWidget()
        self.main_home.setObjectName(u"main_home")
        self.main_home.setGeometry(QRect(0, 0, 785, 2329))
        self.main_home.setMinimumSize(QSize(785, 0))
        self.gridLayout_11 = QGridLayout(self.main_home)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(4, 4, 4, 4)
        self.discount_frame = QFrame(self.main_home)
        self.discount_frame.setObjectName(u"discount_frame")
        self.discount_frame.setMinimumSize(QSize(0, 308))
        self.discount_frame.setMaximumSize(QSize(16777215, 308))
        self.discount_frame.setStyleSheet(u"border-radius: 10px;")
        self.discount_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.discount_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.discount_frame)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(0)
        self.gridLayout_12.setVerticalSpacing(6)
        self.gridLayout_12.setContentsMargins(4, 4, 4, 4)
        self.discount_text = QLabel(self.discount_frame)
        self.discount_text.setObjectName(u"discount_text")
        self.discount_text.setMaximumSize(QSize(16777215, 30))
        self.discount_text.setFont(font4)

        self.gridLayout_12.addWidget(self.discount_text, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.discount_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(785, 0))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_7)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.frame_7)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(785, 0))
        self.scrollArea_2.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.scrollArea_2.setStyleSheet(u"QScrollBar:horizontal {\n"
"        border: none;\n"
"        height: 10px;\n"
"        margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"		background-color: rgb(237, 41, 89);\n"
"       min-width: 10px;\n"
"		border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"        border: none;\n"
"        background: none;\n"
"        width: 0px;\n"
"}")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1402, 266))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 8)
        self.frame_8 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 250))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_8)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setVerticalSpacing(0)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.disc_itm_4 = QFrame(self.frame_8)
        self.disc_itm_4.setObjectName(u"disc_itm_4")
        self.disc_itm_4.setMinimumSize(QSize(170, 250))
        self.disc_itm_4.setMaximumSize(QSize(170, 250))
        self.disc_itm_4.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.disc_itm_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.disc_itm_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_28 = QGridLayout(self.disc_itm_4)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.image_6 = QFrame(self.disc_itm_4)
        self.image_6.setObjectName(u"image_6")
        self.image_6.setMinimumSize(QSize(0, 168))
        self.image_6.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_6.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_28.addWidget(self.image_6, 0, 0, 1, 1)

        self.frame_22 = QFrame(self.disc_itm_4)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"border-width: 0px;")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_22)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setHorizontalSpacing(0)
        self.gridLayout_29.setVerticalSpacing(2)
        self.gridLayout_29.setContentsMargins(4, 0, 4, 4)
        self.disc_label_6 = QLabel(self.frame_22)
        self.disc_label_6.setObjectName(u"disc_label_6")
        self.disc_label_6.setMaximumSize(QSize(55, 16777215))
        font6 = QFont()
        font6.setPointSize(6)
        font6.setStrikeOut(True)
        self.disc_label_6.setFont(font6)
        self.disc_label_6.setStyleSheet(u"color: rgb(85, 0, 255);")
        self.disc_label_6.setScaledContents(False)

        self.gridLayout_29.addWidget(self.disc_label_6, 1, 0, 1, 1)

        self.price_6 = QLabel(self.frame_22)
        self.price_6.setObjectName(u"price_6")
        self.price_6.setFont(font)
        self.price_6.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_29.addWidget(self.price_6, 1, 1, 1, 1)

        self.produc_name_6 = QLabel(self.frame_22)
        self.produc_name_6.setObjectName(u"produc_name_6")
        self.produc_name_6.setScaledContents(False)
        self.produc_name_6.setWordWrap(False)

        self.gridLayout_29.addWidget(self.produc_name_6, 0, 0, 1, 2)

        self.buy_btn_6 = QPushButton(self.frame_22)
        self.buy_btn_6.setObjectName(u"buy_btn_6")
        self.buy_btn_6.setMinimumSize(QSize(0, 22))
        font7 = QFont()
        font7.setPointSize(8)
        font7.setBold(True)
        self.buy_btn_6.setFont(font7)
        self.buy_btn_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_btn_6.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_29.addWidget(self.buy_btn_6, 2, 0, 1, 2)


        self.gridLayout_28.addWidget(self.frame_22, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.disc_itm_4, 0, 4, 1, 1)

        self.disc_itm_2 = QFrame(self.frame_8)
        self.disc_itm_2.setObjectName(u"disc_itm_2")
        self.disc_itm_2.setMinimumSize(QSize(170, 250))
        self.disc_itm_2.setMaximumSize(QSize(170, 250))
        self.disc_itm_2.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.disc_itm_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.disc_itm_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_24 = QGridLayout(self.disc_itm_2)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.image_4 = QFrame(self.disc_itm_2)
        self.image_4.setObjectName(u"image_4")
        self.image_4.setMinimumSize(QSize(0, 168))
        self.image_4.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_4.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_24.addWidget(self.image_4, 0, 0, 1, 1)

        self.frame_20 = QFrame(self.disc_itm_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"border-width: 0px;")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_20)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(0)
        self.gridLayout_25.setVerticalSpacing(2)
        self.gridLayout_25.setContentsMargins(4, 0, 4, 4)
        self.disc_label_4 = QLabel(self.frame_20)
        self.disc_label_4.setObjectName(u"disc_label_4")
        self.disc_label_4.setMaximumSize(QSize(55, 16777215))
        self.disc_label_4.setFont(font6)
        self.disc_label_4.setStyleSheet(u"color: rgb(85, 0, 255);")
        self.disc_label_4.setScaledContents(False)

        self.gridLayout_25.addWidget(self.disc_label_4, 1, 0, 1, 1)

        self.price_4 = QLabel(self.frame_20)
        self.price_4.setObjectName(u"price_4")
        self.price_4.setFont(font)
        self.price_4.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_25.addWidget(self.price_4, 1, 1, 1, 1)

        self.produc_name_4 = QLabel(self.frame_20)
        self.produc_name_4.setObjectName(u"produc_name_4")
        self.produc_name_4.setScaledContents(False)
        self.produc_name_4.setWordWrap(False)

        self.gridLayout_25.addWidget(self.produc_name_4, 0, 0, 1, 2)

        self.buy_btn_4 = QPushButton(self.frame_20)
        self.buy_btn_4.setObjectName(u"buy_btn_4")
        self.buy_btn_4.setMinimumSize(QSize(0, 22))
        self.buy_btn_4.setFont(font7)
        self.buy_btn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_btn_4.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_25.addWidget(self.buy_btn_4, 2, 0, 1, 2)


        self.gridLayout_24.addWidget(self.frame_20, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.disc_itm_2, 0, 2, 1, 1)

        self.disc_itm_3 = QFrame(self.frame_8)
        self.disc_itm_3.setObjectName(u"disc_itm_3")
        self.disc_itm_3.setMinimumSize(QSize(170, 250))
        self.disc_itm_3.setMaximumSize(QSize(170, 250))
        self.disc_itm_3.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.disc_itm_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.disc_itm_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_26 = QGridLayout(self.disc_itm_3)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.image_5 = QFrame(self.disc_itm_3)
        self.image_5.setObjectName(u"image_5")
        self.image_5.setMinimumSize(QSize(0, 168))
        self.image_5.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_5.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_26.addWidget(self.image_5, 0, 0, 1, 1)

        self.frame_21 = QFrame(self.disc_itm_3)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"border-width: 0px;")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_21)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setHorizontalSpacing(0)
        self.gridLayout_27.setVerticalSpacing(2)
        self.gridLayout_27.setContentsMargins(4, 0, 4, 4)
        self.disc_label_5 = QLabel(self.frame_21)
        self.disc_label_5.setObjectName(u"disc_label_5")
        self.disc_label_5.setMaximumSize(QSize(55, 16777215))
        self.disc_label_5.setFont(font6)
        self.disc_label_5.setStyleSheet(u"color: rgb(85, 0, 255);")
        self.disc_label_5.setScaledContents(False)

        self.gridLayout_27.addWidget(self.disc_label_5, 1, 0, 1, 1)

        self.price_5 = QLabel(self.frame_21)
        self.price_5.setObjectName(u"price_5")
        self.price_5.setFont(font)
        self.price_5.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_27.addWidget(self.price_5, 1, 1, 1, 1)

        self.produc_name_5 = QLabel(self.frame_21)
        self.produc_name_5.setObjectName(u"produc_name_5")
        self.produc_name_5.setScaledContents(False)
        self.produc_name_5.setWordWrap(False)

        self.gridLayout_27.addWidget(self.produc_name_5, 0, 0, 1, 2)

        self.buy_btn_5 = QPushButton(self.frame_21)
        self.buy_btn_5.setObjectName(u"buy_btn_5")
        self.buy_btn_5.setMinimumSize(QSize(0, 22))
        self.buy_btn_5.setFont(font7)
        self.buy_btn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_btn_5.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_27.addWidget(self.buy_btn_5, 2, 0, 1, 2)


        self.gridLayout_26.addWidget(self.frame_21, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.disc_itm_3, 0, 3, 1, 1)

        self.disc_itm_6 = QFrame(self.frame_8)
        self.disc_itm_6.setObjectName(u"disc_itm_6")
        self.disc_itm_6.setMinimumSize(QSize(170, 250))
        self.disc_itm_6.setMaximumSize(QSize(170, 250))
        self.disc_itm_6.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.disc_itm_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.disc_itm_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_32 = QGridLayout(self.disc_itm_6)
        self.gridLayout_32.setSpacing(0)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.image_8 = QFrame(self.disc_itm_6)
        self.image_8.setObjectName(u"image_8")
        self.image_8.setMinimumSize(QSize(0, 168))
        self.image_8.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_8.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_32.addWidget(self.image_8, 0, 0, 1, 1)

        self.frame_24 = QFrame(self.disc_itm_6)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"border-width: 0px;")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_24)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setHorizontalSpacing(0)
        self.gridLayout_33.setVerticalSpacing(2)
        self.gridLayout_33.setContentsMargins(4, 0, 4, 4)
        self.disc_label_8 = QLabel(self.frame_24)
        self.disc_label_8.setObjectName(u"disc_label_8")
        self.disc_label_8.setMaximumSize(QSize(55, 16777215))
        self.disc_label_8.setFont(font6)
        self.disc_label_8.setStyleSheet(u"color: rgb(85, 0, 255);")
        self.disc_label_8.setScaledContents(False)

        self.gridLayout_33.addWidget(self.disc_label_8, 1, 0, 1, 1)

        self.price_8 = QLabel(self.frame_24)
        self.price_8.setObjectName(u"price_8")
        self.price_8.setFont(font)
        self.price_8.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_33.addWidget(self.price_8, 1, 1, 1, 1)

        self.produc_name_8 = QLabel(self.frame_24)
        self.produc_name_8.setObjectName(u"produc_name_8")
        self.produc_name_8.setScaledContents(False)
        self.produc_name_8.setWordWrap(False)

        self.gridLayout_33.addWidget(self.produc_name_8, 0, 0, 1, 2)

        self.buy_btn_8 = QPushButton(self.frame_24)
        self.buy_btn_8.setObjectName(u"buy_btn_8")
        self.buy_btn_8.setMinimumSize(QSize(0, 22))
        self.buy_btn_8.setFont(font7)
        self.buy_btn_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_btn_8.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_33.addWidget(self.buy_btn_8, 2, 0, 1, 2)


        self.gridLayout_32.addWidget(self.frame_24, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.disc_itm_6, 0, 6, 1, 1)

        self.disc_itm_7 = QFrame(self.frame_8)
        self.disc_itm_7.setObjectName(u"disc_itm_7")
        self.disc_itm_7.setMinimumSize(QSize(170, 250))
        self.disc_itm_7.setMaximumSize(QSize(170, 250))
        self.disc_itm_7.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.disc_itm_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.disc_itm_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_116 = QGridLayout(self.disc_itm_7)
        self.gridLayout_116.setSpacing(0)
        self.gridLayout_116.setObjectName(u"gridLayout_116")
        self.gridLayout_116.setContentsMargins(0, 0, 0, 0)
        self.image_9 = QFrame(self.disc_itm_7)
        self.image_9.setObjectName(u"image_9")
        self.image_9.setMinimumSize(QSize(0, 168))
        self.image_9.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_9.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_116.addWidget(self.image_9, 0, 0, 1, 1)

        self.frame_25 = QFrame(self.disc_itm_7)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"border-width: 0px;")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_117 = QGridLayout(self.frame_25)
        self.gridLayout_117.setObjectName(u"gridLayout_117")
        self.gridLayout_117.setHorizontalSpacing(0)
        self.gridLayout_117.setVerticalSpacing(2)
        self.gridLayout_117.setContentsMargins(4, 0, 4, 4)
        self.disc_label_9 = QLabel(self.frame_25)
        self.disc_label_9.setObjectName(u"disc_label_9")
        self.disc_label_9.setMaximumSize(QSize(55, 16777215))
        self.disc_label_9.setFont(font6)
        self.disc_label_9.setStyleSheet(u"color: rgb(85, 0, 255);")
        self.disc_label_9.setScaledContents(False)

        self.gridLayout_117.addWidget(self.disc_label_9, 1, 0, 1, 1)

        self.price_9 = QLabel(self.frame_25)
        self.price_9.setObjectName(u"price_9")
        self.price_9.setFont(font)
        self.price_9.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_117.addWidget(self.price_9, 1, 1, 1, 1)

        self.produc_name_9 = QLabel(self.frame_25)
        self.produc_name_9.setObjectName(u"produc_name_9")
        self.produc_name_9.setScaledContents(False)
        self.produc_name_9.setWordWrap(False)

        self.gridLayout_117.addWidget(self.produc_name_9, 0, 0, 1, 2)

        self.buy_btn_9 = QPushButton(self.frame_25)
        self.buy_btn_9.setObjectName(u"buy_btn_9")
        self.buy_btn_9.setMinimumSize(QSize(0, 22))
        self.buy_btn_9.setFont(font7)
        self.buy_btn_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_btn_9.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_117.addWidget(self.buy_btn_9, 2, 0, 1, 2)


        self.gridLayout_116.addWidget(self.frame_25, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.disc_itm_7, 0, 7, 1, 1)

        self.disc_itm_5 = QFrame(self.frame_8)
        self.disc_itm_5.setObjectName(u"disc_itm_5")
        self.disc_itm_5.setMinimumSize(QSize(170, 250))
        self.disc_itm_5.setMaximumSize(QSize(170, 250))
        self.disc_itm_5.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.disc_itm_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.disc_itm_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_30 = QGridLayout(self.disc_itm_5)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.image_7 = QFrame(self.disc_itm_5)
        self.image_7.setObjectName(u"image_7")
        self.image_7.setMinimumSize(QSize(0, 168))
        self.image_7.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_7.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_30.addWidget(self.image_7, 0, 0, 1, 1)

        self.frame_23 = QFrame(self.disc_itm_5)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"border-width: 0px;")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_23)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setHorizontalSpacing(0)
        self.gridLayout_31.setVerticalSpacing(2)
        self.gridLayout_31.setContentsMargins(4, 0, 4, 4)
        self.disc_label_7 = QLabel(self.frame_23)
        self.disc_label_7.setObjectName(u"disc_label_7")
        self.disc_label_7.setMaximumSize(QSize(55, 16777215))
        self.disc_label_7.setFont(font6)
        self.disc_label_7.setStyleSheet(u"color: rgb(85, 0, 255);")
        self.disc_label_7.setScaledContents(False)

        self.gridLayout_31.addWidget(self.disc_label_7, 1, 0, 1, 1)

        self.price_7 = QLabel(self.frame_23)
        self.price_7.setObjectName(u"price_7")
        self.price_7.setFont(font)
        self.price_7.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_31.addWidget(self.price_7, 1, 1, 1, 1)

        self.produc_name_7 = QLabel(self.frame_23)
        self.produc_name_7.setObjectName(u"produc_name_7")
        self.produc_name_7.setScaledContents(False)
        self.produc_name_7.setWordWrap(False)

        self.gridLayout_31.addWidget(self.produc_name_7, 0, 0, 1, 2)

        self.buy_btn_7 = QPushButton(self.frame_23)
        self.buy_btn_7.setObjectName(u"buy_btn_7")
        self.buy_btn_7.setMinimumSize(QSize(0, 22))
        self.buy_btn_7.setFont(font7)
        self.buy_btn_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_btn_7.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_31.addWidget(self.buy_btn_7, 2, 0, 1, 2)


        self.gridLayout_30.addWidget(self.frame_23, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.disc_itm_5, 0, 5, 1, 1)

        self.disc_itm = QFrame(self.frame_8)
        self.disc_itm.setObjectName(u"disc_itm")
        self.disc_itm.setMinimumSize(QSize(170, 250))
        self.disc_itm.setMaximumSize(QSize(170, 250))
        self.disc_itm.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.disc_itm.setFrameShape(QFrame.Shape.StyledPanel)
        self.disc_itm.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_16 = QGridLayout(self.disc_itm)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.image = QFrame(self.disc_itm)
        self.image.setObjectName(u"image")
        self.image.setMinimumSize(QSize(0, 168))
        self.image.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image.setFrameShape(QFrame.Shape.StyledPanel)
        self.image.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_16.addWidget(self.image, 0, 0, 1, 1)

        self.frame_17 = QFrame(self.disc_itm)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"border-width: 0px;")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_17)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(0)
        self.gridLayout_18.setVerticalSpacing(2)
        self.gridLayout_18.setContentsMargins(4, 0, 4, 4)
        self.disc_label = QLabel(self.frame_17)
        self.disc_label.setObjectName(u"disc_label")
        self.disc_label.setMaximumSize(QSize(55, 16777215))
        self.disc_label.setFont(font6)
        self.disc_label.setStyleSheet(u"color: rgb(85, 0, 255);")
        self.disc_label.setScaledContents(False)

        self.gridLayout_18.addWidget(self.disc_label, 1, 0, 1, 1)

        self.price = QLabel(self.frame_17)
        self.price.setObjectName(u"price")
        self.price.setFont(font)
        self.price.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_18.addWidget(self.price, 1, 1, 1, 1)

        self.produc_name = QLabel(self.frame_17)
        self.produc_name.setObjectName(u"produc_name")
        self.produc_name.setScaledContents(False)
        self.produc_name.setWordWrap(False)

        self.gridLayout_18.addWidget(self.produc_name, 0, 0, 1, 2)

        self.buy_btn = QPushButton(self.frame_17)
        self.buy_btn.setObjectName(u"buy_btn")
        self.buy_btn.setMinimumSize(QSize(0, 22))
        self.buy_btn.setFont(font7)
        self.buy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_btn.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_18.addWidget(self.buy_btn, 2, 0, 1, 2)


        self.gridLayout_16.addWidget(self.frame_17, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.disc_itm, 0, 1, 1, 1)

        self.disc_itm_8 = QFrame(self.frame_8)
        self.disc_itm_8.setObjectName(u"disc_itm_8")
        self.disc_itm_8.setMinimumSize(QSize(170, 250))
        self.disc_itm_8.setMaximumSize(QSize(170, 250))
        self.disc_itm_8.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.disc_itm_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.disc_itm_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_118 = QGridLayout(self.disc_itm_8)
        self.gridLayout_118.setSpacing(0)
        self.gridLayout_118.setObjectName(u"gridLayout_118")
        self.gridLayout_118.setContentsMargins(0, 0, 0, 0)
        self.image_10 = QFrame(self.disc_itm_8)
        self.image_10.setObjectName(u"image_10")
        self.image_10.setMinimumSize(QSize(0, 168))
        self.image_10.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_10.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_118.addWidget(self.image_10, 0, 0, 1, 1)

        self.frame_26 = QFrame(self.disc_itm_8)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"border-width: 0px;")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_119 = QGridLayout(self.frame_26)
        self.gridLayout_119.setObjectName(u"gridLayout_119")
        self.gridLayout_119.setHorizontalSpacing(0)
        self.gridLayout_119.setVerticalSpacing(2)
        self.gridLayout_119.setContentsMargins(4, 0, 4, 4)
        self.disc_label_10 = QLabel(self.frame_26)
        self.disc_label_10.setObjectName(u"disc_label_10")
        self.disc_label_10.setMaximumSize(QSize(55, 16777215))
        self.disc_label_10.setFont(font6)
        self.disc_label_10.setStyleSheet(u"color: rgb(85, 0, 255);")
        self.disc_label_10.setScaledContents(False)

        self.gridLayout_119.addWidget(self.disc_label_10, 1, 0, 1, 1)

        self.price_10 = QLabel(self.frame_26)
        self.price_10.setObjectName(u"price_10")
        self.price_10.setFont(font)
        self.price_10.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_119.addWidget(self.price_10, 1, 1, 1, 1)

        self.produc_name_10 = QLabel(self.frame_26)
        self.produc_name_10.setObjectName(u"produc_name_10")
        self.produc_name_10.setScaledContents(False)
        self.produc_name_10.setWordWrap(False)

        self.gridLayout_119.addWidget(self.produc_name_10, 0, 0, 1, 2)

        self.buy_btn_10 = QPushButton(self.frame_26)
        self.buy_btn_10.setObjectName(u"buy_btn_10")
        self.buy_btn_10.setMinimumSize(QSize(0, 22))
        self.buy_btn_10.setFont(font7)
        self.buy_btn_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_btn_10.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_119.addWidget(self.buy_btn_10, 2, 0, 1, 2)


        self.gridLayout_118.addWidget(self.frame_26, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.disc_itm_8, 0, 8, 1, 1)


        self.gridLayout_10.addWidget(self.frame_8, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_13.addWidget(self.scrollArea_2, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_7, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.discount_frame, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.main_home)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setStyleSheet(u"border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFont(font4)

        self.gridLayout_14.addWidget(self.label_2, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.recomended_2 = QFrame(self.frame_3)
        self.recomended_2.setObjectName(u"recomended_2")
        self.recomended_2.setMaximumSize(QSize(16777215, 192))
        self.recomended_2.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_136 = QGridLayout(self.recomended_2)
        self.gridLayout_136.setSpacing(0)
        self.gridLayout_136.setObjectName(u"gridLayout_136")
        self.gridLayout_136.setContentsMargins(0, 0, 0, 0)
        self.image_produc_26 = QFrame(self.recomended_2)
        self.image_produc_26.setObjectName(u"image_produc_26")
        self.image_produc_26.setMinimumSize(QSize(190, 190))
        self.image_produc_26.setMaximumSize(QSize(190, 190))
        self.image_produc_26.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_26.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_136.addWidget(self.image_produc_26, 0, 0, 1, 1)

        self.frame_85 = QFrame(self.recomended_2)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(188, 0))
        self.frame_85.setStyleSheet(u"border-width: 0px;")
        self.frame_85.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_137 = QGridLayout(self.frame_85)
        self.gridLayout_137.setObjectName(u"gridLayout_137")
        self.gridLayout_137.setHorizontalSpacing(0)
        self.gridLayout_137.setVerticalSpacing(16)
        self.produk_26 = QLabel(self.frame_85)
        self.produk_26.setObjectName(u"produk_26")
        self.produk_26.setMaximumSize(QSize(16777215, 60))
        font8 = QFont()
        font8.setPointSize(9)
        self.produk_26.setFont(font8)
        self.produk_26.setScaledContents(True)
        self.produk_26.setWordWrap(True)

        self.gridLayout_137.addWidget(self.produk_26, 0, 0, 1, 4)

        self.diskon_26 = QPushButton(self.frame_85)
        self.diskon_26.setObjectName(u"diskon_26")
        font9 = QFont()
        font9.setItalic(True)
        self.diskon_26.setFont(font9)
        self.diskon_26.setStyleSheet(u"color: rgb(21, 134, 231);")
        icon10 = QIcon()
        icon10.addFile(u"./views/res/icons/icons8-discount-480.png", QSize(), QIcon.Normal, QIcon.Off)
        self.diskon_26.setIcon(icon10)
        self.diskon_26.setIconSize(QSize(20, 20))

        self.gridLayout_137.addWidget(self.diskon_26, 1, 2, 1, 1)

        self.harga_26 = QLabel(self.frame_85)
        self.harga_26.setObjectName(u"harga_26")
        self.harga_26.setMaximumSize(QSize(16777215, 30))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(12)
        font10.setBold(True)
        self.harga_26.setFont(font10)
        self.harga_26.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_137.addWidget(self.harga_26, 1, 0, 1, 1)

        self.tombol_26 = QPushButton(self.frame_85)
        self.tombol_26.setObjectName(u"tombol_26")
        self.tombol_26.setMinimumSize(QSize(0, 40))
        self.tombol_26.setFont(font4)
        self.tombol_26.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_26.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_137.addWidget(self.tombol_26, 2, 0, 1, 4)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_137.addItem(self.horizontalSpacer_27, 1, 1, 1, 1)


        self.gridLayout_136.addWidget(self.frame_85, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_2, 0, 1, 1, 1)

        self.recomended_18 = QFrame(self.frame_3)
        self.recomended_18.setObjectName(u"recomended_18")
        self.recomended_18.setMaximumSize(QSize(16777215, 192))
        self.recomended_18.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_18.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_168 = QGridLayout(self.recomended_18)
        self.gridLayout_168.setSpacing(0)
        self.gridLayout_168.setObjectName(u"gridLayout_168")
        self.gridLayout_168.setContentsMargins(0, 0, 0, 0)
        self.image_produc_42 = QFrame(self.recomended_18)
        self.image_produc_42.setObjectName(u"image_produc_42")
        self.image_produc_42.setMinimumSize(QSize(190, 190))
        self.image_produc_42.setMaximumSize(QSize(190, 190))
        self.image_produc_42.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_42.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_168.addWidget(self.image_produc_42, 0, 0, 1, 1)

        self.frame_101 = QFrame(self.recomended_18)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMinimumSize(QSize(188, 0))
        self.frame_101.setStyleSheet(u"border-width: 0px;")
        self.frame_101.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_169 = QGridLayout(self.frame_101)
        self.gridLayout_169.setObjectName(u"gridLayout_169")
        self.gridLayout_169.setHorizontalSpacing(0)
        self.gridLayout_169.setVerticalSpacing(16)
        self.produk_42 = QLabel(self.frame_101)
        self.produk_42.setObjectName(u"produk_42")
        self.produk_42.setMaximumSize(QSize(16777215, 60))
        self.produk_42.setFont(font8)
        self.produk_42.setScaledContents(True)
        self.produk_42.setWordWrap(True)

        self.gridLayout_169.addWidget(self.produk_42, 0, 0, 1, 4)

        self.diskon_42 = QPushButton(self.frame_101)
        self.diskon_42.setObjectName(u"diskon_42")
        self.diskon_42.setFont(font9)
        self.diskon_42.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_42.setIcon(icon10)
        self.diskon_42.setIconSize(QSize(20, 20))

        self.gridLayout_169.addWidget(self.diskon_42, 1, 2, 1, 1)

        self.harga_42 = QLabel(self.frame_101)
        self.harga_42.setObjectName(u"harga_42")
        self.harga_42.setMaximumSize(QSize(16777215, 30))
        self.harga_42.setFont(font10)
        self.harga_42.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_169.addWidget(self.harga_42, 1, 0, 1, 1)

        self.tombol_42 = QPushButton(self.frame_101)
        self.tombol_42.setObjectName(u"tombol_42")
        self.tombol_42.setMinimumSize(QSize(0, 40))
        self.tombol_42.setFont(font4)
        self.tombol_42.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_42.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_169.addWidget(self.tombol_42, 2, 0, 1, 4)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_169.addItem(self.horizontalSpacer_43, 1, 1, 1, 1)


        self.gridLayout_168.addWidget(self.frame_101, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_18, 8, 1, 1, 1)

        self.recomended_3 = QFrame(self.frame_3)
        self.recomended_3.setObjectName(u"recomended_3")
        self.recomended_3.setMaximumSize(QSize(16777215, 192))
        self.recomended_3.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_138 = QGridLayout(self.recomended_3)
        self.gridLayout_138.setSpacing(0)
        self.gridLayout_138.setObjectName(u"gridLayout_138")
        self.gridLayout_138.setContentsMargins(0, 0, 0, 0)
        self.image_produc_27 = QFrame(self.recomended_3)
        self.image_produc_27.setObjectName(u"image_produc_27")
        self.image_produc_27.setMinimumSize(QSize(190, 190))
        self.image_produc_27.setMaximumSize(QSize(190, 190))
        self.image_produc_27.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_27.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_138.addWidget(self.image_produc_27, 0, 0, 1, 1)

        self.frame_86 = QFrame(self.recomended_3)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(188, 0))
        self.frame_86.setStyleSheet(u"border-width: 0px;")
        self.frame_86.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_139 = QGridLayout(self.frame_86)
        self.gridLayout_139.setObjectName(u"gridLayout_139")
        self.gridLayout_139.setHorizontalSpacing(0)
        self.gridLayout_139.setVerticalSpacing(16)
        self.produk_27 = QLabel(self.frame_86)
        self.produk_27.setObjectName(u"produk_27")
        self.produk_27.setMaximumSize(QSize(16777215, 60))
        self.produk_27.setFont(font8)
        self.produk_27.setScaledContents(True)
        self.produk_27.setWordWrap(True)

        self.gridLayout_139.addWidget(self.produk_27, 0, 0, 1, 4)

        self.diskon_27 = QPushButton(self.frame_86)
        self.diskon_27.setObjectName(u"diskon_27")
        self.diskon_27.setFont(font9)
        self.diskon_27.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_27.setIcon(icon10)
        self.diskon_27.setIconSize(QSize(20, 20))

        self.gridLayout_139.addWidget(self.diskon_27, 1, 2, 1, 1)

        self.harga_27 = QLabel(self.frame_86)
        self.harga_27.setObjectName(u"harga_27")
        self.harga_27.setMaximumSize(QSize(16777215, 30))
        self.harga_27.setFont(font10)
        self.harga_27.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_139.addWidget(self.harga_27, 1, 0, 1, 1)

        self.tombol_27 = QPushButton(self.frame_86)
        self.tombol_27.setObjectName(u"tombol_27")
        self.tombol_27.setMinimumSize(QSize(0, 40))
        self.tombol_27.setFont(font4)
        self.tombol_27.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_27.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_139.addWidget(self.tombol_27, 2, 0, 1, 4)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_139.addItem(self.horizontalSpacer_28, 1, 1, 1, 1)


        self.gridLayout_138.addWidget(self.frame_86, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_3, 1, 0, 1, 1)

        self.recomended_7 = QFrame(self.frame_3)
        self.recomended_7.setObjectName(u"recomended_7")
        self.recomended_7.setMaximumSize(QSize(16777215, 192))
        self.recomended_7.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_146 = QGridLayout(self.recomended_7)
        self.gridLayout_146.setSpacing(0)
        self.gridLayout_146.setObjectName(u"gridLayout_146")
        self.gridLayout_146.setContentsMargins(0, 0, 0, 0)
        self.image_produc_31 = QFrame(self.recomended_7)
        self.image_produc_31.setObjectName(u"image_produc_31")
        self.image_produc_31.setMinimumSize(QSize(190, 190))
        self.image_produc_31.setMaximumSize(QSize(190, 190))
        self.image_produc_31.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_31.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_146.addWidget(self.image_produc_31, 0, 0, 1, 1)

        self.frame_90 = QFrame(self.recomended_7)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(188, 0))
        self.frame_90.setStyleSheet(u"border-width: 0px;")
        self.frame_90.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_147 = QGridLayout(self.frame_90)
        self.gridLayout_147.setObjectName(u"gridLayout_147")
        self.gridLayout_147.setHorizontalSpacing(0)
        self.gridLayout_147.setVerticalSpacing(16)
        self.produk_31 = QLabel(self.frame_90)
        self.produk_31.setObjectName(u"produk_31")
        self.produk_31.setMaximumSize(QSize(16777215, 60))
        self.produk_31.setFont(font8)
        self.produk_31.setScaledContents(True)
        self.produk_31.setWordWrap(True)

        self.gridLayout_147.addWidget(self.produk_31, 0, 0, 1, 4)

        self.diskon_31 = QPushButton(self.frame_90)
        self.diskon_31.setObjectName(u"diskon_31")
        self.diskon_31.setFont(font9)
        self.diskon_31.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_31.setIcon(icon10)
        self.diskon_31.setIconSize(QSize(20, 20))

        self.gridLayout_147.addWidget(self.diskon_31, 1, 2, 1, 1)

        self.harga_31 = QLabel(self.frame_90)
        self.harga_31.setObjectName(u"harga_31")
        self.harga_31.setMaximumSize(QSize(16777215, 30))
        self.harga_31.setFont(font10)
        self.harga_31.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_147.addWidget(self.harga_31, 1, 0, 1, 1)

        self.tombol_31 = QPushButton(self.frame_90)
        self.tombol_31.setObjectName(u"tombol_31")
        self.tombol_31.setMinimumSize(QSize(0, 40))
        self.tombol_31.setFont(font4)
        self.tombol_31.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_31.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_147.addWidget(self.tombol_31, 2, 0, 1, 4)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_147.addItem(self.horizontalSpacer_32, 1, 1, 1, 1)


        self.gridLayout_146.addWidget(self.frame_90, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_7, 3, 0, 1, 1)

        self.recomended_16 = QFrame(self.frame_3)
        self.recomended_16.setObjectName(u"recomended_16")
        self.recomended_16.setMaximumSize(QSize(16777215, 192))
        self.recomended_16.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_16.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_164 = QGridLayout(self.recomended_16)
        self.gridLayout_164.setSpacing(0)
        self.gridLayout_164.setObjectName(u"gridLayout_164")
        self.gridLayout_164.setContentsMargins(0, 0, 0, 0)
        self.image_produc_40 = QFrame(self.recomended_16)
        self.image_produc_40.setObjectName(u"image_produc_40")
        self.image_produc_40.setMinimumSize(QSize(190, 190))
        self.image_produc_40.setMaximumSize(QSize(190, 190))
        self.image_produc_40.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_40.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_164.addWidget(self.image_produc_40, 0, 0, 1, 1)

        self.frame_99 = QFrame(self.recomended_16)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(188, 0))
        self.frame_99.setStyleSheet(u"border-width: 0px;")
        self.frame_99.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_165 = QGridLayout(self.frame_99)
        self.gridLayout_165.setObjectName(u"gridLayout_165")
        self.gridLayout_165.setHorizontalSpacing(0)
        self.gridLayout_165.setVerticalSpacing(16)
        self.produk_40 = QLabel(self.frame_99)
        self.produk_40.setObjectName(u"produk_40")
        self.produk_40.setMaximumSize(QSize(16777215, 60))
        self.produk_40.setFont(font8)
        self.produk_40.setScaledContents(True)
        self.produk_40.setWordWrap(True)

        self.gridLayout_165.addWidget(self.produk_40, 0, 0, 1, 4)

        self.diskon_40 = QPushButton(self.frame_99)
        self.diskon_40.setObjectName(u"diskon_40")
        self.diskon_40.setFont(font9)
        self.diskon_40.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_40.setIcon(icon10)
        self.diskon_40.setIconSize(QSize(20, 20))

        self.gridLayout_165.addWidget(self.diskon_40, 1, 2, 1, 1)

        self.harga_40 = QLabel(self.frame_99)
        self.harga_40.setObjectName(u"harga_40")
        self.harga_40.setMaximumSize(QSize(16777215, 30))
        self.harga_40.setFont(font10)
        self.harga_40.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_165.addWidget(self.harga_40, 1, 0, 1, 1)

        self.tombol_40 = QPushButton(self.frame_99)
        self.tombol_40.setObjectName(u"tombol_40")
        self.tombol_40.setMinimumSize(QSize(0, 40))
        self.tombol_40.setFont(font4)
        self.tombol_40.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_40.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_165.addWidget(self.tombol_40, 2, 0, 1, 4)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_165.addItem(self.horizontalSpacer_41, 1, 1, 1, 1)


        self.gridLayout_164.addWidget(self.frame_99, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_16, 7, 1, 1, 1)

        self.recomended = QFrame(self.frame_3)
        self.recomended.setObjectName(u"recomended")
        self.recomended.setMaximumSize(QSize(16777215, 192))
        self.recomended.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_82 = QGridLayout(self.recomended)
        self.gridLayout_82.setSpacing(0)
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.gridLayout_82.setContentsMargins(0, 0, 0, 0)
        self.image_produc = QFrame(self.recomended)
        self.image_produc.setObjectName(u"image_produc")
        self.image_produc.setMinimumSize(QSize(190, 190))
        self.image_produc.setMaximumSize(QSize(190, 190))
        self.image_produc.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_82.addWidget(self.image_produc, 0, 0, 1, 1)

        self.frame_60 = QFrame(self.recomended)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(188, 0))
        self.frame_60.setStyleSheet(u"border-width: 0px;")
        self.frame_60.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_83 = QGridLayout(self.frame_60)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.gridLayout_83.setHorizontalSpacing(0)
        self.gridLayout_83.setVerticalSpacing(16)
        self.produk = QLabel(self.frame_60)
        self.produk.setObjectName(u"produk")
        self.produk.setMaximumSize(QSize(16777215, 60))
        self.produk.setFont(font8)
        self.produk.setScaledContents(True)
        self.produk.setWordWrap(True)

        self.gridLayout_83.addWidget(self.produk, 0, 0, 1, 4)

        self.diskon = QPushButton(self.frame_60)
        self.diskon.setObjectName(u"diskon")
        self.diskon.setFont(font9)
        self.diskon.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon.setIcon(icon10)
        self.diskon.setIconSize(QSize(20, 20))

        self.gridLayout_83.addWidget(self.diskon, 1, 2, 1, 1)

        self.harga = QLabel(self.frame_60)
        self.harga.setObjectName(u"harga")
        self.harga.setMaximumSize(QSize(16777215, 30))
        self.harga.setFont(font10)
        self.harga.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_83.addWidget(self.harga, 1, 0, 1, 1)

        self.tombol = QPushButton(self.frame_60)
        self.tombol.setObjectName(u"tombol")
        self.tombol.setMinimumSize(QSize(0, 40))
        self.tombol.setFont(font4)
        self.tombol.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_83.addWidget(self.tombol, 2, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_83.addItem(self.horizontalSpacer, 1, 1, 1, 1)


        self.gridLayout_82.addWidget(self.frame_60, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended, 0, 0, 1, 1)

        self.recomended_9 = QFrame(self.frame_3)
        self.recomended_9.setObjectName(u"recomended_9")
        self.recomended_9.setMaximumSize(QSize(16777215, 192))
        self.recomended_9.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_150 = QGridLayout(self.recomended_9)
        self.gridLayout_150.setSpacing(0)
        self.gridLayout_150.setObjectName(u"gridLayout_150")
        self.gridLayout_150.setContentsMargins(0, 0, 0, 0)
        self.image_produc_33 = QFrame(self.recomended_9)
        self.image_produc_33.setObjectName(u"image_produc_33")
        self.image_produc_33.setMinimumSize(QSize(190, 190))
        self.image_produc_33.setMaximumSize(QSize(190, 190))
        self.image_produc_33.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_33.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_150.addWidget(self.image_produc_33, 0, 0, 1, 1)

        self.frame_92 = QFrame(self.recomended_9)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(188, 0))
        self.frame_92.setStyleSheet(u"border-width: 0px;")
        self.frame_92.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_151 = QGridLayout(self.frame_92)
        self.gridLayout_151.setObjectName(u"gridLayout_151")
        self.gridLayout_151.setHorizontalSpacing(0)
        self.gridLayout_151.setVerticalSpacing(16)
        self.produk_33 = QLabel(self.frame_92)
        self.produk_33.setObjectName(u"produk_33")
        self.produk_33.setMaximumSize(QSize(16777215, 60))
        self.produk_33.setFont(font8)
        self.produk_33.setScaledContents(True)
        self.produk_33.setWordWrap(True)

        self.gridLayout_151.addWidget(self.produk_33, 0, 0, 1, 4)

        self.diskon_33 = QPushButton(self.frame_92)
        self.diskon_33.setObjectName(u"diskon_33")
        self.diskon_33.setFont(font9)
        self.diskon_33.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_33.setIcon(icon10)
        self.diskon_33.setIconSize(QSize(20, 20))

        self.gridLayout_151.addWidget(self.diskon_33, 1, 2, 1, 1)

        self.harga_33 = QLabel(self.frame_92)
        self.harga_33.setObjectName(u"harga_33")
        self.harga_33.setMaximumSize(QSize(16777215, 30))
        self.harga_33.setFont(font10)
        self.harga_33.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_151.addWidget(self.harga_33, 1, 0, 1, 1)

        self.tombol_33 = QPushButton(self.frame_92)
        self.tombol_33.setObjectName(u"tombol_33")
        self.tombol_33.setMinimumSize(QSize(0, 40))
        self.tombol_33.setFont(font4)
        self.tombol_33.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_33.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_151.addWidget(self.tombol_33, 2, 0, 1, 4)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_151.addItem(self.horizontalSpacer_34, 1, 1, 1, 1)


        self.gridLayout_150.addWidget(self.frame_92, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_9, 4, 0, 1, 1)

        self.recomended_14 = QFrame(self.frame_3)
        self.recomended_14.setObjectName(u"recomended_14")
        self.recomended_14.setMaximumSize(QSize(16777215, 192))
        self.recomended_14.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_14.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_160 = QGridLayout(self.recomended_14)
        self.gridLayout_160.setSpacing(0)
        self.gridLayout_160.setObjectName(u"gridLayout_160")
        self.gridLayout_160.setContentsMargins(0, 0, 0, 0)
        self.image_produc_38 = QFrame(self.recomended_14)
        self.image_produc_38.setObjectName(u"image_produc_38")
        self.image_produc_38.setMinimumSize(QSize(190, 190))
        self.image_produc_38.setMaximumSize(QSize(190, 190))
        self.image_produc_38.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_38.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_160.addWidget(self.image_produc_38, 0, 0, 1, 1)

        self.frame_97 = QFrame(self.recomended_14)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMinimumSize(QSize(188, 0))
        self.frame_97.setStyleSheet(u"border-width: 0px;")
        self.frame_97.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_161 = QGridLayout(self.frame_97)
        self.gridLayout_161.setObjectName(u"gridLayout_161")
        self.gridLayout_161.setHorizontalSpacing(0)
        self.gridLayout_161.setVerticalSpacing(16)
        self.produk_38 = QLabel(self.frame_97)
        self.produk_38.setObjectName(u"produk_38")
        self.produk_38.setMaximumSize(QSize(16777215, 60))
        self.produk_38.setFont(font8)
        self.produk_38.setScaledContents(True)
        self.produk_38.setWordWrap(True)

        self.gridLayout_161.addWidget(self.produk_38, 0, 0, 1, 4)

        self.diskon_38 = QPushButton(self.frame_97)
        self.diskon_38.setObjectName(u"diskon_38")
        self.diskon_38.setFont(font9)
        self.diskon_38.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_38.setIcon(icon10)
        self.diskon_38.setIconSize(QSize(20, 20))

        self.gridLayout_161.addWidget(self.diskon_38, 1, 2, 1, 1)

        self.harga_38 = QLabel(self.frame_97)
        self.harga_38.setObjectName(u"harga_38")
        self.harga_38.setMaximumSize(QSize(16777215, 30))
        self.harga_38.setFont(font10)
        self.harga_38.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_161.addWidget(self.harga_38, 1, 0, 1, 1)

        self.tombol_38 = QPushButton(self.frame_97)
        self.tombol_38.setObjectName(u"tombol_38")
        self.tombol_38.setMinimumSize(QSize(0, 40))
        self.tombol_38.setFont(font4)
        self.tombol_38.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_38.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_161.addWidget(self.tombol_38, 2, 0, 1, 4)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_161.addItem(self.horizontalSpacer_39, 1, 1, 1, 1)


        self.gridLayout_160.addWidget(self.frame_97, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_14, 6, 1, 1, 1)

        self.recomended_12 = QFrame(self.frame_3)
        self.recomended_12.setObjectName(u"recomended_12")
        self.recomended_12.setMaximumSize(QSize(16777215, 192))
        self.recomended_12.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_12.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_156 = QGridLayout(self.recomended_12)
        self.gridLayout_156.setSpacing(0)
        self.gridLayout_156.setObjectName(u"gridLayout_156")
        self.gridLayout_156.setContentsMargins(0, 0, 0, 0)
        self.image_produc_36 = QFrame(self.recomended_12)
        self.image_produc_36.setObjectName(u"image_produc_36")
        self.image_produc_36.setMinimumSize(QSize(190, 190))
        self.image_produc_36.setMaximumSize(QSize(190, 190))
        self.image_produc_36.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_36.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_156.addWidget(self.image_produc_36, 0, 0, 1, 1)

        self.frame_95 = QFrame(self.recomended_12)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(188, 0))
        self.frame_95.setStyleSheet(u"border-width: 0px;")
        self.frame_95.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_157 = QGridLayout(self.frame_95)
        self.gridLayout_157.setObjectName(u"gridLayout_157")
        self.gridLayout_157.setHorizontalSpacing(0)
        self.gridLayout_157.setVerticalSpacing(16)
        self.produk_36 = QLabel(self.frame_95)
        self.produk_36.setObjectName(u"produk_36")
        self.produk_36.setMaximumSize(QSize(16777215, 60))
        self.produk_36.setFont(font8)
        self.produk_36.setScaledContents(True)
        self.produk_36.setWordWrap(True)

        self.gridLayout_157.addWidget(self.produk_36, 0, 0, 1, 4)

        self.diskon_36 = QPushButton(self.frame_95)
        self.diskon_36.setObjectName(u"diskon_36")
        self.diskon_36.setFont(font9)
        self.diskon_36.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_36.setIcon(icon10)
        self.diskon_36.setIconSize(QSize(20, 20))

        self.gridLayout_157.addWidget(self.diskon_36, 1, 2, 1, 1)

        self.harga_36 = QLabel(self.frame_95)
        self.harga_36.setObjectName(u"harga_36")
        self.harga_36.setMaximumSize(QSize(16777215, 30))
        self.harga_36.setFont(font10)
        self.harga_36.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_157.addWidget(self.harga_36, 1, 0, 1, 1)

        self.tombol_36 = QPushButton(self.frame_95)
        self.tombol_36.setObjectName(u"tombol_36")
        self.tombol_36.setMinimumSize(QSize(0, 40))
        self.tombol_36.setFont(font4)
        self.tombol_36.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_36.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_157.addWidget(self.tombol_36, 2, 0, 1, 4)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_157.addItem(self.horizontalSpacer_37, 1, 1, 1, 1)


        self.gridLayout_156.addWidget(self.frame_95, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_12, 5, 1, 1, 1)

        self.recomended_8 = QFrame(self.frame_3)
        self.recomended_8.setObjectName(u"recomended_8")
        self.recomended_8.setMaximumSize(QSize(16777215, 192))
        self.recomended_8.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_148 = QGridLayout(self.recomended_8)
        self.gridLayout_148.setSpacing(0)
        self.gridLayout_148.setObjectName(u"gridLayout_148")
        self.gridLayout_148.setContentsMargins(0, 0, 0, 0)
        self.image_produc_32 = QFrame(self.recomended_8)
        self.image_produc_32.setObjectName(u"image_produc_32")
        self.image_produc_32.setMinimumSize(QSize(190, 190))
        self.image_produc_32.setMaximumSize(QSize(190, 190))
        self.image_produc_32.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_32.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_148.addWidget(self.image_produc_32, 0, 0, 1, 1)

        self.frame_91 = QFrame(self.recomended_8)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(188, 0))
        self.frame_91.setStyleSheet(u"border-width: 0px;")
        self.frame_91.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_149 = QGridLayout(self.frame_91)
        self.gridLayout_149.setObjectName(u"gridLayout_149")
        self.gridLayout_149.setHorizontalSpacing(0)
        self.gridLayout_149.setVerticalSpacing(16)
        self.produk_32 = QLabel(self.frame_91)
        self.produk_32.setObjectName(u"produk_32")
        self.produk_32.setMaximumSize(QSize(16777215, 60))
        self.produk_32.setFont(font8)
        self.produk_32.setScaledContents(True)
        self.produk_32.setWordWrap(True)

        self.gridLayout_149.addWidget(self.produk_32, 0, 0, 1, 4)

        self.diskon_32 = QPushButton(self.frame_91)
        self.diskon_32.setObjectName(u"diskon_32")
        self.diskon_32.setFont(font9)
        self.diskon_32.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_32.setIcon(icon10)
        self.diskon_32.setIconSize(QSize(20, 20))

        self.gridLayout_149.addWidget(self.diskon_32, 1, 2, 1, 1)

        self.harga_32 = QLabel(self.frame_91)
        self.harga_32.setObjectName(u"harga_32")
        self.harga_32.setMaximumSize(QSize(16777215, 30))
        self.harga_32.setFont(font10)
        self.harga_32.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_149.addWidget(self.harga_32, 1, 0, 1, 1)

        self.tombol_32 = QPushButton(self.frame_91)
        self.tombol_32.setObjectName(u"tombol_32")
        self.tombol_32.setMinimumSize(QSize(0, 40))
        self.tombol_32.setFont(font4)
        self.tombol_32.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_32.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_149.addWidget(self.tombol_32, 2, 0, 1, 4)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_149.addItem(self.horizontalSpacer_33, 1, 1, 1, 1)


        self.gridLayout_148.addWidget(self.frame_91, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_8, 3, 1, 1, 1)

        self.recomended_11 = QFrame(self.frame_3)
        self.recomended_11.setObjectName(u"recomended_11")
        self.recomended_11.setMaximumSize(QSize(16777215, 192))
        self.recomended_11.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_11.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_154 = QGridLayout(self.recomended_11)
        self.gridLayout_154.setSpacing(0)
        self.gridLayout_154.setObjectName(u"gridLayout_154")
        self.gridLayout_154.setContentsMargins(0, 0, 0, 0)
        self.image_produc_35 = QFrame(self.recomended_11)
        self.image_produc_35.setObjectName(u"image_produc_35")
        self.image_produc_35.setMinimumSize(QSize(190, 190))
        self.image_produc_35.setMaximumSize(QSize(190, 190))
        self.image_produc_35.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_35.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_154.addWidget(self.image_produc_35, 0, 0, 1, 1)

        self.frame_94 = QFrame(self.recomended_11)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(188, 0))
        self.frame_94.setStyleSheet(u"border-width: 0px;")
        self.frame_94.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_155 = QGridLayout(self.frame_94)
        self.gridLayout_155.setObjectName(u"gridLayout_155")
        self.gridLayout_155.setHorizontalSpacing(0)
        self.gridLayout_155.setVerticalSpacing(16)
        self.produk_35 = QLabel(self.frame_94)
        self.produk_35.setObjectName(u"produk_35")
        self.produk_35.setMaximumSize(QSize(16777215, 60))
        self.produk_35.setFont(font8)
        self.produk_35.setScaledContents(True)
        self.produk_35.setWordWrap(True)

        self.gridLayout_155.addWidget(self.produk_35, 0, 0, 1, 4)

        self.diskon_35 = QPushButton(self.frame_94)
        self.diskon_35.setObjectName(u"diskon_35")
        self.diskon_35.setFont(font9)
        self.diskon_35.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_35.setIcon(icon10)
        self.diskon_35.setIconSize(QSize(20, 20))

        self.gridLayout_155.addWidget(self.diskon_35, 1, 2, 1, 1)

        self.harga_35 = QLabel(self.frame_94)
        self.harga_35.setObjectName(u"harga_35")
        self.harga_35.setMaximumSize(QSize(16777215, 30))
        self.harga_35.setFont(font10)
        self.harga_35.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_155.addWidget(self.harga_35, 1, 0, 1, 1)

        self.tombol_35 = QPushButton(self.frame_94)
        self.tombol_35.setObjectName(u"tombol_35")
        self.tombol_35.setMinimumSize(QSize(0, 40))
        self.tombol_35.setFont(font4)
        self.tombol_35.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_35.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_155.addWidget(self.tombol_35, 2, 0, 1, 4)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_155.addItem(self.horizontalSpacer_36, 1, 1, 1, 1)


        self.gridLayout_154.addWidget(self.frame_94, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_11, 5, 0, 1, 1)

        self.recomended_13 = QFrame(self.frame_3)
        self.recomended_13.setObjectName(u"recomended_13")
        self.recomended_13.setMaximumSize(QSize(16777215, 192))
        self.recomended_13.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_13.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_158 = QGridLayout(self.recomended_13)
        self.gridLayout_158.setSpacing(0)
        self.gridLayout_158.setObjectName(u"gridLayout_158")
        self.gridLayout_158.setContentsMargins(0, 0, 0, 0)
        self.image_produc_37 = QFrame(self.recomended_13)
        self.image_produc_37.setObjectName(u"image_produc_37")
        self.image_produc_37.setMinimumSize(QSize(190, 190))
        self.image_produc_37.setMaximumSize(QSize(190, 190))
        self.image_produc_37.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_37.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_158.addWidget(self.image_produc_37, 0, 0, 1, 1)

        self.frame_96 = QFrame(self.recomended_13)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(188, 0))
        self.frame_96.setStyleSheet(u"border-width: 0px;")
        self.frame_96.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_159 = QGridLayout(self.frame_96)
        self.gridLayout_159.setObjectName(u"gridLayout_159")
        self.gridLayout_159.setHorizontalSpacing(0)
        self.gridLayout_159.setVerticalSpacing(16)
        self.produk_37 = QLabel(self.frame_96)
        self.produk_37.setObjectName(u"produk_37")
        self.produk_37.setMaximumSize(QSize(16777215, 60))
        self.produk_37.setFont(font8)
        self.produk_37.setScaledContents(True)
        self.produk_37.setWordWrap(True)

        self.gridLayout_159.addWidget(self.produk_37, 0, 0, 1, 4)

        self.diskon_37 = QPushButton(self.frame_96)
        self.diskon_37.setObjectName(u"diskon_37")
        self.diskon_37.setFont(font9)
        self.diskon_37.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_37.setIcon(icon10)
        self.diskon_37.setIconSize(QSize(20, 20))

        self.gridLayout_159.addWidget(self.diskon_37, 1, 2, 1, 1)

        self.harga_37 = QLabel(self.frame_96)
        self.harga_37.setObjectName(u"harga_37")
        self.harga_37.setMaximumSize(QSize(16777215, 30))
        self.harga_37.setFont(font10)
        self.harga_37.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_159.addWidget(self.harga_37, 1, 0, 1, 1)

        self.tombol_37 = QPushButton(self.frame_96)
        self.tombol_37.setObjectName(u"tombol_37")
        self.tombol_37.setMinimumSize(QSize(0, 40))
        self.tombol_37.setFont(font4)
        self.tombol_37.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_37.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_159.addWidget(self.tombol_37, 2, 0, 1, 4)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_159.addItem(self.horizontalSpacer_38, 1, 1, 1, 1)


        self.gridLayout_158.addWidget(self.frame_96, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_13, 6, 0, 1, 1)

        self.recomended_5 = QFrame(self.frame_3)
        self.recomended_5.setObjectName(u"recomended_5")
        self.recomended_5.setMaximumSize(QSize(16777215, 192))
        self.recomended_5.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_142 = QGridLayout(self.recomended_5)
        self.gridLayout_142.setSpacing(0)
        self.gridLayout_142.setObjectName(u"gridLayout_142")
        self.gridLayout_142.setContentsMargins(0, 0, 0, 0)
        self.image_produc_29 = QFrame(self.recomended_5)
        self.image_produc_29.setObjectName(u"image_produc_29")
        self.image_produc_29.setMinimumSize(QSize(190, 190))
        self.image_produc_29.setMaximumSize(QSize(190, 190))
        self.image_produc_29.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_29.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_142.addWidget(self.image_produc_29, 0, 0, 1, 1)

        self.frame_88 = QFrame(self.recomended_5)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(188, 0))
        self.frame_88.setStyleSheet(u"border-width: 0px;")
        self.frame_88.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_143 = QGridLayout(self.frame_88)
        self.gridLayout_143.setObjectName(u"gridLayout_143")
        self.gridLayout_143.setHorizontalSpacing(0)
        self.gridLayout_143.setVerticalSpacing(16)
        self.produk_29 = QLabel(self.frame_88)
        self.produk_29.setObjectName(u"produk_29")
        self.produk_29.setMaximumSize(QSize(16777215, 60))
        self.produk_29.setFont(font8)
        self.produk_29.setScaledContents(True)
        self.produk_29.setWordWrap(True)

        self.gridLayout_143.addWidget(self.produk_29, 0, 0, 1, 4)

        self.diskon_29 = QPushButton(self.frame_88)
        self.diskon_29.setObjectName(u"diskon_29")
        self.diskon_29.setFont(font9)
        self.diskon_29.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_29.setIcon(icon10)
        self.diskon_29.setIconSize(QSize(20, 20))

        self.gridLayout_143.addWidget(self.diskon_29, 1, 2, 1, 1)

        self.harga_29 = QLabel(self.frame_88)
        self.harga_29.setObjectName(u"harga_29")
        self.harga_29.setMaximumSize(QSize(16777215, 30))
        self.harga_29.setFont(font10)
        self.harga_29.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_143.addWidget(self.harga_29, 1, 0, 1, 1)

        self.tombol_29 = QPushButton(self.frame_88)
        self.tombol_29.setObjectName(u"tombol_29")
        self.tombol_29.setMinimumSize(QSize(0, 40))
        self.tombol_29.setFont(font4)
        self.tombol_29.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_29.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_143.addWidget(self.tombol_29, 2, 0, 1, 4)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_143.addItem(self.horizontalSpacer_30, 1, 1, 1, 1)


        self.gridLayout_142.addWidget(self.frame_88, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_5, 2, 0, 1, 1)

        self.recomended_6 = QFrame(self.frame_3)
        self.recomended_6.setObjectName(u"recomended_6")
        self.recomended_6.setMaximumSize(QSize(16777215, 192))
        self.recomended_6.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_144 = QGridLayout(self.recomended_6)
        self.gridLayout_144.setSpacing(0)
        self.gridLayout_144.setObjectName(u"gridLayout_144")
        self.gridLayout_144.setContentsMargins(0, 0, 0, 0)
        self.image_produc_30 = QFrame(self.recomended_6)
        self.image_produc_30.setObjectName(u"image_produc_30")
        self.image_produc_30.setMinimumSize(QSize(190, 190))
        self.image_produc_30.setMaximumSize(QSize(190, 190))
        self.image_produc_30.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_30.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_144.addWidget(self.image_produc_30, 0, 0, 1, 1)

        self.frame_89 = QFrame(self.recomended_6)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(188, 0))
        self.frame_89.setStyleSheet(u"border-width: 0px;")
        self.frame_89.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_145 = QGridLayout(self.frame_89)
        self.gridLayout_145.setObjectName(u"gridLayout_145")
        self.gridLayout_145.setHorizontalSpacing(0)
        self.gridLayout_145.setVerticalSpacing(16)
        self.produk_30 = QLabel(self.frame_89)
        self.produk_30.setObjectName(u"produk_30")
        self.produk_30.setMaximumSize(QSize(16777215, 60))
        self.produk_30.setFont(font8)
        self.produk_30.setScaledContents(True)
        self.produk_30.setWordWrap(True)

        self.gridLayout_145.addWidget(self.produk_30, 0, 0, 1, 4)

        self.diskon_30 = QPushButton(self.frame_89)
        self.diskon_30.setObjectName(u"diskon_30")
        self.diskon_30.setFont(font9)
        self.diskon_30.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_30.setIcon(icon10)
        self.diskon_30.setIconSize(QSize(20, 20))

        self.gridLayout_145.addWidget(self.diskon_30, 1, 2, 1, 1)

        self.harga_30 = QLabel(self.frame_89)
        self.harga_30.setObjectName(u"harga_30")
        self.harga_30.setMaximumSize(QSize(16777215, 30))
        self.harga_30.setFont(font10)
        self.harga_30.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_145.addWidget(self.harga_30, 1, 0, 1, 1)

        self.tombol_30 = QPushButton(self.frame_89)
        self.tombol_30.setObjectName(u"tombol_30")
        self.tombol_30.setMinimumSize(QSize(0, 40))
        self.tombol_30.setFont(font4)
        self.tombol_30.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_30.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_145.addWidget(self.tombol_30, 2, 0, 1, 4)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_145.addItem(self.horizontalSpacer_31, 1, 1, 1, 1)


        self.gridLayout_144.addWidget(self.frame_89, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_6, 2, 1, 1, 1)

        self.recomended_10 = QFrame(self.frame_3)
        self.recomended_10.setObjectName(u"recomended_10")
        self.recomended_10.setMaximumSize(QSize(16777215, 192))
        self.recomended_10.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_152 = QGridLayout(self.recomended_10)
        self.gridLayout_152.setSpacing(0)
        self.gridLayout_152.setObjectName(u"gridLayout_152")
        self.gridLayout_152.setContentsMargins(0, 0, 0, 0)
        self.image_produc_34 = QFrame(self.recomended_10)
        self.image_produc_34.setObjectName(u"image_produc_34")
        self.image_produc_34.setMinimumSize(QSize(190, 190))
        self.image_produc_34.setMaximumSize(QSize(190, 190))
        self.image_produc_34.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_34.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_152.addWidget(self.image_produc_34, 0, 0, 1, 1)

        self.frame_93 = QFrame(self.recomended_10)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(188, 0))
        self.frame_93.setStyleSheet(u"border-width: 0px;")
        self.frame_93.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_153 = QGridLayout(self.frame_93)
        self.gridLayout_153.setObjectName(u"gridLayout_153")
        self.gridLayout_153.setHorizontalSpacing(0)
        self.gridLayout_153.setVerticalSpacing(16)
        self.produk_34 = QLabel(self.frame_93)
        self.produk_34.setObjectName(u"produk_34")
        self.produk_34.setMaximumSize(QSize(16777215, 60))
        self.produk_34.setFont(font8)
        self.produk_34.setScaledContents(True)
        self.produk_34.setWordWrap(True)

        self.gridLayout_153.addWidget(self.produk_34, 0, 0, 1, 4)

        self.diskon_34 = QPushButton(self.frame_93)
        self.diskon_34.setObjectName(u"diskon_34")
        self.diskon_34.setFont(font9)
        self.diskon_34.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_34.setIcon(icon10)
        self.diskon_34.setIconSize(QSize(20, 20))

        self.gridLayout_153.addWidget(self.diskon_34, 1, 2, 1, 1)

        self.harga_34 = QLabel(self.frame_93)
        self.harga_34.setObjectName(u"harga_34")
        self.harga_34.setMaximumSize(QSize(16777215, 30))
        self.harga_34.setFont(font10)
        self.harga_34.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_153.addWidget(self.harga_34, 1, 0, 1, 1)

        self.tombol_34 = QPushButton(self.frame_93)
        self.tombol_34.setObjectName(u"tombol_34")
        self.tombol_34.setMinimumSize(QSize(0, 40))
        self.tombol_34.setFont(font4)
        self.tombol_34.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_34.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_153.addWidget(self.tombol_34, 2, 0, 1, 4)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_153.addItem(self.horizontalSpacer_35, 1, 1, 1, 1)


        self.gridLayout_152.addWidget(self.frame_93, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_10, 4, 1, 1, 1)

        self.recomended_4 = QFrame(self.frame_3)
        self.recomended_4.setObjectName(u"recomended_4")
        self.recomended_4.setMaximumSize(QSize(16777215, 192))
        self.recomended_4.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_140 = QGridLayout(self.recomended_4)
        self.gridLayout_140.setSpacing(0)
        self.gridLayout_140.setObjectName(u"gridLayout_140")
        self.gridLayout_140.setContentsMargins(0, 0, 0, 0)
        self.image_produc_28 = QFrame(self.recomended_4)
        self.image_produc_28.setObjectName(u"image_produc_28")
        self.image_produc_28.setMinimumSize(QSize(190, 190))
        self.image_produc_28.setMaximumSize(QSize(190, 190))
        self.image_produc_28.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_28.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_140.addWidget(self.image_produc_28, 0, 0, 1, 1)

        self.frame_87 = QFrame(self.recomended_4)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(188, 0))
        self.frame_87.setStyleSheet(u"border-width: 0px;")
        self.frame_87.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_141 = QGridLayout(self.frame_87)
        self.gridLayout_141.setObjectName(u"gridLayout_141")
        self.gridLayout_141.setHorizontalSpacing(0)
        self.gridLayout_141.setVerticalSpacing(16)
        self.produk_28 = QLabel(self.frame_87)
        self.produk_28.setObjectName(u"produk_28")
        self.produk_28.setMaximumSize(QSize(16777215, 60))
        self.produk_28.setFont(font8)
        self.produk_28.setScaledContents(True)
        self.produk_28.setWordWrap(True)

        self.gridLayout_141.addWidget(self.produk_28, 0, 0, 1, 4)

        self.diskon_28 = QPushButton(self.frame_87)
        self.diskon_28.setObjectName(u"diskon_28")
        self.diskon_28.setFont(font9)
        self.diskon_28.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_28.setIcon(icon10)
        self.diskon_28.setIconSize(QSize(20, 20))

        self.gridLayout_141.addWidget(self.diskon_28, 1, 2, 1, 1)

        self.harga_28 = QLabel(self.frame_87)
        self.harga_28.setObjectName(u"harga_28")
        self.harga_28.setMaximumSize(QSize(16777215, 30))
        self.harga_28.setFont(font10)
        self.harga_28.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_141.addWidget(self.harga_28, 1, 0, 1, 1)

        self.tombol_28 = QPushButton(self.frame_87)
        self.tombol_28.setObjectName(u"tombol_28")
        self.tombol_28.setMinimumSize(QSize(0, 40))
        self.tombol_28.setFont(font4)
        self.tombol_28.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_28.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_141.addWidget(self.tombol_28, 2, 0, 1, 4)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_141.addItem(self.horizontalSpacer_29, 1, 1, 1, 1)


        self.gridLayout_140.addWidget(self.frame_87, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_4, 1, 1, 1, 1)

        self.recomended_17 = QFrame(self.frame_3)
        self.recomended_17.setObjectName(u"recomended_17")
        self.recomended_17.setMaximumSize(QSize(16777215, 192))
        self.recomended_17.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_17.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_166 = QGridLayout(self.recomended_17)
        self.gridLayout_166.setSpacing(0)
        self.gridLayout_166.setObjectName(u"gridLayout_166")
        self.gridLayout_166.setContentsMargins(0, 0, 0, 0)
        self.image_produc_41 = QFrame(self.recomended_17)
        self.image_produc_41.setObjectName(u"image_produc_41")
        self.image_produc_41.setMinimumSize(QSize(190, 190))
        self.image_produc_41.setMaximumSize(QSize(190, 190))
        self.image_produc_41.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_41.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_166.addWidget(self.image_produc_41, 0, 0, 1, 1)

        self.frame_100 = QFrame(self.recomended_17)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(188, 0))
        self.frame_100.setStyleSheet(u"border-width: 0px;")
        self.frame_100.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_167 = QGridLayout(self.frame_100)
        self.gridLayout_167.setObjectName(u"gridLayout_167")
        self.gridLayout_167.setHorizontalSpacing(0)
        self.gridLayout_167.setVerticalSpacing(16)
        self.produk_41 = QLabel(self.frame_100)
        self.produk_41.setObjectName(u"produk_41")
        self.produk_41.setMaximumSize(QSize(16777215, 60))
        self.produk_41.setFont(font8)
        self.produk_41.setScaledContents(True)
        self.produk_41.setWordWrap(True)

        self.gridLayout_167.addWidget(self.produk_41, 0, 0, 1, 4)

        self.diskon_41 = QPushButton(self.frame_100)
        self.diskon_41.setObjectName(u"diskon_41")
        self.diskon_41.setFont(font9)
        self.diskon_41.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_41.setIcon(icon10)
        self.diskon_41.setIconSize(QSize(20, 20))

        self.gridLayout_167.addWidget(self.diskon_41, 1, 2, 1, 1)

        self.harga_41 = QLabel(self.frame_100)
        self.harga_41.setObjectName(u"harga_41")
        self.harga_41.setMaximumSize(QSize(16777215, 30))
        self.harga_41.setFont(font10)
        self.harga_41.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_167.addWidget(self.harga_41, 1, 0, 1, 1)

        self.tombol_41 = QPushButton(self.frame_100)
        self.tombol_41.setObjectName(u"tombol_41")
        self.tombol_41.setMinimumSize(QSize(0, 40))
        self.tombol_41.setFont(font4)
        self.tombol_41.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_41.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_167.addWidget(self.tombol_41, 2, 0, 1, 4)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_167.addItem(self.horizontalSpacer_42, 1, 1, 1, 1)


        self.gridLayout_166.addWidget(self.frame_100, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_17, 8, 0, 1, 1)

        self.recomended_15 = QFrame(self.frame_3)
        self.recomended_15.setObjectName(u"recomended_15")
        self.recomended_15.setMaximumSize(QSize(16777215, 192))
        self.recomended_15.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_15.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_162 = QGridLayout(self.recomended_15)
        self.gridLayout_162.setSpacing(0)
        self.gridLayout_162.setObjectName(u"gridLayout_162")
        self.gridLayout_162.setContentsMargins(0, 0, 0, 0)
        self.image_produc_39 = QFrame(self.recomended_15)
        self.image_produc_39.setObjectName(u"image_produc_39")
        self.image_produc_39.setMinimumSize(QSize(190, 190))
        self.image_produc_39.setMaximumSize(QSize(190, 190))
        self.image_produc_39.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_39.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_162.addWidget(self.image_produc_39, 0, 0, 1, 1)

        self.frame_98 = QFrame(self.recomended_15)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(188, 0))
        self.frame_98.setStyleSheet(u"border-width: 0px;")
        self.frame_98.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_163 = QGridLayout(self.frame_98)
        self.gridLayout_163.setObjectName(u"gridLayout_163")
        self.gridLayout_163.setHorizontalSpacing(0)
        self.gridLayout_163.setVerticalSpacing(16)
        self.produk_39 = QLabel(self.frame_98)
        self.produk_39.setObjectName(u"produk_39")
        self.produk_39.setMaximumSize(QSize(16777215, 60))
        self.produk_39.setFont(font8)
        self.produk_39.setScaledContents(True)
        self.produk_39.setWordWrap(True)

        self.gridLayout_163.addWidget(self.produk_39, 0, 0, 1, 4)

        self.diskon_39 = QPushButton(self.frame_98)
        self.diskon_39.setObjectName(u"diskon_39")
        self.diskon_39.setFont(font9)
        self.diskon_39.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_39.setIcon(icon10)
        self.diskon_39.setIconSize(QSize(20, 20))

        self.gridLayout_163.addWidget(self.diskon_39, 1, 2, 1, 1)

        self.harga_39 = QLabel(self.frame_98)
        self.harga_39.setObjectName(u"harga_39")
        self.harga_39.setMaximumSize(QSize(16777215, 30))
        self.harga_39.setFont(font10)
        self.harga_39.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_163.addWidget(self.harga_39, 1, 0, 1, 1)

        self.tombol_39 = QPushButton(self.frame_98)
        self.tombol_39.setObjectName(u"tombol_39")
        self.tombol_39.setMinimumSize(QSize(0, 40))
        self.tombol_39.setFont(font4)
        self.tombol_39.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_39.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_163.addWidget(self.tombol_39, 2, 0, 1, 4)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_163.addItem(self.horizontalSpacer_40, 1, 1, 1, 1)


        self.gridLayout_162.addWidget(self.frame_98, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_15, 7, 0, 1, 1)

        self.recomended_19 = QFrame(self.frame_3)
        self.recomended_19.setObjectName(u"recomended_19")
        self.recomended_19.setMaximumSize(QSize(16777215, 192))
        self.recomended_19.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_19.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_170 = QGridLayout(self.recomended_19)
        self.gridLayout_170.setSpacing(0)
        self.gridLayout_170.setObjectName(u"gridLayout_170")
        self.gridLayout_170.setContentsMargins(0, 0, 0, 0)
        self.image_produc_43 = QFrame(self.recomended_19)
        self.image_produc_43.setObjectName(u"image_produc_43")
        self.image_produc_43.setMinimumSize(QSize(190, 190))
        self.image_produc_43.setMaximumSize(QSize(190, 190))
        self.image_produc_43.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_43.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_43.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_170.addWidget(self.image_produc_43, 0, 0, 1, 1)

        self.frame_102 = QFrame(self.recomended_19)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setMinimumSize(QSize(188, 0))
        self.frame_102.setStyleSheet(u"border-width: 0px;")
        self.frame_102.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_171 = QGridLayout(self.frame_102)
        self.gridLayout_171.setObjectName(u"gridLayout_171")
        self.gridLayout_171.setHorizontalSpacing(0)
        self.gridLayout_171.setVerticalSpacing(16)
        self.produk_43 = QLabel(self.frame_102)
        self.produk_43.setObjectName(u"produk_43")
        self.produk_43.setMaximumSize(QSize(16777215, 60))
        self.produk_43.setFont(font8)
        self.produk_43.setScaledContents(True)
        self.produk_43.setWordWrap(True)

        self.gridLayout_171.addWidget(self.produk_43, 0, 0, 1, 4)

        self.diskon_43 = QPushButton(self.frame_102)
        self.diskon_43.setObjectName(u"diskon_43")
        self.diskon_43.setFont(font9)
        self.diskon_43.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_43.setIcon(icon10)
        self.diskon_43.setIconSize(QSize(20, 20))

        self.gridLayout_171.addWidget(self.diskon_43, 1, 2, 1, 1)

        self.harga_43 = QLabel(self.frame_102)
        self.harga_43.setObjectName(u"harga_43")
        self.harga_43.setMaximumSize(QSize(16777215, 30))
        self.harga_43.setFont(font10)
        self.harga_43.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_171.addWidget(self.harga_43, 1, 0, 1, 1)

        self.tombol_43 = QPushButton(self.frame_102)
        self.tombol_43.setObjectName(u"tombol_43")
        self.tombol_43.setMinimumSize(QSize(0, 40))
        self.tombol_43.setFont(font4)
        self.tombol_43.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_43.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_171.addWidget(self.tombol_43, 2, 0, 1, 4)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_171.addItem(self.horizontalSpacer_44, 1, 1, 1, 1)


        self.gridLayout_170.addWidget(self.frame_102, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_19, 9, 0, 1, 1)

        self.recomended_20 = QFrame(self.frame_3)
        self.recomended_20.setObjectName(u"recomended_20")
        self.recomended_20.setMaximumSize(QSize(16777215, 192))
        self.recomended_20.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;")
        self.recomended_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.recomended_20.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_172 = QGridLayout(self.recomended_20)
        self.gridLayout_172.setSpacing(0)
        self.gridLayout_172.setObjectName(u"gridLayout_172")
        self.gridLayout_172.setContentsMargins(0, 0, 0, 0)
        self.image_produc_44 = QFrame(self.recomended_20)
        self.image_produc_44.setObjectName(u"image_produc_44")
        self.image_produc_44.setMinimumSize(QSize(190, 190))
        self.image_produc_44.setMaximumSize(QSize(190, 190))
        self.image_produc_44.setStyleSheet(u"border-width: 0px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_produc_44.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_produc_44.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_172.addWidget(self.image_produc_44, 0, 0, 1, 1)

        self.frame_103 = QFrame(self.recomended_20)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(188, 0))
        self.frame_103.setStyleSheet(u"border-width: 0px;")
        self.frame_103.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_173 = QGridLayout(self.frame_103)
        self.gridLayout_173.setObjectName(u"gridLayout_173")
        self.gridLayout_173.setHorizontalSpacing(0)
        self.gridLayout_173.setVerticalSpacing(16)
        self.produk_44 = QLabel(self.frame_103)
        self.produk_44.setObjectName(u"produk_44")
        self.produk_44.setMaximumSize(QSize(16777215, 60))
        self.produk_44.setFont(font8)
        self.produk_44.setScaledContents(True)
        self.produk_44.setWordWrap(True)

        self.gridLayout_173.addWidget(self.produk_44, 0, 0, 1, 4)

        self.diskon_44 = QPushButton(self.frame_103)
        self.diskon_44.setObjectName(u"diskon_44")
        self.diskon_44.setFont(font9)
        self.diskon_44.setStyleSheet(u"color: rgb(21, 134, 231);")
        self.diskon_44.setIcon(icon10)
        self.diskon_44.setIconSize(QSize(20, 20))

        self.gridLayout_173.addWidget(self.diskon_44, 1, 2, 1, 1)

        self.harga_44 = QLabel(self.frame_103)
        self.harga_44.setObjectName(u"harga_44")
        self.harga_44.setMaximumSize(QSize(16777215, 30))
        self.harga_44.setFont(font10)
        self.harga_44.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_173.addWidget(self.harga_44, 1, 0, 1, 1)

        self.tombol_44 = QPushButton(self.frame_103)
        self.tombol_44.setObjectName(u"tombol_44")
        self.tombol_44.setMinimumSize(QSize(0, 40))
        self.tombol_44.setFont(font4)
        self.tombol_44.setCursor(QCursor(Qt.PointingHandCursor))
        self.tombol_44.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_173.addWidget(self.tombol_44, 2, 0, 1, 4)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_173.addItem(self.horizontalSpacer_45, 1, 1, 1, 1)


        self.gridLayout_172.addWidget(self.frame_103, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.recomended_20, 9, 1, 1, 1)


        self.gridLayout_14.addWidget(self.frame_3, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_5, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.main_home)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.search.setStyleSheet(u"")
        self.gridLayout_17 = QGridLayout(self.search)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.search)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_4)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(9, 9, 9, 9)
        self.listWidget = QListWidget(self.frame_4)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget.setWordWrap(False)
        self.listWidget.setSelectionRectVisible(False)

        self.gridLayout_20.addWidget(self.listWidget, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame = QFrame(self.search)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"background-color: rgb(21, 134, 231);\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frame)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(8, 4, 8, 4)
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(200, 30))
        self.lineEdit_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.lineEdit_3.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color:rgb(57, 115, 172);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_19.addWidget(self.lineEdit_3, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u"./views/res/icons/icons8-search-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon11)
        self.pushButton.setIconSize(QSize(25, 25))

        self.gridLayout_19.addWidget(self.pushButton, 0, 1, 1, 1)


        self.gridLayout_17.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.search)
        self.discount = QWidget()
        self.discount.setObjectName(u"discount")
        self.gridLayout_21 = QGridLayout(self.discount)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.discount)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 50))
        self.frame_9.setStyleSheet(u"background-color: rgb(21, 134, 231);\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_9)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(8, 4, 8, 4)
        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(30, 30))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setIcon(icon11)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.gridLayout_22.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_9)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(200, 30))
        self.lineEdit_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.lineEdit_6.setStyleSheet(u"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color:rgb(57, 115, 172);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_22.addWidget(self.lineEdit_6, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frame_9, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.discount)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_10)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.listWidget_2 = QListWidget(self.frame_10)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout_23.addWidget(self.listWidget_2, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frame_10, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.discount)
        self.nrw_arrivals = QWidget()
        self.nrw_arrivals.setObjectName(u"nrw_arrivals")
        self.gridLayout_35 = QGridLayout(self.nrw_arrivals)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.listWidget_3 = QListWidget(self.nrw_arrivals)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout_35.addWidget(self.listWidget_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.nrw_arrivals)
        self.being_packed = QWidget()
        self.being_packed.setObjectName(u"being_packed")
        self.gridLayout_39 = QGridLayout(self.being_packed)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.listWidget_7 = QListWidget(self.being_packed)
        self.listWidget_7.setObjectName(u"listWidget_7")

        self.gridLayout_39.addWidget(self.listWidget_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.being_packed)
        self.cancelled = QWidget()
        self.cancelled.setObjectName(u"cancelled")
        self.gridLayout_36 = QGridLayout(self.cancelled)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.listWidget_4 = QListWidget(self.cancelled)
        self.listWidget_4.setObjectName(u"listWidget_4")

        self.gridLayout_36.addWidget(self.listWidget_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.cancelled)
        self.sent = QWidget()
        self.sent.setObjectName(u"sent")
        self.gridLayout_38 = QGridLayout(self.sent)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.listWidget_6 = QListWidget(self.sent)
        self.listWidget_6.setObjectName(u"listWidget_6")

        self.gridLayout_38.addWidget(self.listWidget_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.sent)
        self.completed = QWidget()
        self.completed.setObjectName(u"completed")
        self.gridLayout_37 = QGridLayout(self.completed)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.listWidget_5 = QListWidget(self.completed)
        self.listWidget_5.setObjectName(u"listWidget_5")

        self.gridLayout_37.addWidget(self.listWidget_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.completed)
        self.charts = QWidget()
        self.charts.setObjectName(u"charts")
        self.gridLayout_40 = QGridLayout(self.charts)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.listWidget_8 = QListWidget(self.charts)
        self.listWidget_8.setObjectName(u"listWidget_8")

        self.gridLayout_40.addWidget(self.listWidget_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.charts)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 2, 1, 1)

        user_MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(user_MainWindow)
        self.pushButton_10.toggled.connect(self.big_sidebar.setVisible)
        self.pushButton_10.toggled.connect(self.mini_sidebar.setHidden)
        self.mini_btn_home.toggled.connect(self.big_btn_home.setChecked)
        self.mini_btn_search.toggled.connect(self.big_btn_search.setChecked)
        self.mini_btn_discount.toggled.connect(self.big_btn_discount.setChecked)
        self.mini_btn_new.toggled.connect(self.big_btn_new.setChecked)
        self.mini_btn_order.toggled.connect(self.big_btn_order.setChecked)
        self.mini_btn_settings.toggled.connect(self.big_btn_settings.setChecked)
        self.big_btn_settings.toggled.connect(self.mini_btn_settings.setChecked)
        self.big_btn_order.toggled.connect(self.mini_btn_order.setChecked)
        self.big_btn_new.toggled.connect(self.mini_btn_new.setChecked)
        self.big_btn_discount.toggled.connect(self.mini_btn_discount.setChecked)
        self.big_btn_search.toggled.connect(self.mini_btn_search.setChecked)
        self.big_btn_home.toggled.connect(self.mini_btn_home.setChecked)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(user_MainWindow)
    # setupUi

    def retranslateUi(self, user_MainWindow):
        user_MainWindow.setWindowTitle(QCoreApplication.translate("user_MainWindow", u"MainWindow", None))
        self.mini_btn_logout.setText("")
        self.mini_btn_order.setText("")
        self.mini_btn_search.setText("")
        self.mini_btn_settings.setText("")
        self.mini_btn_discount.setText("")
        self.mini_btn_home.setText("")
        self.mini_btn_new.setText("")
        self.shop_name.setText(QCoreApplication.translate("user_MainWindow", u"Pro Shop", None))
        self.big_btn_logout.setText(QCoreApplication.translate("user_MainWindow", u" Log Out", None))
        self.big_btn_discount.setText(QCoreApplication.translate("user_MainWindow", u" Discount", None))
        self.big_btn_search.setText(QCoreApplication.translate("user_MainWindow", u" Search", None))
        self.big_btn_settings.setText(QCoreApplication.translate("user_MainWindow", u" Settings", None))
        self.big_btn_new.setText(QCoreApplication.translate("user_MainWindow", u" New Arrivals", None))
        self.big_btn_order.setText(QCoreApplication.translate("user_MainWindow", u" My Order", None))
        self.big_btn_home.setText(QCoreApplication.translate("user_MainWindow", u" Home", None))
        self.label_9.setText(QCoreApplication.translate("user_MainWindow", u"Welcome to ProShop", None))
        self.welcome_txt.setText(QCoreApplication.translate("user_MainWindow", u"Hello,", None))
        self.wave_anim.setText("")
        self.pushButton_10.setText("")
        self.money.setText(QCoreApplication.translate("user_MainWindow", u"Rp 0", None))
        self.profiile.setText("")
        self.btn_wallet.setText("")
        self.chart.setText("")
        self.discount_text.setText(QCoreApplication.translate("user_MainWindow", u"Discount", None))
        self.disc_label_6.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.150.000", None))
        self.price_6.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.000.000", None))
        self.produc_name_6.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dorem lorem imsum", None))
        self.buy_btn_6.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.disc_label_4.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.150.000", None))
        self.price_4.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.000.000", None))
        self.produc_name_4.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dorem lorem imsum", None))
        self.buy_btn_4.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.disc_label_5.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.150.000", None))
        self.price_5.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.000.000", None))
        self.produc_name_5.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dorem lorem imsum", None))
        self.buy_btn_5.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.disc_label_8.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.150.000", None))
        self.price_8.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.000.000", None))
        self.produc_name_8.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dorem lorem imsum", None))
        self.buy_btn_8.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.disc_label_9.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.150.000", None))
        self.price_9.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.000.000", None))
        self.produc_name_9.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dorem lorem imsum", None))
        self.buy_btn_9.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.disc_label_7.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.150.000", None))
        self.price_7.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.000.000", None))
        self.produc_name_7.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dorem lorem imsum", None))
        self.buy_btn_7.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.disc_label.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.150.000", None))
        self.price.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.000.000", None))
        self.produc_name.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dorem lorem imsum", None))
        self.buy_btn.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.disc_label_10.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.150.000", None))
        self.price_10.setText(QCoreApplication.translate("user_MainWindow", u"Rp 1.000.000", None))
        self.produc_name_10.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dorem lorem imsum", None))
        self.buy_btn_10.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.label_2.setText(QCoreApplication.translate("user_MainWindow", u"Recomended", None))
        self.produk_26.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_26.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_26.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_26.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_42.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_42.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_42.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_42.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_27.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_27.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_27.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_27.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_31.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_31.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_31.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_31.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_40.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_40.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_40.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_40.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_33.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_33.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_33.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_33.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_38.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_38.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_38.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_38.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_36.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_36.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_36.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_36.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_32.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_32.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_32.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_32.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_35.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_35.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_35.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_35.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_37.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_37.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_37.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_37.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_29.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_29.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_29.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_29.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_30.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_30.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_30.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_30.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_34.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_34.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_34.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_34.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_28.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_28.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_28.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_28.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_41.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_41.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_41.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_41.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_39.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_39.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_39.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_39.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_43.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_43.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_43.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_43.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.produk_44.setText(QCoreApplication.translate("user_MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.", None))
        self.diskon_44.setText(QCoreApplication.translate("user_MainWindow", u"10%", None))
        self.harga_44.setText(QCoreApplication.translate("user_MainWindow", u"Rp 100.000", None))
        self.tombol_44.setText(QCoreApplication.translate("user_MainWindow", u"Buy", None))
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("user_MainWindow", u"Search here", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("user_MainWindow", u"Search here", None))
    # retranslateUi

