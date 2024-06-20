# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_displayYiPjVm.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(696, 150)
        MainWindow.setMaximumSize(QSize(16777215, 150))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.item_images = QFrame(self.centralwidget)
        self.item_images.setObjectName(u"item_images")
        self.item_images.setMinimumSize(QSize(150, 150))
        self.item_images.setMaximumSize(QSize(150, 150))
        self.item_images.setFrameShape(QFrame.Shape.StyledPanel)
        self.item_images.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.item_images)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setStyleSheet(u"background-color: transparent;")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.the_category = QLabel(self.frame)
        self.the_category.setObjectName(u"the_category")
        self.the_category.setMinimumSize(QSize(86, 0))
        self.the_category.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setBold(True)
        self.the_category.setFont(font)
        self.the_category.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"padding-left: 10;\n"
"padding-right: 10;")
        self.the_category.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.the_category, 2, 1, 1, 1)

        self.categ = QLabel(self.frame)
        self.categ.setObjectName(u"categ")

        self.gridLayout.addWidget(self.categ, 2, 0, 1, 1)

        self.desc = QLabel(self.frame)
        self.desc.setObjectName(u"desc")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Light"])
        font1.setItalic(True)
        self.desc.setFont(font1)
        self.desc.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.desc, 1, 0, 1, 4)

        self.names_itm = QLabel(self.frame)
        self.names_itm.setObjectName(u"names_itm")
        self.names_itm.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Black"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.names_itm.setFont(font2)
        self.names_itm.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.names_itm, 0, 0, 1, 4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.itm_price = QLabel(self.frame_2)
        self.itm_price.setObjectName(u"itm_price")
        self.itm_price.setFont(font)
        self.itm_price.setStyleSheet(u"color: rgb(0, 255, 247);")

        self.gridLayout_2.addWidget(self.itm_price, 0, 1, 1, 1)

        self.discount_itm = QLabel(self.frame_2)
        self.discount_itm.setObjectName(u"discount_itm")
        self.discount_itm.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setItalic(True)
        font3.setStrikeOut(True)
        self.discount_itm.setFont(font3)
        self.discount_itm.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_2.addWidget(self.discount_itm, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 3)


        self.horizontalLayout.addWidget(self.frame)

        self.Buy_button = QPushButton(self.centralwidget)
        self.Buy_button.setObjectName(u"Buy_button")
        self.Buy_button.setMinimumSize(QSize(130, 130))
        self.Buy_button.setMaximumSize(QSize(130, 130))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Black"])
        font4.setPointSize(13)
        self.Buy_button.setFont(font4)
        self.Buy_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Buy_button.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.horizontalLayout.addWidget(self.Buy_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.the_category.setText(QCoreApplication.translate("MainWindow", u"CATEGORY", None))
        self.categ.setText(QCoreApplication.translate("MainWindow", u"Category :", None))
        self.desc.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.names_itm.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.itm_price.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.discount_itm.setText(QCoreApplication.translate("MainWindow", u"ppppppp", None))
        self.Buy_button.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
    # retranslateUi

