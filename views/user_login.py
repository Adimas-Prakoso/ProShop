from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
    QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QStackedWidget, QWidget)

class user_login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 395)
        MainWindow.setMinimumSize(QSize(780, 395))
        MainWindow.setMaximumSize(QSize(780, 395))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(780, 395))
        self.centralwidget.setMaximumSize(QSize(780, 395))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(780, 395))
        self.frame_3.setMaximumSize(QSize(780, 395))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.gridLayout_5 = QGridLayout(self.login)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.image = QFrame(self.login)
        self.image.setObjectName(u"image")
        self.image.setMaximumSize(QSize(390, 395))
        self.image.setStyleSheet(u"border-radius: 10px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image.setFrameShape(QFrame.Shape.StyledPanel)
        self.image.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.image)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_5.addWidget(self.image, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.login)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(8, -1, 9, -1)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 170, 127);\n"
"")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(0)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 2)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 5, 5, 5)
        self.verification = QLineEdit(self.frame)
        self.verification.setObjectName(u"verification")
        self.verification.setMinimumSize(QSize(0, 40))
        self.verification.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px")

        self.gridLayout_3.addWidget(self.verification, 0, 0, 1, 1)

        self.send_code = QPushButton(self.frame)
        self.send_code.setObjectName(u"send_code")
        self.send_code.setMinimumSize(QSize(50, 35))
        font1 = QFont()
        font1.setBold(True)
        self.send_code.setFont(font1)
        self.send_code.setCursor(QCursor(Qt.PointingHandCursor))
        self.send_code.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 170, 127);\n"
"	border-top-right-radius: 10px;\n"
"	border-color: rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(193, 128, 96)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 210, 133)\n"
"}")

        self.gridLayout_3.addWidget(self.send_code, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame, 5, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(6)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.password = QLineEdit(self.frame_7)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 40))
        self.password.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px")
        self.password.setMaxLength(32767)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_9.addWidget(self.password, 0, 0, 1, 1)

        self.show_btn = QPushButton(self.frame_7)
        self.show_btn.setObjectName(u"show_btn")
        self.show_btn.setMaximumSize(QSize(40, 40))
        self.show_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_btn.setStyleSheet(u"QPushButton: {\n"
"	color: rgb(255, 170, 127);\n"
"}")
        icon = QIcon()
        icon.addFile(u"./views/res/icons/icons8-hide-500.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"./views/res/icons/icons8-show-500.png", QSize(), QIcon.Normal, QIcon.On)
        self.show_btn.setIcon(icon)
        self.show_btn.setIconSize(QSize(30, 30))
        self.show_btn.setCheckable(True)

        self.gridLayout_9.addWidget(self.show_btn, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_7, 3, 0, 1, 2)

        self.emails = QLineEdit(self.frame_6)
        self.emails.setObjectName(u"emails")
        self.emails.setMinimumSize(QSize(0, 40))
        self.emails.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px")
        self.emails.setClearButtonEnabled(False)

        self.gridLayout_7.addWidget(self.emails, 1, 0, 1, 2)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_2.setFont(font2)

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 2)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout_7.addWidget(self.label_8, 4, 0, 1, 2)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setFont(font2)

        self.gridLayout_7.addWidget(self.label_3, 2, 0, 1, 2)


        self.gridLayout_6.addWidget(self.frame_6, 1, 0, 1, 2)

        self.regis_btn = QPushButton(self.frame_5)
        self.regis_btn.setObjectName(u"regis_btn")
        self.regis_btn.setMinimumSize(QSize(0, 35))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.regis_btn.setFont(font3)
        self.regis_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.regis_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 170, 127);\n"
"	border-top-right-radius: 10px;\n"
"	border-color: rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(193, 128, 96)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 210, 133)\n"
"}")

        self.gridLayout_6.addWidget(self.regis_btn, 3, 0, 1, 2)

        self.login_btn = QPushButton(self.frame_5)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(0, 60))
        self.login_btn.setFont(font3)
        self.login_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 170, 127);\n"
