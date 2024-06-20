from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class admin_login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 465)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 460))
        self.centralwidget.setMaximumSize(QSize(800, 460))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(120, 45))
        self.frame_2.setMaximumSize(QSize(16777215, 45))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(30, 30))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 0)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/icons8-minimize-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton.setCheckable(False)

        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(30, 30))
        self.pushButton_2.setMaximumSize(QSize(30, 30))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 0, 0)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/icons8-close-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.image = QFrame(self.frame_3)
        self.image.setObjectName(u"image")
        self.image.setMaximumSize(QSize(390, 395))
        self.image.setStyleSheet(u"border-radius: 10px;\n"
"border-image: url(:/image/images/logo.jpeg);")
        self.image.setFrameShape(QFrame.Shape.StyledPanel)
        self.image.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.image)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.image, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.adm_login_btn = QPushButton(self.frame_5)
        self.adm_login_btn.setObjectName(u"adm_login_btn")
        self.adm_login_btn.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(10)
        font.setBold(True)
        self.adm_login_btn.setFont(font)
        self.adm_login_btn.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_5.addWidget(self.adm_login_btn, 2, 0, 1, 2)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(10, 10, 10, 10)
        self.adm_username = QLineEdit(self.frame_6)
        self.adm_username.setObjectName(u"adm_username")
        self.adm_username.setMinimumSize(QSize(0, 40))
        self.adm_username.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px")

        self.gridLayout_6.addWidget(self.adm_username, 2, 0, 1, 2)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_2.setFont(font1)

        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setFont(font1)

        self.gridLayout_6.addWidget(self.label_3, 3, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(6)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.show_btn = QPushButton(self.frame_7)
        self.show_btn.setObjectName(u"show_btn")
        self.show_btn.setMaximumSize(QSize(40, 40))
        self.show_btn.setStyleSheet(u"QPushButton: {\n"
"	color: rgb(255, 170, 127);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/icons8-hide-500.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icon/icons/icons8-show-500.png", QSize(), QIcon.Normal, QIcon.On)
        self.show_btn.setIcon(icon2)
        self.show_btn.setIconSize(QSize(30, 30))
        self.show_btn.setCheckable(True)

        self.gridLayout_7.addWidget(self.show_btn, 0, 1, 1, 1)

        self.adm_password = QLineEdit(self.frame_7)
        self.adm_password.setObjectName(u"adm_password")
        self.adm_password.setMinimumSize(QSize(0, 40))
        self.adm_password.setStyleSheet(u"border-radius: 12px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px")
        self.adm_password.setMaxLength(12)
        self.adm_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_7.addWidget(self.adm_password, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_7, 4, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_6, 1, 0, 1, 2)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Black"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 170, 127);\n"
"")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(0)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 2)


        self.gridLayout_4.addWidget(self.frame_5, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked["bool"].connect(MainWindow.close)
        self.pushButton.pressed.connect(MainWindow.hide)
        self.pushButton.released.connect(MainWindow.show)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.adm_login_btn.setText(QCoreApplication.translate("MainWindow", u"LOGIN/MASUK", None))
        self.adm_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Input Username!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.show_btn.setText("")
        self.adm_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Input Password!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ADMIN LOGIN", None))
    # retranslateUi

