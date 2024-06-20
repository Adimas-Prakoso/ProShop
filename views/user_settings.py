from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QCursor,
    QFont)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_settings(object):
    def setupUi(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"settings")
        settings.resize(500, 550)
        settings.setMinimumSize(QSize(500, 550))
        settings.setMaximumSize(QSize(500, 550))
        self.centralwidget = QWidget(settings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setCursor(QCursor(Qt.ArrowCursor))
        self.frame.setStyleSheet(u"background-color: rgb(21, 134, 231);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(15)
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 498, 930))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(21, 134, 231);;\n"
"}\n"
"")
        self.pushButton.setCheckable(True)

        self.gridLayout_6.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pass_frame = QFrame(self.frame_4)
        self.pass_frame.setObjectName(u"pass_frame")
        self.pass_frame.setMinimumSize(QSize(0, 240))
        self.pass_frame.setMaximumSize(QSize(16777215, 240))
        self.pass_frame.setStyleSheet(u"background-color: rgb(245, 235, 223);")
        self.pass_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.pass_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.pass_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_6 = QLabel(self.pass_frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)

        self.btn_pass_verif = QPushButton(self.pass_frame)
        self.btn_pass_verif.setObjectName(u"btn_pass_verif")
        self.btn_pass_verif.setMinimumSize(QSize(50, 30))
        self.btn_pass_verif.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pass_verif.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.btn_pass_verif, 5, 1, 1, 1)

        self.label_7 = QLabel(self.pass_frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_7.addWidget(self.label_7, 2, 0, 1, 1)

        self.passwor_baru = QLineEdit(self.pass_frame)
        self.passwor_baru.setObjectName(u"passwor_baru")
        self.passwor_baru.setMinimumSize(QSize(0, 30))

        self.gridLayout_7.addWidget(self.passwor_baru, 3, 0, 1, 2)

        self.pass_verifikasi = QLineEdit(self.pass_frame)
        self.pass_verifikasi.setObjectName(u"pass_verifikasi")
        self.pass_verifikasi.setMinimumSize(QSize(0, 30))

        self.gridLayout_7.addWidget(self.pass_verifikasi, 5, 0, 1, 1)

        self.password_saatini = QLineEdit(self.pass_frame)
        self.password_saatini.setObjectName(u"password_saatini")
        self.password_saatini.setMinimumSize(QSize(0, 30))

        self.gridLayout_7.addWidget(self.password_saatini, 1, 0, 1, 2)

        self.label_8 = QLabel(self.pass_frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 4, 0, 1, 1)

        self.save_pass = QPushButton(self.pass_frame)
        self.save_pass.setObjectName(u"save_pass")
        self.save_pass.setMinimumSize(QSize(0, 30))
        self.save_pass.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_pass.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.save_pass, 6, 0, 1, 2)


        self.gridLayout_6.addWidget(self.pass_frame, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(21, 134, 231);;\n"
"}\n"
"")
        self.pushButton_2.setCheckable(True)

        self.gridLayout_4.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.penga_frame = QFrame(self.frame_2)
        self.penga_frame.setObjectName(u"penga_frame")
        self.penga_frame.setMinimumSize(QSize(0, 300))
        self.penga_frame.setMaximumSize(QSize(16777215, 300))
        self.penga_frame.setStyleSheet(u"background-color: rgb(245, 235, 223);")
        self.penga_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.penga_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.penga_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_5 = QLabel(self.penga_frame)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_5.setFont(font2)

        self.gridLayout_5.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_3 = QLabel(self.penga_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.penga_frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 30))
        self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.comboBox_2, 1, 0, 1, 1)

        self.matauang = QComboBox(self.penga_frame)
        self.matauang.setObjectName(u"matauang")
        self.matauang.setMinimumSize(QSize(0, 30))
        self.matauang.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.matauang, 6, 0, 1, 1)

        self.aktif = QRadioButton(self.penga_frame)
        self.aktif.setObjectName(u"aktif")
        self.aktif.setCursor(QCursor(Qt.PointingHandCursor))
        self.aktif.setCheckable(True)
        self.aktif.setChecked(True)

        self.gridLayout_5.addWidget(self.aktif, 3, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.penga_frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 30))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"")
        self.pushButton_5.setCheckable(True)

        self.gridLayout_5.addWidget(self.pushButton_5, 7, 0, 1, 1)

        self.label_4 = QLabel(self.penga_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout_5.addWidget(self.label_4, 2, 0, 1, 1)

        self.nonaktif = QRadioButton(self.penga_frame)
        self.nonaktif.setObjectName(u"nonaktif")
        self.nonaktif.setCursor(QCursor(Qt.PointingHandCursor))
        self.nonaktif.setChecked(False)

        self.gridLayout_5.addWidget(self.nonaktif, 4, 0, 1, 1)


        self.gridLayout_4.addWidget(self.penga_frame, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(21, 134, 231);;\n"
"}\n"
"")
        self.pushButton_6.setCheckable(True)

        self.gridLayout_8.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.email_frame = QFrame(self.frame_6)
        self.email_frame.setObjectName(u"email_frame")
        self.email_frame.setMinimumSize(QSize(0, 240))
        self.email_frame.setMaximumSize(QSize(16777215, 240))
        self.email_frame.setStyleSheet(u"background-color: rgb(245, 235, 223);")
        self.email_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.email_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.email_frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_9 = QLabel(self.email_frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)

        self.btn_email_verif = QPushButton(self.email_frame)
        self.btn_email_verif.setObjectName(u"btn_email_verif")
        self.btn_email_verif.setMinimumSize(QSize(50, 30))
        self.btn_email_verif.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_email_verif.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.btn_email_verif, 5, 1, 1, 1)

        self.label_10 = QLabel(self.email_frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_9.addWidget(self.label_10, 2, 0, 1, 1)

        self.email_baru = QLineEdit(self.email_frame)
        self.email_baru.setObjectName(u"email_baru")
        self.email_baru.setMinimumSize(QSize(0, 30))

        self.gridLayout_9.addWidget(self.email_baru, 3, 0, 1, 2)

        self.email_verifikasi = QLineEdit(self.email_frame)
        self.email_verifikasi.setObjectName(u"email_verifikasi")
        self.email_verifikasi.setMinimumSize(QSize(0, 30))

        self.gridLayout_9.addWidget(self.email_verifikasi, 5, 0, 1, 1)

        self.email_saatini = QLineEdit(self.email_frame)
        self.email_saatini.setObjectName(u"email_saatini")
        self.email_saatini.setMinimumSize(QSize(0, 30))

        self.gridLayout_9.addWidget(self.email_saatini, 1, 0, 1, 2)

        self.label_11 = QLabel(self.email_frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_9.addWidget(self.label_11, 4, 0, 1, 1)

        self.save_email = QPushButton(self.email_frame)
        self.save_email.setObjectName(u"save_email")
        self.save_email.setMinimumSize(QSize(0, 30))
        self.save_email.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_email.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(237, 41, 89);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(186, 32, 71);\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.save_email, 6, 0, 1, 2)


        self.gridLayout_8.addWidget(self.email_frame, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_6, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(settings)
        self.pushButton_2.toggled.connect(self.penga_frame.setVisible)
        self.pushButton.toggled.connect(self.pass_frame.setVisible)
        self.pushButton_6.toggled.connect(self.email_frame.setVisible)

        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("settings", u"SETTINGS", None))
        self.pushButton.setText(QCoreApplication.translate("settings", u"UBAH PASSWORD", None))
        self.label_6.setText(QCoreApplication.translate("settings", u"Password Saat Ini", None))
        self.btn_pass_verif.setText(QCoreApplication.translate("settings", u"KIRIM", None))
        self.label_7.setText(QCoreApplication.translate("settings", u"Password Baru", None))
        self.label_8.setText(QCoreApplication.translate("settings", u"Kode Verifikasi", None))
        self.save_pass.setText(QCoreApplication.translate("settings", u"SIMPAN PRUBAHAN", None))
        self.pushButton_2.setText(QCoreApplication.translate("settings", u"PENGATURAN APLIKASI", None))
        self.label_5.setText(QCoreApplication.translate("settings", u"Mata Uang", None))
        self.label_3.setText(QCoreApplication.translate("settings", u"Tema", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("settings", u"Light", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("settings", u"Dark", None))

        self.aktif.setText(QCoreApplication.translate("settings", u"Aktif", None))
        self.pushButton_5.setText(QCoreApplication.translate("settings", u"SIMPAN PERUBAHAN", None))
        self.label_4.setText(QCoreApplication.translate("settings", u"Notifikasi", None))
        self.nonaktif.setText(QCoreApplication.translate("settings", u"Nonaktif", None))
        self.pushButton_6.setText(QCoreApplication.translate("settings", u"UBAH ALAMAT EMAIL", None))
        self.label_9.setText(QCoreApplication.translate("settings", u"Email Saat Ini", None))
        self.btn_email_verif.setText(QCoreApplication.translate("settings", u"KIRIM", None))
        self.label_10.setText(QCoreApplication.translate("settings", u"Email Baru", None))
        self.label_11.setText(QCoreApplication.translate("settings", u"Kode Verifikasi", None))
        self.save_email.setText(QCoreApplication.translate("settings", u"SIMPAN PRUBAHAN", None))
    # retranslateUi