"	border-top-right-radius: 10px;\n"
"	border-color: rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(193, 128, 96)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 210, 133)\n"
"}")

        self.gridLayout_6.addWidget(self.login_btn, 2, 0, 1, 2)


        self.gridLayout_5.addWidget(self.frame_5, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.login)
        self.regis = QWidget()
        self.regis.setObjectName(u"regis")
        self.gridLayout_11 = QGridLayout(self.regis)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.regis)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_9)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(8, -1, -1, -1)
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 170, 127);\n"
"")
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(0)

        self.gridLayout_12.addWidget(self.label_4, 0, 0, 1, 2)

        self.reg_btn = QPushButton(self.frame_9)
        self.reg_btn.setObjectName(u"reg_btn")
        self.reg_btn.setMinimumSize(QSize(0, 50))
        self.reg_btn.setFont(font3)
        self.reg_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.reg_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 170, 127);\n"
"	border-top-right-radius: 10px;\n"
"	border-color: rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(193, 128, 96)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 210, 133)\n"
"}")

        self.gridLayout_12.addWidget(self.reg_btn, 2, 0, 1, 2)

        self.login_btn_2 = QPushButton(self.frame_9)
        self.login_btn_2.setObjectName(u"login_btn_2")
        self.login_btn_2.setMinimumSize(QSize(0, 35))
        self.login_btn_2.setFont(font3)
        self.login_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_btn_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 170, 127);\n"
"	border-top-right-radius: 10px;\n"
"	border-color: rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(193, 128, 96)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 210, 133)\n"
"}")

        self.gridLayout_12.addWidget(self.login_btn_2, 3, 0, 1, 2)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_10)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(10, 10, 10, 10)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_11)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(6)
        self.gridLayout_14.setVerticalSpacing(0)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.show_btn_2 = QPushButton(self.frame_11)
        self.show_btn_2.setObjectName(u"show_btn_2")
        self.show_btn_2.setMaximumSize(QSize(40, 40))
        self.show_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_btn_2.setStyleSheet(u"QPushButton: {\n"
"	color: rgb(255, 170, 127);\n"
"}")
        self.show_btn_2.setIcon(icon)
        self.show_btn_2.setIconSize(QSize(30, 30))
        self.show_btn_2.setCheckable(True)

        self.gridLayout_14.addWidget(self.show_btn_2, 0, 1, 1, 1)

        self.reg_password = QLineEdit(self.frame_11)
        self.reg_password.setObjectName(u"reg_password")
        self.reg_password.setMinimumSize(QSize(0, 40))
        self.reg_password.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px")
        self.reg_password.setMaxLength(0)
        self.reg_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_14.addWidget(self.reg_password, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_11, 5, 0, 1, 1)

        self.reg_username = QLineEdit(self.frame_10)
        self.reg_username.setObjectName(u"reg_username")
        self.reg_username.setMinimumSize(QSize(0, 40))
        self.reg_username.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px")

        self.gridLayout_13.addWidget(self.reg_username, 1, 0, 1, 2)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout_13.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setFont(font2)

        self.gridLayout_13.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))
        self.label_5.setFont(font2)

        self.gridLayout_13.addWidget(self.label_5, 0, 0, 1, 1)

        self.reg_email = QLineEdit(self.frame_10)
        self.reg_email.setObjectName(u"reg_email")
        self.reg_email.setMinimumSize(QSize(0, 40))
        self.reg_email.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px")

        self.gridLayout_13.addWidget(self.reg_email, 3, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_10, 1, 0, 1, 2)


        self.gridLayout_11.addWidget(self.frame_9, 0, 1, 1, 1)

        self.image_2 = QFrame(self.regis)
        self.image_2.setObjectName(u"image_2")
        self.image_2.setMaximumSize(QSize(390, 395))
        self.image_2.setStyleSheet(u"border-radius: 10px;\n"
"border-image: url(./views/res/images/logo.jpeg);")
        self.image_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.image_2)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_11.addWidget(self.image_2, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.regis)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.verification.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input Verification code!", None))
        self.send_code.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Input Password!", None))
        self.show_btn.setText("")
        self.emails.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Input Email!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Verification Code", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.regis_btn.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.reg_btn.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.login_btn_2.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.show_btn_2.setText("")
        self.reg_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Input Password!", None))
        self.reg_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Input Username!", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.reg_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Input Email!", None))
    # retranslateUi

