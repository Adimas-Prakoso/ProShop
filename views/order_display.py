# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_displaybBottX.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem,
    QWidget)

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
        self.horizontalLayout.setContentsMargins(0, 0, 9, 0)
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
        self.names_itm = QLabel(self.frame)
        self.names_itm.setObjectName(u"names_itm")
        self.names_itm.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(10)
        font.setBold(True)
        self.names_itm.setFont(font)
        self.names_itm.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.names_itm, 0, 0, 1, 3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.quantity = QLabel(self.frame_2)
        self.quantity.setObjectName(u"quantity")

        self.gridLayout_2.addWidget(self.quantity, 1, 1, 1, 1)

        self.label_status = QLabel(self.frame_2)
        self.label_status.setObjectName(u"label_status")

        self.gridLayout_2.addWidget(self.label_status, 2, 0, 1, 1)

        self.label_quantity = QLabel(self.frame_2)
        self.label_quantity.setObjectName(u"label_quantity")

        self.gridLayout_2.addWidget(self.label_quantity, 1, 0, 1, 1)

        self.discount_itm = QLabel(self.frame_2)
        self.discount_itm.setObjectName(u"discount_itm")
        self.discount_itm.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setItalic(True)
        font1.setStrikeOut(True)
        self.discount_itm.setFont(font1)
        self.discount_itm.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_2.addWidget(self.discount_itm, 0, 0, 1, 1)

        self.itm_price = QLabel(self.frame_2)
        self.itm_price.setObjectName(u"itm_price")
        font2 = QFont()
        font2.setBold(True)
        self.itm_price.setFont(font2)
        self.itm_price.setStyleSheet(u"color: rgb(0, 255, 247);")

        self.gridLayout_2.addWidget(self.itm_price, 0, 1, 1, 1)

        self.status_barang = QLabel(self.frame_2)
        self.status_barang.setObjectName(u"status_barang")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        self.status_barang.setFont(font3)
        self.status_barang.setStyleSheet(u"color: rgb(0, 255, 0);")

        self.gridLayout_2.addWidget(self.status_barang, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 3)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.names_itm.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.quantity.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.label_quantity.setText(QCoreApplication.translate("MainWindow", u"Quantity :", None))
        self.discount_itm.setText(QCoreApplication.translate("MainWindow", u"ppppppp", None))
        self.itm_price.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.status_barang.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

