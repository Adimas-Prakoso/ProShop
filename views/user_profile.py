# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QWidget)

class Ui_profile(object):
    def setupUi(self, profile):
        if not profile.objectName():
            profile.setObjectName(u"profile")
        profile.resize(400, 600)
        profile.setMinimumSize(QSize(400, 600))
        profile.setMaximumSize(QSize(400, 600))
        self.centralwidget = QWidget(profile)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(400, 600))
        self.centralwidget.setMaximumSize(QSize(400, 600))
        self.centralwidget.setStyleSheet(u"background-color: rgb(21, 134, 231);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 390, 673))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 230))
        self.frame.setMaximumSize(QSize(16777215, 230))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.image_profile = QFrame(self.frame)
        self.image_profile.setObjectName(u"image_profile")
        self.image_profile.setMinimumSize(QSize(150, 150))
        self.image_profile.setMaximumSize(QSize(150, 150))
        self.image_profile.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 75px;")
        self.image_profile.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_profile.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_3.addWidget(self.image_profile, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.change_btn = QPushButton(self.frame)
        self.change_btn.setObjectName(u"change_btn")
        self.change_btn.setMinimumSize(QSize(300, 30))
        self.change_btn.setMaximumSize(QSize(300, 30))
        font = QFont()
        font.setBold(True)
        self.change_btn.setFont(font)
        self.change_btn.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.change_btn, 2, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 2, 4, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(4)
        self.btn_gender = QPushButton(self.frame_2)
        self.btn_gender.setObjectName(u"btn_gender")
        self.btn_gender.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.btn_gender.setFont(font1)
        self.btn_gender.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.btn_gender, 9, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 25))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Black"])
        font2.setPointSize(10)
        self.label_3.setFont(font2)

        self.gridLayout_4.addWidget(self.label_3, 4, 0, 1, 2)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 25))
        self.label_5.setFont(font2)

        self.gridLayout_4.addWidget(self.label_5, 8, 0, 1, 2)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 25))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        self.label_4.setFont(font3)

        self.gridLayout_4.addWidget(self.label_4, 6, 0, 1, 2)

        self.btn_bio = QPushButton(self.frame_2)
        self.btn_bio.setObjectName(u"btn_bio")
        self.btn_bio.setMinimumSize(QSize(0, 35))
        self.btn_bio.setFont(font)
        self.btn_bio.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.btn_bio, 3, 1, 1, 1)

        self.phone = QLineEdit(self.frame_2)
        self.phone.setObjectName(u"phone")
        self.phone.setMinimumSize(QSize(0, 35))
        self.phone.setMaximumSize(QSize(16777215, 16777215))
        self.phone.setFont(font3)
        self.phone.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"color: rgb(255, 255, 255);\n"
"background-color:  rgb(255, 170, 127);")

        self.gridLayout_4.addWidget(self.phone, 7, 0, 1, 1)

        self.nama = QLineEdit(self.frame_2)
        self.nama.setObjectName(u"nama")
        self.nama.setMinimumSize(QSize(0, 35))
        self.nama.setFont(font3)
        self.nama.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"color: rgb(255, 255, 255);\n"
"background-color:  rgb(255, 170, 127);")

        self.gridLayout_4.addWidget(self.nama, 1, 0, 1, 1)

        self.btn_nama = QPushButton(self.frame_2)
        self.btn_nama.setObjectName(u"btn_nama")
        self.btn_nama.setMinimumSize(QSize(70, 35))
        self.btn_nama.setFont(font)
        self.btn_nama.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.btn_nama, 1, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 2)

        self.btn_phone = QPushButton(self.frame_2)
        self.btn_phone.setObjectName(u"btn_phone")
        self.btn_phone.setMinimumSize(QSize(0, 35))
        self.btn_phone.setFont(font)
        self.btn_phone.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.btn_phone, 7, 1, 1, 1)

        self.alamat = QLineEdit(self.frame_2)
        self.alamat.setObjectName(u"alamat")
        self.alamat.setMinimumSize(QSize(0, 35))
        self.alamat.setFont(font3)
        self.alamat.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"color: rgb(255, 255, 255);\n"
"background-color:  rgb(255, 170, 127);")

        self.gridLayout_4.addWidget(self.alamat, 5, 0, 1, 1)

        self.bio = QLineEdit(self.frame_2)
        self.bio.setObjectName(u"bio")
        self.bio.setMinimumSize(QSize(0, 35))
        self.bio.setFont(font3)
        self.bio.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"color: rgb(255, 255, 255);\n"
"background-color:  rgb(255, 170, 127);")

        self.gridLayout_4.addWidget(self.bio, 3, 0, 1, 1)

        self.btn_alamat = QPushButton(self.frame_2)
        self.btn_alamat.setObjectName(u"btn_alamat")
        self.btn_alamat.setMinimumSize(QSize(0, 35))
        self.btn_alamat.setFont(font)
        self.btn_alamat.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.btn_alamat, 5, 1, 1, 1)

        self.gender = QComboBox(self.frame_2)
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.setObjectName(u"gender")
        self.gender.setMinimumSize(QSize(0, 35))
        self.gender.setFont(font3)
        self.gender.setStyleSheet(u"QComboBox {\n"
"	border-radius: 12px;\n"
"	border-color: rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:  rgb(255, 170, 127);\n"
"}\n"
"QComboBox::drop-down {\n"
"	width: 0px;\n"
"	border: none;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: none;\n"
"}")

        self.gridLayout_4.addWidget(self.gender, 9, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 2)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout_4.addWidget(self.label_6, 10, 0, 1, 1)

        self.btn_lahir = QPushButton(self.frame_2)
        self.btn_lahir.setObjectName(u"btn_lahir")
        self.btn_lahir.setMinimumSize(QSize(0, 35))
        self.btn_lahir.setFont(font)
        self.btn_lahir.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.btn_lahir, 11, 1, 1, 1)

        self.lahir = QLineEdit(self.frame_2)
        self.lahir.setObjectName(u"lahir")
        self.lahir.setMinimumSize(QSize(0, 35))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Black"])
        font4.setBold(True)
        self.lahir.setFont(font4)
        self.lahir.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"color: rgb(255, 255, 255);\n"
"background-color:  rgb(255, 170, 127);")

        self.gridLayout_4.addWidget(self.lahir, 11, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(0, 40))
        self.save_btn.setMaximumSize(QSize(16777215, 40))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI Black"])
        font5.setPointSize(11)
        self.save_btn.setFont(font5)
        self.save_btn.setStyleSheet(u"QPushButton{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"	border-width: 3px;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.save_btn, 2, 0, 1, 1)

        profile.setCentralWidget(self.centralwidget)

        self.retranslateUi(profile)

        QMetaObject.connectSlotsByName(profile)

        self.nama.setDisabled(True)
        self.phone.setDisabled(True)
        self.alamat.setDisabled(True)
        self.bio.setDisabled(True)
        self.gender.setDisabled(True)
        self.lahir.setDisabled(True)
        
    # setupUi

    def retranslateUi(self, profile):
        profile.setWindowTitle(QCoreApplication.translate("profile", u"MainWindow", None))
        self.change_btn.setText(QCoreApplication.translate("profile", u"Change Profile Image", None))
        self.btn_gender.setText(QCoreApplication.translate("profile", u"Ubah", None))
        self.label_3.setText(QCoreApplication.translate("profile", u"Alamat :", None))
        self.label_5.setText(QCoreApplication.translate("profile", u"Gender :", None))
        self.label_4.setText(QCoreApplication.translate("profile", u"Nomor Telfon :", None))
        self.btn_bio.setText(QCoreApplication.translate("profile", u"Ubah", None))
        self.phone.setPlaceholderText(QCoreApplication.translate("profile", u"Dengan 62 bukan 08", None))
        self.nama.setPlaceholderText(QCoreApplication.translate("profile", u"Nama", None))
        self.btn_nama.setText(QCoreApplication.translate("profile", u"Ubah", None))
        self.label.setText(QCoreApplication.translate("profile", u"Nama :", None))
        self.btn_phone.setText(QCoreApplication.translate("profile", u"Ubah", None))
        self.alamat.setPlaceholderText(QCoreApplication.translate("profile", u"Nomor rumah, Nama jalan, Nama kelurahan, Nama kecamatan, Nama kota, Nama provinsi", None))
        self.bio.setPlaceholderText(QCoreApplication.translate("profile", u"Bio", None))
        self.btn_alamat.setText(QCoreApplication.translate("profile", u"Ubah", None))
        self.gender.setItemText(0, QCoreApplication.translate("profile", u"Pria", None))
        self.gender.setItemText(1, QCoreApplication.translate("profile", u"Wanita", None))

        self.gender.setPlaceholderText(QCoreApplication.translate("profile", u"Pria/Wanita", None))
        self.label_2.setText(QCoreApplication.translate("profile", u"Bio :", None))
        self.label_6.setText(QCoreApplication.translate("profile", u"Tanggal lLahir :", None))
        self.btn_lahir.setText(QCoreApplication.translate("profile", u"Ubah", None))
        self.lahir.setPlaceholderText(QCoreApplication.translate("profile", u"Tanggal/Bulan/Tahun", None))
        self.save_btn.setText(QCoreApplication.translate("profile", u"SAVE", None))
    # retranslateUi

