import json
import logging
import os
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QMovie, QIcon, QAction, QFont, QCursor
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit, QMenu, QListWidgetItem, QGridLayout, QLabel, QFrame, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy, QPushButton, QFileDialog
from matplotlib.backend_bases import CloseEvent
from rich.console import Console
from views.admin_login import admin_login
from views.user_login import user_login
from views.user_main import user_MainWindow
from views.user_profile import Ui_profile
from views.user_settings import Ui_settings
from views.buy_item import BuyWindow
from views.user_chart import ChartWindow
import time
import threading
import random
import shutil

from controller.app_controls import (
    register_user,
    login_user,
    login_admin,
    get_user_data,
    send_verification_code,
    generate_verification_code,
    change_profile,
    change_email,
    change_password,
    change_settings,
    get_produc_by_id,
    generate_random_id,
    discount_price,
    get_item_by_category,
    get_item_by_name,
    list_item_by_higer_discount,
    list_item_by_lower_price,
    list_item_by_higher_price,
    get_last_10_items,
    add_comment,
    get_item_from_price_range,
    get_20_random_items,
    get_8_raandom_discount_items,
    get_all_item_in_random_order,
    add_to_cart,
    add_to_order,
    deduct_money,
    change_user_image,
    copy_and_rename_image,
    get_user_chart,
    remove_from_cart
)

console = Console()


class UsrLoginWindow(QMainWindow):
    logger_file_path = "./.logger"

    def __init__(self):
        super().__init__()
        self.ui = user_login()
        self.ui.setupUi(self)
        self.setWindowTitle("User Login")  # Set the window title
        icon_path = os.path.abspath("./views/res/images/logo.jpeg")
        self.setWindowIcon(QIcon(icon_path))  # Set the window icon
        self.main = None
        self.setup_connections()
        self.auto_login()
        self.code = generate_verification_code()
        self.ui.reg_password.setMaxLength(32767)

    def setup_connections(self):
        self.ui.login_btn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login))
        self.ui.regis_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.regis))
        self.ui.login_btn.clicked.connect(self.login)
        self.ui.reg_btn.clicked.connect(self.register)
        self.ui.show_btn.clicked.connect(self.toggle_password_visibility)
        self.ui.show_btn_2.clicked.connect(self.toggle_reg_password_visibility)
        self.ui.send_code.clicked.connect(lambda: self.send_code())

    def auto_login(self):
        if os.path.isfile(self.logger_file_path):
            with open(self.logger_file_path, "r") as logger_file:
                logger_data = json.load(logger_file)
                email = logger_data.get("email")
                password = logger_data.get("password")
                if self.attempt_login_auto(email, password):
                    self.switch_to_main_window()
        else:
            console.log("No logger file found!")
            self.show()

    def attempt_login_auto(self, email, password):
        response = login_user(email=email, password=password)
        if response["status"]:
            console.log("User successfully logged in!")
            return True
        else:
            self.show()
            return False

    def attempt_login(self, email, password):
        if self.check_code() == True:
            response = login_user(email=email, password=password)
            if response["status"]:
                console.log("User successfully logged in!")
                return True
            return False

    def switch_to_main_window(self):
        self.main = UserMainWindow()
        self.main.show()
        self.close()

    def login(self):
        email = self.ui.emails.text().strip()
        password = self.ui.password.text().strip()
        if self.attempt_login(email, password):
            self.clear_login_fields()
            self.show_message("Login Successful", "You have been logged in successfully.")
            self.switch_to_main_window()
        else:
            self.clear_login_fields()
            self.show_message("Login Failed", "The email or password you entered is incorrect.")

    def register(self):
        email = self.ui.reg_email.text().strip()
        username = self.ui.reg_username.text().strip()
        password = self.ui.reg_password.text().strip()
        response = register_user(email=email, username=username, password=password)
        if response["status"]:
            self.clear_registration_fields()
            self.ui.emails.setText(email)
            self.ui.password.setText(password)
            self.ui.stackedWidget.setCurrentWidget(self.ui.login)
            self.show_message("Registration Successful", "Your account has been created successfully.")
        else:
            self.clear_registration_fields()
            self.show_message("Registration Failed", response["message"])

    def clear_login_fields(self):
        self.ui.emails.clear()
        self.ui.password.clear()

    def clear_registration_fields(self):
        self.ui.reg_email.clear()
        self.ui.reg_username.clear()
        self.ui.reg_password.clear()

    def show_message(self, title, message):
        QMessageBox.information(self, title, message)

    def toggle_password_visibility(self):
        self.toggle_visibility(self.ui.password, self.ui.show_btn)

    def toggle_reg_password_visibility(self):
        self.toggle_visibility(self.ui.reg_password, self.ui.show_btn_2)

    def toggle_visibility(self, line_edit, toggle_button):
        line_edit.setEchoMode(QLineEdit.EchoMode.Normal if toggle_button.isChecked() else QLineEdit.EchoMode.Password)
    
    def send_code(self):
        email = self.ui.emails.text()
        data = send_verification_code(email=email, verification_code=self.code, pesan="Kami telah menerima permintaan untuk memverifikasi email Anda.\nJangan berikan kode verifikasi ini kepada siapapun!")
        message = data["message"]
        if data["status"] == True:
            QMessageBox.information(self, "Verification Code", message)
        else:
            QMessageBox.information(self, "Verification Code", message)
            
    
    def check_code(self):
        if self.ui.verification.text() == self.code:
            return True
        else:
            return False


class UserMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = user_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("User Main Window")  # Set the window title
        icon_path = os.path.abspath("./views/res/images/logo.jpeg")
        self.setWindowIcon(QIcon(icon_path))
        self.ui.big_sidebar.hide()
        self.show()
        gif_file = "./views/res/animated/wave_hand.gif"
        gif_file_path = os.path.abspath(gif_file)
        movie = QMovie(gif_file_path)
        movie.setScaledSize(self.ui.wave_anim.size())
        self.ui.wave_anim.setMovie(movie)
        movie.start()
        with open("./.logger", "r") as logger_file:
            logger_data = json.load(logger_file)
            email = logger_data.get("email")
            password = logger_data.get("password")
            user_data = get_user_data(email=email, password=password)
            self.ui.welcome_txt.setText("Hi, " + user_data["username"])
            self.profile_picture = user_data['profile']['profile_picture']
        self.ui.mini_btn_home.clicked.connect(lambda: self.toggle_mini_buttons(self.ui.mini_btn_home))
        self.ui.mini_btn_search.clicked.connect(lambda: self.toggle_mini_buttons(self.ui.mini_btn_search))
        self.ui.mini_btn_discount.clicked.connect(lambda: self.toggle_mini_buttons(self.ui.mini_btn_discount))
        self.ui.mini_btn_new.clicked.connect(lambda: self.toggle_mini_buttons(self.ui.mini_btn_new))
        self.ui.mini_btn_order.clicked.connect(lambda: self.toggle_mini_buttons(self.ui.mini_btn_order))
        self.ui.mini_btn_order.clicked.connect(lambda: self.show_custom_context_menu(self.ui.mini_btn_order, ["Being Packed", "Delivered", "Completed", "Cancelled"]))
        self.ui.mini_btn_settings.clicked.connect(lambda: self.toggle_mini_buttons(self.ui.mini_btn_settings))
        self.ui.big_btn_home.clicked.connect(lambda: self.toggle_big_buttons(self.ui.big_btn_home))
        self.ui.big_btn_search.clicked.connect(lambda: self.toggle_big_buttons(self.ui.big_btn_search))
        self.ui.big_btn_discount.clicked.connect(lambda: self.toggle_big_buttons(self.ui.big_btn_discount))
        self.ui.big_btn_new.clicked.connect(lambda: self.toggle_big_buttons(self.ui.big_btn_new))
        self.ui.big_btn_order.clicked.connect(lambda: self.toggle_big_buttons(self.ui.big_btn_order))
        self.ui.big_btn_order.clicked.connect(lambda: self.show_custom_context_menu(self.ui.big_btn_order, ["Being Packed", "Delivered", "Completed", "Cancelled"]))
        self.ui.big_btn_settings.clicked.connect(lambda: self.toggle_big_buttons(self.ui.big_btn_settings))
        self.ui.big_btn_logout.clicked.connect(self.logout)
        self.ui.mini_btn_logout.clicked.connect(self.logout)
        self.ui.profiile.clicked.connect(lambda: self.show_custom_context_menu(self.ui.profiile, ["Profile", "Settings", "Logout"]))
        self.ui.mini_btn_settings.clicked.connect(self.show_settings)
        self.ui.chart.clicked.connect(lambda: self.show_chart())
        # Start the login status checking in a separate thread
        self.login_status_thread = threading.Thread(target=self.check_login_status)
        self.login_status_thread.start()
        self.set_discount_item()
        self.set_recomended_item()
        self.setup_connections()
        self.new_arrivals()
        self.search()
    
    def show_chart(self):
        self.chart = UserCharts()
        self.chart.show()

    def new_arrivals(self):
        items = get_last_10_items()
        for item in items:
            self.list_item = QListWidgetItem()
            self.list_item.setSizeHint(QSize(0, 150))

            self.centralwidget = QWidget()
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
            self.item_images.setStyleSheet(f"border-image: url({item['image_path']});")

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
            self.the_category.setText(item["category"])

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
            self.desc.setText(item["description"])

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
            self.names_itm.setText(item["name"])

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
            if item["discount"] == 0:
                self.itm_price.setText(f"Rp {format(item['price'], ',')}")
            else:
                self.itm_price.setText(f"Rp {format(discount_price(price=item['price'], discount=item['discount']), ',')}")

            self.gridLayout_2.addWidget(self.itm_price, 0, 1, 1, 1)

            self.discount_itm = QLabel(self.frame_2)
            self.discount_itm.setObjectName(u"discount_itm")
            self.discount_itm.setMaximumSize(QSize(200, 16777215))
            font3 = QFont()
            font3.setItalic(True)
            font3.setStrikeOut(True)
            self.discount_itm.setFont(font3)
            self.discount_itm.setStyleSheet(u"color: rgb(255, 0, 0);")
            if item["discount"] == 0:
                self.discount_itm.hide()
            else:
                self.discount_itm.setText(f"Rp {format(item['price'], ',')}")

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
            self.Buy_button.setText("BUY")
            self.Buy_button.clicked.connect(lambda _, item=item: BuyItem(item=item))

            self.horizontalLayout.addWidget(self.Buy_button)
            
            # Set the item widget for the list item
            self.ui.listWidget_3.addItem(self.list_item)
            self.ui.listWidget_3.setItemWidget(self.list_item, self.centralwidget)


    def search(self):
        get_item = get_all_item_in_random_order()
        get_discount_item = list_item_by_higer_discount()
        def search_item():
            self.ui.listWidget.clear()
            get_item = get_all_item_in_random_order()
            if self.ui.lineEdit_3.text() == "":
                QMessageBox.warning(self, "Warning", "Please enter a search query.")
            else:
                get_item = get_item_by_name(produc_list=get_item, name=self.ui.lineEdit_3.text())

            for item in get_item:
                self.list_item = QListWidgetItem()
                self.list_item.setSizeHint(QSize(0, 150))

                self.centralwidget = QWidget()
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
                self.item_images.setStyleSheet(f"border-image: url({item['image_path']});")

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
                self.the_category.setText(item["category"])

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
                self.desc.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                self.desc.setText(item["description"])

                self.gridLayout.addWidget(self.desc, 1, 0, 1, 4)

                self.names_itm = QLabel(self.frame)
                self.names_itm.setObjectName(u"names_itm")
                self.names_itm.setMaximumSize(QSize(16777215, 20))
                font2 = QFont()
                font2.setFamilies([u"Segoe UI Black"])
                font2.setPointSize(10)
                font2.setBold(True)
                self.names_itm.setFont(font2)
                self.names_itm.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                self.names_itm.setText(item["name"])

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
                if item["discount"] == 0:
                    self.itm_price.setText(f"Rp {format(item['price'], ',')}")
                else:
                    self.itm_price.setText(f"Rp {format(discount_price(price=item['price'], discount=item['discount']), ',')}")

                self.gridLayout_2.addWidget(self.itm_price, 0, 1, 1, 1)

                self.discount_itm = QLabel(self.frame_2)
                self.discount_itm.setObjectName(u"discount_itm")
                self.discount_itm.setMaximumSize(QSize(200, 16777215))
                font3 = QFont()
                font3.setItalic(True)
                font3.setStrikeOut(True)
                self.discount_itm.setFont(font3)
                self.discount_itm.setStyleSheet(u"color: rgb(255, 0, 0);")
                if item["discount"] == 0:
                    self.discount_itm.hide()
                else:
                    self.discount_itm.setText(f"Rp {format(item['price'], ',')}")

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
                self.Buy_button.setText("BUY")
                self.Buy_button.clicked.connect(lambda _, item=item: BuyItem(item=item))

                self.horizontalLayout.addWidget(self.Buy_button)
                
                # Set the item widget for the list item
                self.ui.listWidget.addItem(self.list_item)
                self.ui.listWidget.setItemWidget(self.list_item, self.centralwidget)

        def search_discount():
            self.ui.listWidget_2.clear()
            get_discount_item = list_item_by_higer_discount()
            if self.ui.lineEdit_6.text() == "":
                QMessageBox.warning(self, "Warning", "Please enter a search query.")
            else:
                get_discount_item = get_item_by_name(produc_list=get_discount_item, name=self.ui.lineEdit_6.text())

            for item in get_discount_item:
                self.list_item = QListWidgetItem()
                self.list_item.setSizeHint(QSize(0, 150))

                self.centralwidget = QWidget()
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
                self.item_images.setStyleSheet(f"border-image: url({item['image_path']});")

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
                self.the_category.setText(item["category"])

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
                self.desc.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                self.desc.setText(item["description"])

                self.gridLayout.addWidget(self.desc, 1, 0, 1, 4)

                self.names_itm = QLabel(self.frame)
                self.names_itm.setObjectName(u"names_itm")
                self.names_itm.setMaximumSize(QSize(16777215, 20))
                font2 = QFont()
                font2.setFamilies([u"Segoe UI Black"])
                font2.setPointSize(10)
                font2.setBold(True)
                self.names_itm.setFont(font2)
                self.names_itm.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                self.names_itm.setText(item["name"])

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
                if item["discount"] == 0:
                    self.itm_price.setText(f"Rp {format(item['price'], ',')}")
                else:
                    self.itm_price.setText(f"Rp {format(discount_price(price=item['price'], discount=item['discount']), ',')}")

                self.gridLayout_2.addWidget(self.itm_price, 0, 1, 1, 1)

                self.discount_itm = QLabel(self.frame_2)
                self.discount_itm.setObjectName(u"discount_itm")
                self.discount_itm.setMaximumSize(QSize(200, 16777215))
                font3 = QFont()
                font3.setItalic(True)
                font3.setStrikeOut(True)
                self.discount_itm.setFont(font3)
                self.discount_itm.setStyleSheet(u"color: rgb(255, 0, 0);")
                if item["discount"] == 0:
                    self.discount_itm.hide()
                else:
                    self.discount_itm.setText(f"Rp {format(item['price'], ',')}")

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
                self.Buy_button.setText("BUY")
                self.Buy_button.clicked.connect(lambda _, item=item: BuyItem(item=item))

                self.horizontalLayout.addWidget(self.Buy_button)
                
                # Set the item widget for the list item
                self.ui.listWidget_2.addItem(self.list_item)
                self.ui.listWidget_2.setItemWidget(self.list_item, self.centralwidget)

        self.ui.pushButton.clicked.connect(search_item)
        self.ui.pushButton_2.clicked.connect(search_discount)

        for item in get_item:
            self.list_item = QListWidgetItem()
            self.list_item.setSizeHint(QSize(0, 150))

            self.centralwidget = QWidget()
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
            self.item_images.setStyleSheet(f"border-image: url({item['image_path']});")

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
            self.the_category.setText(item["category"])

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
            self.desc.setText(item["description"])

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
            self.names_itm.setText(item["name"])

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
            if item["discount"] == 0:
                self.itm_price.setText(f"Rp {format(item['price'], ',')}")
            else:
                self.itm_price.setText(f"Rp {format(discount_price(price=item['price'], discount=item['discount']), ',')}")

            self.gridLayout_2.addWidget(self.itm_price, 0, 1, 1, 1)

            self.discount_itm = QLabel(self.frame_2)
            self.discount_itm.setObjectName(u"discount_itm")
            self.discount_itm.setMaximumSize(QSize(200, 16777215))
            font3 = QFont()
            font3.setItalic(True)
            font3.setStrikeOut(True)
            self.discount_itm.setFont(font3)
            self.discount_itm.setStyleSheet(u"color: rgb(255, 0, 0);")
            if item["discount"] == 0:
                self.discount_itm.hide()
            else:
                self.discount_itm.setText(f"Rp {format(item['price'], ',')}")

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
            self.Buy_button.setText("BUY")
            self.Buy_button.clicked.connect(lambda _, item=item: BuyItem(item=item))

            self.horizontalLayout.addWidget(self.Buy_button)
            
            # Set the item widget for the list item
            self.ui.listWidget.addItem(self.list_item)
            self.ui.listWidget.setItemWidget(self.list_item, self.centralwidget) 

        for item in get_discount_item:
            self.list_item = QListWidgetItem()
            self.list_item.setSizeHint(QSize(0, 150))

            self.centralwidget = QWidget()
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
            self.item_images.setStyleSheet(f"border-image: url({item['image_path']});")

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
            self.the_category.setText(item["category"])

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
            self.desc.setText(item["description"])

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
            self.names_itm.setText(item["name"])

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
            if item["discount"] == 0:
                self.itm_price.setText(f"Rp {format(item['price'], ',')}")
            else:
                self.itm_price.setText(f"Rp {format(discount_price(price=item['price'], discount=item['discount']), ',')}")

            self.gridLayout_2.addWidget(self.itm_price, 0, 1, 1, 1)

            self.discount_itm = QLabel(self.frame_2)
            self.discount_itm.setObjectName(u"discount_itm")
            self.discount_itm.setMaximumSize(QSize(200, 16777215))
            font3 = QFont()
            font3.setItalic(True)
            font3.setStrikeOut(True)
            self.discount_itm.setFont(font3)
            self.discount_itm.setStyleSheet(u"color: rgb(255, 0, 0);")
            if item["discount"] == 0:
                self.discount_itm.hide()
            else:
                self.discount_itm.setText(f"Rp {format(item['price'], ',')}")

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
            self.Buy_button.setText("BUY")
            self.Buy_button.clicked.connect(lambda _, item=item: BuyItem(item=item))

            self.horizontalLayout.addWidget(self.Buy_button)
            
            # Set the item widget for the list item
            self.ui.listWidget_2.addItem(self.list_item)
            self.ui.listWidget_2.setItemWidget(self.list_item, self.centralwidget) 

    def setup_connections(self):
        self.ui.mini_btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.mini_btn_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search))
        self.ui.mini_btn_discount.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.discount))
        self.ui.mini_btn_new.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.nrw_arrivals))
        self.ui.big_btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.big_btn_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search))
        self.ui.big_btn_discount.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.discount))
        self.ui.big_btn_new.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.nrw_arrivals))
            
    
    def check_login_status(self):
        while self.isVisible():  # Check if the UserMainWindow is still visible
            console.log("Checking login status...")
            with open("./.logger", "r") as logger_file:
                logger_data = json.load(logger_file)
                email = logger_data.get("email")
                password = logger_data.get("password")
                status = login_user(email=email, password=password)
                self.handle_login_status(status["status"])
                user_money = get_user_data(email=email, password=password)["money"]
                self.ui.money.setText(f"Rp {format(user_money, ',')}")
                if os.path.isfile(self.profile_picture):
                    self.ui.profile_img.setStyleSheet(
                        "border-color: rgb(0, 0, 0); border-style: outset; border-width: 1px; border-radius: 20px; border-image: url("
                        + self.profile_picture
                        + ");"
                    )
                else:
                    console.log(f"Could not create pixmap from {self.profile_picture}")
            time.sleep(5)
    
    def handle_login_status(self, login_status):
        QtCore.QMetaObject.invokeMethod(self, "update_login_status", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(bool, login_status))
    
    @QtCore.Slot(bool)
    def update_login_status(self, login_status):
        console.log(f"Login status: {login_status}")
        if not login_status:
            QtWidgets.QMessageBox.warning(self, "Logout", "Your account has been logged out due to inactivity!")
            console.log("User logged out successfully!")
            try:
                os.remove("./.logger") 
            except OSError as e:
                logging.error(f"Error removing '.logger' file: {e}")
            self.close()
            self.login_window = UsrLoginWindow()
            self.login_window.show()

    def logout(self):
        # Function to perform logout
        reply = QMessageBox.question(
            self,
            "Logout",
            "Are you sure you want to logout?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            console.log("User logged out successfully!")
            try:
                os.remove("./.logger") 
            except OSError as e:
                logging.error(f"Error removing '.logger' file: {e}")
            self.close()
            login_window = UsrLoginWindow()
            login_window.show()
        else:
            console.log("User cancelled logout!")

    def set_discount_item(self):
        # Function to set the discount items
        discount_items = get_8_raandom_discount_items()

        # Set discount item image
        self.ui.image.setStyleSheet(f"border-width: 0px; border-image: url({discount_items[0]["image_path"]});")
        self.ui.image_4.setStyleSheet(f"border-width: 0px; border-image: url({discount_items[1]["image_path"]});")
        self.ui.image_5.setStyleSheet(f"border-width: 0px; border-image: url({discount_items[2]["image_path"]});")
        self.ui.image_6.setStyleSheet(f"border-width: 0px; border-image: url({discount_items[3]["image_path"]});")
        self.ui.image_7.setStyleSheet(f"border-width: 0px; border-image: url({discount_items[4]["image_path"]});")
        self.ui.image_8.setStyleSheet(f"border-width: 0px; border-image: url({discount_items[5]["image_path"]});")
        self.ui.image_9.setStyleSheet(f"border-width: 0px; border-image: url({discount_items[6]["image_path"]});")
        self.ui.image_10.setStyleSheet(f"border-width: 0px; border-image: url({discount_items[7]["image_path"]});")

        # Set discount item name
        self.ui.produc_name.setText(discount_items[0]["name"])
        self.ui.produc_name_4.setText(discount_items[1]["name"])
        self.ui.produc_name_5.setText(discount_items[2]["name"])
        self.ui.produc_name_6.setText(discount_items[3]["name"])
        self.ui.produc_name_7.setText(discount_items[4]["name"])
        self.ui.produc_name_8.setText(discount_items[5]["name"])
        self.ui.produc_name_9.setText(discount_items[6]["name"])
        self.ui.produc_name_10.setText(discount_items[7]["name"])

        # Set discount item price
        self.ui.disc_label.setText(f"Rp {format(discount_items[0]['price'], ',')}")
        self.ui.disc_label_4.setText(f"Rp {format(discount_items[1]['price'], ',')}")
        self.ui.disc_label_5.setText(f"Rp {format(discount_items[2]['price'], ',')}")
        self.ui.disc_label_6.setText(f"Rp {format(discount_items[3]['price'], ',')}")
        self.ui.disc_label_7.setText(f"Rp {format(discount_items[4]['price'], ',')}")
        self.ui.disc_label_8.setText(f"Rp {format(discount_items[5]['price'], ',')}")
        self.ui.disc_label_9.setText(f"Rp {format(discount_items[6]['price'], ',')}")
        self.ui.disc_label_10.setText(f"Rp {format(discount_items[7]['price'], ',')}")

        # Set discount item discount
        self.ui.price.setText(f"Rp {format(discount_price(price=discount_items[0]["price"], discount=discount_items[0]["discount"]), ',')}")
        self.ui.price_4.setText(f"Rp {format(discount_price(price=discount_items[1]["price"], discount=discount_items[1]["discount"]), ',')}")
        self.ui.price_5.setText(f"Rp {format(discount_price(price=discount_items[2]["price"], discount=discount_items[2]["discount"]), ',')}")
        self.ui.price_6.setText(f"Rp {format(discount_price(price=discount_items[3]["price"], discount=discount_items[3]["discount"]), ',')}")
        self.ui.price_7.setText(f"Rp {format(discount_price(price=discount_items[4]["price"], discount=discount_items[4]["discount"]), ',')}")
        self.ui.price_8.setText(f"Rp {format(discount_price(price=discount_items[5]["price"], discount=discount_items[5]["discount"]), ',')}")
        self.ui.price_9.setText(f"Rp {format(discount_price(price=discount_items[6]["price"], discount=discount_items[6]["discount"]), ',')}")
        self.ui.price_10.setText(f"Rp {format(discount_price(price=discount_items[7]["price"], discount=discount_items[7]["discount"]), ',')}")

        # Set when buy button clicked
        self.ui.buy_btn.clicked.connect(lambda: BuyItem(item=discount_items[0]))
        self.ui.buy_btn_4.clicked.connect(lambda: BuyItem(item=discount_items[1]))
        self.ui.buy_btn_5.clicked.connect(lambda: BuyItem(item=discount_items[2]))
        self.ui.buy_btn_6.clicked.connect(lambda: BuyItem(item=discount_items[3]))
        self.ui.buy_btn_7.clicked.connect(lambda: BuyItem(item=discount_items[4]))
        self.ui.buy_btn_8.clicked.connect(lambda: BuyItem(item=discount_items[5]))
        self.ui.buy_btn_9.clicked.connect(lambda: BuyItem(item=discount_items[6]))
        self.ui.buy_btn_10.clicked.connect(lambda: BuyItem(item=discount_items[7]))

    def set_recomended_item(self):
        # Function to set the recommended items
        recomended_items = get_20_random_items()

        # Set recommended item image
        self.ui.image_produc.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[0]['image_path']});")
        self.ui.image_produc_26.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[1]['image_path']});")
        self.ui.image_produc_27.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[2]['image_path']});")
        self.ui.image_produc_28.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[3]['image_path']});")
        self.ui.image_produc_29.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[4]['image_path']});")
        self.ui.image_produc_30.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[5]['image_path']});")
        self.ui.image_produc_31.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[6]['image_path']});")
        self.ui.image_produc_32.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[7]['image_path']});")
        self.ui.image_produc_33.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[8]['image_path']});")
        self.ui.image_produc_34.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[9]['image_path']});")
        self.ui.image_produc_35.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[10]['image_path']});")
        self.ui.image_produc_36.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[11]['image_path']});")
        self.ui.image_produc_37.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[12]['image_path']});")
        self.ui.image_produc_38.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[13]['image_path']});")
        self.ui.image_produc_39.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[14]['image_path']});")
        self.ui.image_produc_40.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[15]['image_path']});")
        self.ui.image_produc_41.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[16]['image_path']});")
        self.ui.image_produc_42.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[17]['image_path']});")
        self.ui.image_produc_43.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[18]['image_path']});")
        self.ui.image_produc_44.setStyleSheet(f"border-width: 0px; border-image: url({recomended_items[19]['image_path']});")

        # Set recommended item name
        self.ui.produk.setText(recomended_items[0]['name'])
        self.ui.produk_26.setText(recomended_items[1]['name'])
        self.ui.produk_27.setText(recomended_items[2]['name'])
        self.ui.produk_28.setText(recomended_items[3]['name'])
        self.ui.produk_29.setText(recomended_items[4]['name'])
        self.ui.produk_30.setText(recomended_items[5]['name'])
        self.ui.produk_31.setText(recomended_items[6]['name'])
        self.ui.produk_32.setText(recomended_items[7]['name'])
        self.ui.produk_33.setText(recomended_items[8]['name'])
        self.ui.produk_34.setText(recomended_items[9]['name'])
        self.ui.produk_35.setText(recomended_items[10]['name'])
        self.ui.produk_36.setText(recomended_items[11]['name'])
        self.ui.produk_37.setText(recomended_items[12]['name'])
        self.ui.produk_38.setText(recomended_items[13]['name'])
        self.ui.produk_39.setText(recomended_items[14]['name'])
        self.ui.produk_40.setText(recomended_items[15]['name'])
        self.ui.produk_41.setText(recomended_items[16]['name'])
        self.ui.produk_42.setText(recomended_items[17]['name'])
        self.ui.produk_43.setText(recomended_items[18]['name'])
        self.ui.produk_44.setText(recomended_items[19]['name'])

        # Set recommended item price
        self.ui.harga.setText(f"Rp {format(discount_price(price=recomended_items[0]["price"], discount=recomended_items[0]["discount"]), ',')}")
        self.ui.harga_26.setText(f"Rp {format(discount_price(price=recomended_items[1]["price"], discount=recomended_items[1]["discount"]), ',')}")
        self.ui.harga_27.setText(f"Rp {format(discount_price(price=recomended_items[2]["price"], discount=recomended_items[2]["discount"]), ',')}")
        self.ui.harga_28.setText(f"Rp {format(discount_price(price=recomended_items[3]["price"], discount=recomended_items[3]["discount"]), ',')}")
        self.ui.harga_29.setText(f"Rp {format(discount_price(price=recomended_items[4]["price"], discount=recomended_items[4]["discount"]), ',')}")
        self.ui.harga_30.setText(f"Rp {format(discount_price(price=recomended_items[5]["price"], discount=recomended_items[5]["discount"]), ',')}")
        self.ui.harga_31.setText(f"Rp {format(discount_price(price=recomended_items[6]["price"], discount=recomended_items[6]["discount"]), ',')}")
        self.ui.harga_32.setText(f"Rp {format(discount_price(price=recomended_items[7]["price"], discount=recomended_items[7]["discount"]), ',')}")
        self.ui.harga_33.setText(f"Rp {format(discount_price(price=recomended_items[8]["price"], discount=recomended_items[8]["discount"]), ',')}")
        self.ui.harga_34.setText(f"Rp {format(discount_price(price=recomended_items[9]["price"], discount=recomended_items[9]["discount"]), ',')}")
        self.ui.harga_35.setText(f"Rp {format(discount_price(price=recomended_items[10]["price"], discount=recomended_items[10]["discount"]), ',')}")
        self.ui.harga_36.setText(f"Rp {format(discount_price(price=recomended_items[11]["price"], discount=recomended_items[11]["discount"]), ',')}")
        self.ui.harga_37.setText(f"Rp {format(discount_price(price=recomended_items[12]["price"], discount=recomended_items[12]["discount"]), ',')}")
        self.ui.harga_38.setText(f"Rp {format(discount_price(price=recomended_items[13]["price"], discount=recomended_items[13]["discount"]), ',')}")
        self.ui.harga_39.setText(f"Rp {format(discount_price(price=recomended_items[14]["price"], discount=recomended_items[14]["discount"]), ',')}")
        self.ui.harga_40.setText(f"Rp {format(discount_price(price=recomended_items[15]["price"], discount=recomended_items[15]["discount"]), ',')}")
        self.ui.harga_41.setText(f"Rp {format(discount_price(price=recomended_items[16]["price"], discount=recomended_items[16]["discount"]), ',')}")
        self.ui.harga_42.setText(f"Rp {format(discount_price(price=recomended_items[17]["price"], discount=recomended_items[17]["discount"]), ',')}")
        self.ui.harga_43.setText(f"Rp {format(discount_price(price=recomended_items[18]["price"], discount=recomended_items[18]["discount"]), ',')}")
        self.ui.harga_44.setText(f"Rp {format(discount_price(price=recomended_items[19]["price"], discount=recomended_items[19]["discount"]), ',')}")

        # Set recommended item discount
        if recomended_items[0]["discount"] != 0:
            self.ui.diskon.setText(f"{recomended_items[0]['discount']}%")
        else:
            self.ui.diskon.hide()

        if recomended_items[1]["discount"] != 0:
            self.ui.diskon_26.setText(f"{recomended_items[1]['discount']}%")
        else:
            self.ui.diskon_26.hide()

        if recomended_items[2]["discount"] != 0:
            self.ui.diskon_27.setText(f"{recomended_items[2]['discount']}%")
        else:
            self.ui.diskon_27.hide()

        if recomended_items[3]["discount"] != 0:
            self.ui.diskon_28.setText(f"{recomended_items[3]['discount']}%")
        else:
            self.ui.diskon_28.hide()

        if recomended_items[4]["discount"] != 0:
            self.ui.diskon_29.setText(f"{recomended_items[4]['discount']}%")
        else:
            self.ui.diskon_29.hide()

        if recomended_items[5]["discount"] != 0:
            self.ui.diskon_30.setText(f"{recomended_items[5]['discount']}%")
        else:
            self.ui.diskon_30.hide()

        if recomended_items[6]["discount"] != 0:
            self.ui.diskon_31.setText(f"{recomended_items[6]['discount']}%")
        else:
            self.ui.diskon_31.hide()

        if recomended_items[7]["discount"] != 0:
            self.ui.diskon_32.setText(f"{recomended_items[7]['discount']}%")
        else:
            self.ui.diskon_32.hide()

        if recomended_items[8]["discount"] != 0:
            self.ui.diskon_33.setText(f"{recomended_items[8]['discount']}%")
        else:
            self.ui.diskon_33.hide()

        if recomended_items[9]["discount"] != 0:
            self.ui.diskon_34.setText(f"{recomended_items[9]['discount']}%")
        else:
            self.ui.diskon_34.hide()

        if recomended_items[10]["discount"] != 0:
            self.ui.diskon_35.setText(f"{recomended_items[10]['discount']}%")
        else:
            self.ui.diskon_35.hide()

        if recomended_items[11]["discount"] != 0:
            self.ui.diskon_36.setText(f"{recomended_items[11]['discount']}%")
        else:
            self.ui.diskon_36.hide()

        if recomended_items[12]["discount"] != 0:
            self.ui.diskon_37.setText(f"{recomended_items[12]['discount']}%")
        else:
            self.ui.diskon_37.hide()

        if recomended_items[13]["discount"] != 0:
            self.ui.diskon_38.setText(f"{recomended_items[13]['discount']}%")
        else:
            self.ui.diskon_38.hide()

        if recomended_items[14]["discount"] != 0:
            self.ui.diskon_39.setText(f"{recomended_items[14]['discount']}%")
        else:
            self.ui.diskon_39.hide()

        if recomended_items[15]["discount"] != 0:
            self.ui.diskon_40.setText(f"{recomended_items[15]['discount']}%")
        else:
            self.ui.diskon_40.hide()

        if recomended_items[16]["discount"] != 0:
            self.ui.diskon_41.setText(f"{recomended_items[16]['discount']}%")
        else:
            self.ui.diskon_41.hide()

        if recomended_items[17]["discount"] != 0:
            self.ui.diskon_42.setText(f"{recomended_items[17]['discount']}%")
        else:
            self.ui.diskon_42.hide()

        if recomended_items[18]["discount"] != 0:
            self.ui.diskon_43.setText(f"{recomended_items[18]['discount']}%")
        else:
            self.ui.diskon_43.hide()

        if recomended_items[19]["discount"] != 0:
            self.ui.diskon_44.setText(f"{recomended_items[19]['discount']}%")
        else:
            self.ui.diskon_44.hide()

        # Set when buy button clicked
        self.ui.tombol.clicked.connect(lambda: BuyItem(item=recomended_items[0]))
        self.ui.tombol_26.clicked.connect(lambda: BuyItem(item=recomended_items[1]))
        self.ui.tombol_27.clicked.connect(lambda: BuyItem(item=recomended_items[2]))
        self.ui.tombol_28.clicked.connect(lambda: BuyItem(item=recomended_items[3]))
        self.ui.tombol_29.clicked.connect(lambda: BuyItem(item=recomended_items[4]))
        self.ui.tombol_30.clicked.connect(lambda: BuyItem(item=recomended_items[5]))
        self.ui.tombol_31.clicked.connect(lambda: BuyItem(item=recomended_items[6]))
        self.ui.tombol_32.clicked.connect(lambda: BuyItem(item=recomended_items[7]))
        self.ui.tombol_33.clicked.connect(lambda: BuyItem(item=recomended_items[8]))
        self.ui.tombol_34.clicked.connect(lambda: BuyItem(item=recomended_items[9]))
        self.ui.tombol_35.clicked.connect(lambda: BuyItem(item=recomended_items[10]))
        self.ui.tombol_36.clicked.connect(lambda: BuyItem(item=recomended_items[11]))
        self.ui.tombol_37.clicked.connect(lambda: BuyItem(item=recomended_items[12]))
        self.ui.tombol_38.clicked.connect(lambda: BuyItem(item=recomended_items[13]))
        self.ui.tombol_39.clicked.connect(lambda: BuyItem(item=recomended_items[14]))
        self.ui.tombol_40.clicked.connect(lambda: BuyItem(item=recomended_items[15]))
        self.ui.tombol_41.clicked.connect(lambda: BuyItem(item=recomended_items[16]))
        self.ui.tombol_42.clicked.connect(lambda: BuyItem(item=recomended_items[17]))
        self.ui.tombol_43.clicked.connect(lambda: BuyItem(item=recomended_items[18]))
        self.ui.tombol_44.clicked.connect(lambda: BuyItem(item=recomended_items[19]))

    def closeEvent(self, event: CloseEvent):
        console.log("User main window closed!")

    def toggle_big_buttons(self, clicked_button):
        # Fungsi untuk mengatur tombol besar yang aktif dan non-aktif
        big_buttons = [
            self.ui.big_btn_home,
            self.ui.big_btn_search,
            self.ui.big_btn_discount,
            self.ui.big_btn_new,
            self.ui.big_btn_order,
            self.ui.big_btn_settings,
        ]
        for button in big_buttons:
            button.setChecked(button == clicked_button)

    def toggle_mini_buttons(self, clicked_button):
        # Fungsi untuk mengatur tombol mini yang aktif dan non-aktif
        mini_buttons = [
            self.ui.mini_btn_home,
            self.ui.mini_btn_search,
            self.ui.mini_btn_discount,
            self.ui.mini_btn_new,
            self.ui.mini_btn_order,
            self.ui.mini_btn_settings,
        ]
        for button in mini_buttons:
            button.setChecked(button == clicked_button)
    
    def show_custom_context_menu(self, button, menu_items):
        context_menu = QMenu(self)
        context_menu.setStyleSheet("""
            QMenu {
            background-color: rgb(239, 40, 91);
            color: black;
            }
            QMenu::item:selected {
            background-color: rgb(255, 255, 255);
            color: rgb(236, 41, 89);
            }
            QMenu::item:hover {
            color: rgb(255, 255, 255);
            border-color: rgb(255, 255, 255);
            border-style: outset;
            border-width: 1px;
            border-right-width: 0px;
            }
        """)
        for item in menu_items:
            action = QAction(item, self)
            context_menu.addAction(action)
            action.triggered.connect(self.handle_menu_action)  # Connect the action to a handler function
        context_menu.exec_(button.mapToGlobal(button.rect().topRight()))

    def handle_menu_action(self):
        action = self.sender()  # Get the action that triggered the event
        if action:
            action_text = action.text()
            {
                "Profile": self.show_profile,
                "Settings": self.show_settings,
                "Logout": self.logout,
                "Being Packed": self.show_being_packed,
                "Delivered": self.show_delivered,
                "Completed": self.show_completed,
                "Cancelled": self.show_cancelled
            }.get(action_text, lambda: None)()

    def show_profile(self):
        # Function to show the profile page
        self.profile = UserProfile()
        self.profile.show()
        console.log("Showing profile page")

    def show_settings(self):
        # Function to show the settings page
        self.settings = UserSettings()
        self.settings.show()
        console.log("Showing settings page")

    def show_being_packed(self):
        # Function to show the orders being packed
        console.log("Showing orders being packed")

    def show_delivered(self):
        # Function to show the delivered orders
        console.log("Showing delivered orders")
    
    def show_completed(self):
        # Function to show the completed orders
        console.log("Showing completed orders")
    
    def show_cancelled(self):
        # Function to show the cancelled orders
        console.log("Showing cancelled orders")

class UserProfile(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_profile()
        self.ui.setupUi(self)
        self.setWindowTitle("User Profile")  # Set the window title
        icon_path = os.path.abspath("./views/res/images/logo.jpeg")
        self.setWindowIcon(QIcon(icon_path))
        self.ui.save_btn.clicked.connect(self.save_profile)
        self.ui.change_btn.clicked.connect(self.change_profile_picture)
        self.ui.btn_nama.clicked.connect(lambda: self.ui.nama.setEnabled(True))
        self.ui.btn_phone.clicked.connect(lambda: self.ui.phone.setEnabled(True))
        self.ui.btn_alamat.clicked.connect(lambda: self.ui.alamat.setEnabled(True))
        self.ui.btn_bio.clicked.connect(lambda: self.ui.bio.setEnabled(True))
        self.ui.btn_gender.clicked.connect(lambda: self.ui.gender.setEnabled(True))
        self.ui.btn_lahir.clicked.connect(lambda: self.ui.lahir.setEnabled(True))
        with open("./.logger", "r") as logger_file:
            logger_data = json.load(logger_file)
            self.email = logger_data.get("email")
            self.password = logger_data.get("password")
        response = get_user_data(email=self.email, password=self.password)
        user_data = response["profile"]
        self.ui.nama.setText(user_data["name"])
        self.ui.bio.setText(user_data["bio"])
        self.ui.alamat.setText(user_data["address"])
        self.ui.phone.setText(user_data["phone"])
        self.ui.gender.setCurrentText(user_data["gender"])
        self.ui.lahir.setText(user_data["birthdate"])
        self.ui.image_profile.setStyleSheet(f"border-image: url({user_data['profile_picture']}); border-color: rgb(0, 0, 0); border-style: outset; border-width: 2px; border-radius: 75px;")
        self.ui.change_btn.clicked.connect(lambda: self.open_image_dialog())
        self.show()

    def open_image_dialog(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_filter = "Image Files (*.jpg *.jpeg *.png)"
            file_path, _ = QFileDialog.getOpenFileName(None, "Select Image", "", file_filter, options=options)
            if file_path:
                # Do something with the selected image file
                copied_image_path = copy_and_rename_image(file_path=file_path, user_id=get_user_data(email=self.email, password=self.password)["user_id"])
                # Example usage:
                response = change_user_image(user_id=get_user_data(email=self.email, password=self.password)["user_id"], image_path=copied_image_path)
                if response["status"]:
                    self.ui.image_profile.setStyleSheet(f"border-image: url({copied_image_path}); border-color: rgb(0, 0, 0); border-style: outset; border-width: 2px; border-radius: 75px;")
                    QMessageBox.information(self, "Profile Picture Changed", response["message"])
                    console.log("Profile picture changed successfully!")
                else:
                    QMessageBox.warning(self, "Profile Picture Change Failed", response["message"])
                    console.error("Profile picture change failed!")
            else:
                print("No image file selected")

    def save_profile(self):
        # Function to save the profile
        name = self.ui.nama.text()
        bio = self.ui.bio.text()
        address = self.ui.alamat.text()
        phone = self.ui.phone.text()
        gender = self.ui.gender.currentText()
        birthdate = self.ui.lahir.text()
        reply = QMessageBox.question(
            self,
            "Profile Saved",
            "Are you done editing your profile?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            # Perform any additional actions if needed
            response = change_profile(self.email, self.password, name, bio, address, phone, gender, birthdate)
            QMessageBox.information(self, "Profile Saved", response["message"])
            console.log("Profile saved successfully!")
            self.close()
            pass

    def change_profile_picture(self):
        # Function to change the profile picture
        console.log("Profile picture changed successfully!")

    def closeEvent(self, event: CloseEvent):
        console.log("User profile window closed!")

class UserSettings(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_settings()
        self.ui.setupUi(self)
        self.setWindowTitle("User Settings")  # Set the window title
        self.setWindowIcon(QIcon(os.path.abspath("./views/res/images/logo.jpeg")))
        
        self.ui.penga_frame.hide()
        self.ui.email_frame.hide()
        self.ui.pass_frame.hide()
        self.ui.matauang.addItems(['IDR','USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD'])
        self.load_logger_data()
        self.assign_button_actions()
        self.cek()
        self.show()

    def load_logger_data(self):
        with open("./.logger", "r") as logger_file:
            logger_data = json.load(logger_file)
        self.email = logger_data.get("email")
        self.password = logger_data.get("password")
        self.code = generate_verification_code()

    def assign_button_actions(self):
        self.ui.btn_email_verif.clicked.connect(self.verify_email)
        self.ui.save_email.clicked.connect(self.save_email)
        self.ui.btn_pass_verif.clicked.connect(self.verify_password)
        self.ui.save_pass.clicked.connect(self.save_password)
        self.ui.pushButton_5.clicked.connect(self.save_settings)

    def verify_password(self):
        pass_now = self.password
        cek_email = get_user_data(email=self.email, password=self.password)
        if pass_now == cek_email["password"]:
            data = send_verification_code(email=self.email, verification_code=self.code, pesan="Kami telah menerima permintaan untuk mengubah password akun Anda. Jangan berikan kode verifikasi ini kepada siapapun!")
            message = data["message"]
            if data["status"] == True:
                QMessageBox.information(self, "Verification Code", message)
            else:
                QMessageBox.information(self, "Verification Code", message)
        else:
            QMessageBox.warning(self, "Verification Code", "Password saat ini tidak sesuai!")

    def save_password(self):
        password = self.ui.passwor_baru.text()
        if self.ui.pass_verifikasi.text() == self.code:
            response = change_password(self.email, self.password, password)
            QMessageBox.information(self, "Password Changed", response["message"])
            console.log("Password changed successfully!")
            self.close()
        else:
            QMessageBox.warning(self, "Verification Code", "Kode verifikasi salah!")

    def verify_email(self):
        email_now = self.ui.email_saatini.text()
        cek_email = get_user_data(email=self.email, password=self.password)
        if email_now == cek_email["email"]:
            data = send_verification_code(email=email_now, verification_code=self.code, pesan="Kami telah menerima permintaan untuk mengubah email Anda.\nJangan berikan kode verifikasi ini kepada siapapun!")
            message = data["message"]
            if data["status"] == True:
                QMessageBox.information(self, "Verification Code", message)
            else:
                QMessageBox.information(self, "Verification Code", message)
        else:
            QMessageBox.warning(self, "Verification Code", "Email saat ini tidak sesuai!")
    
    def save_email(self):
        email_saatini = self.ui.email_saatini.text()
        email_baru = self.ui.email_baru.text()
        if self.ui.email_verifikasi.text() == self.code:
            response = change_email(email_saatini, self.password, email_baru)
            QMessageBox.information(self, "Email Changed", response["message"])
            console.log("Email changed successfully!")
            self.close()
        else:
            QMessageBox.warning(self, "Verification Code", "Kode verifikasi salah!")

    def save_settings(self):
        # Function to save the settings
        if self.ui.aktif.isChecked() == True:
            self.status_notif = True
        if self.ui.nonaktif.isChecked() == True:
            self.status_notif = False
        response = change_settings(email=self.email, password=self.password, notifications=self.status_notif, theme=self.ui.comboBox_2.currentText().lower(), currency=self.ui.matauang.currentText())
        console.log("Settings saved successfully!")
        self.close()

    def cek(self):
        self.user = get_user_data(email=self.email, password=self.password)
        if self.user["settings"]["notifications"] == True:
            self.ui.aktif.setChecked(True)
        else:
            self.ui.nonaktif.setChecked(True)
        self.ui.comboBox_2.setCurrentText(self.user["settings"]["theme"].capitalize())
        self.ui.matauang.setCurrentText(self.user["settings"]["currency"])

    def closeEvent(self, event: CloseEvent):
        console.log("User settings window closed!")

class BuyItem(QMainWindow):
    def __init__(self, item):
        super().__init__()
        self.ui = BuyWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Buy Item")  # Set the window title
        self.setWindowIcon(QIcon(os.path.abspath("./views/res/images/logo.jpeg")))
        self.show()
        gif_file = "./views/res/animated/ok.gif"
        gif_file_path = os.path.abspath(gif_file)
        movie = QMovie(gif_file_path)
        movie.setScaledSize(self.ui.sucess_anim.size())
        self.ui.sucess_anim.setMovie(movie)
        movie.start()
        self.shipping = random.randint(7000, 10000)
        self.admin = random.randint(2000, 5000)
        self.item = item
        self.ui.names.setText(item["name"])
        self.ui.harga_item.setText(f"Rp {format(discount_price(price=item['price'], discount=item['discount']), ',')}")
        if item["discount"] != 0:
            self.ui.presentase_diskon.setText(f"{item['discount']}% OFF")
            self.ui.harga_diskon.setText(f"Rp {format(item['price'], ',')}")
        else:
            self.ui.harga_diskon.hide()
            self.ui.presentase_diskon.hide()
        self.ui.description.setText(item["description"])
        self.ui.category.setText(item["category"])
        self.ui.item_image.setStyleSheet(f"border-image: url({item['image_path']});")
        if len(item["variation"]) == 2:
            self.ui.variaton1.setText(item["variation"][0])
            self.ui.variation2.setText(item["variation"][1])
            self.ui.variation3.hide()
        elif len(item["variation"]) == 1:
            self.ui.variaton1.setText(item["variation"][0])
            self.ui.variation2.hide()
            self.ui.variation3.hide()
        else:
            self.ui.variaton1.setText(item["variation"][0])
            self.ui.variation2.setText(item["variation"][1])
            self.ui.variation3.setText(item["variation"][2])
        self.ui.add_chart.clicked.connect(lambda: self.add_chart_item(item["id"]))
        self.ui.pushButton.clicked.connect(lambda: self.payment(item))
        self.ui.payment_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.item_info))
        self.ui.pushButton_3.clicked.connect(lambda: self.bayar(item))

    def add_chart_item(self, item_id):
        # Function to add the item to the chart
        response = add_to_cart(item_id)
        if response["status"] == True:
            QMessageBox.information(self, "Add to Chart", response["message"])
            console.log("Item added to the chart successfully!")
        else:
            QMessageBox.warning(self, "Add to Chart", response["message"])
            console.log("Failed to add item to the chart!")

    def payment(self, item):
        if self.ui.purchase_amount.value() != 0:
            self.ui.buy_img.setStyleSheet(f"border-image: url({item['image_path']});")
            self.ui.stackedWidget.setCurrentWidget(self.ui.metode_pembayaran)
            self.ui.buy_name.setText(item["name"])
            self.ui.buy_amount.setText(f"× {str(self.ui.purchase_amount.value())}")
            self.ui.buy_variation.setText(self.get_selected_variation())
            with open("./.logger", "r") as logger_file:
                logger_data = json.load(logger_file)
                email = logger_data.get("email")
                password = logger_data.get("password")
            user_data = get_user_data(email=email, password=password)
            self.ui.buy_address.setText(user_data["profile"]["address"])
            self.ui.buy_payment.addItems(["COD", "ProShop Wallet"])
            self.ui.shipping_cost.setText(f"Rp {format(self.shipping, ',')}")
            self.ui.admin_fees.setText(f"Rp {format(self.admin, ',')}")
            self.ui.total_cost.setText(f"Rp {format(discount_price(price=item['price'], discount=item['discount']) * self.ui.purchase_amount.value() + self.shipping + self.admin, ',')}")
        else:
            QMessageBox.warning(self, "Purchase Amount", "Please enter the purchase amount!")

    def get_selected_variation(self):
                if self.ui.variaton1.isChecked():
                    return self.ui.variaton1.text()
                elif self.ui.variation2.isChecked():
                    return self.ui.variation2.text()
                elif self.ui.variation3.isChecked():
                    return self.ui.variation3.text()
                else:
                    return ""
    
    def bayar(self, item):
        if self.ui.buy_payment.currentText() == "COD":
            QMessageBox.information(self, "Payment", "Your order has been placed successfully!")
            console.log("Order placed successfully!")
            add_to_order(product_id=item["id"], price=discount_price(price=item['price'], discount=item['discount']) * self.ui.purchase_amount.value() + self.shipping + self.admin, quantity=self.ui.purchase_amount.value())
            self.close()
        else:
            with open("./.logger", "r") as logger_file:
                logger_data = json.load(logger_file)
                email = logger_data.get("email")
                password = logger_data.get("password")
            user_data = get_user_data(email=email, password=password)
            if user_data["money"] < discount_price(price=item['price'], discount=item['discount']) * self.ui.purchase_amount.value() + self.shipping + self.admin:
                QMessageBox.warning(self, "Payment", "Your balance is not enough to make this purchase!")
            else:
                deduct_money(user_id=user_data["user_id"], amount=discount_price(price=item['price'], discount=item['discount']) * self.ui.purchase_amount.value() + self.shipping + self.admin)
                self.ui.stackedWidget.setCurrentWidget(self.ui.sucess)
                add_to_order(product_id=item["id"], price=discount_price(price=item['price'], discount=item['discount']) * self.ui.purchase_amount.value() + self.shipping + self.admin, quantity=self.ui.purchase_amount.value())
                QMessageBox.information(self, "Payment", "Order placed successfully!")
            console.log("Order placed successfully!")
            self.close()

class UserCharts(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ChartWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("User Charts")  # Set the window title
        self.setWindowIcon(QIcon(os.path.abspath("./views/res/images/logo.jpeg")))
        self.load_chart_items()
        self.show()

    def load_chart_items(self):
        # Function to load the chart items
        with open("./.logger", "r") as logger_file:
            logger_data = json.load(logger_file)
            email = logger_data.get("email")
            password = logger_data.get("password")
        user_ID = get_user_data(email=email, password=password)["user_id"]
        chart_items = get_user_chart(user_id=user_ID)
        for item in chart_items:
            self.list_item = QListWidgetItem()
            self.list_item.setSizeHint(QSize(0, 150))

            self.centralwidget = QWidget()
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
            self.item_images.setStyleSheet(u"border-image: url(" + item["image_path"] + ");")

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
            self.the_category.setText(item["category"])

            self.gridLayout.addWidget(self.the_category, 2, 1, 1, 1)

            self.categ = QLabel(self.frame)
            self.categ.setObjectName(u"categ")
            self.categ.setText("Category: ")

            self.gridLayout.addWidget(self.categ, 2, 0, 1, 1)

            self.desc = QLabel(self.frame)
            self.desc.setObjectName(u"desc")
            font1 = QFont()
            font1.setFamilies([u"Segoe UI Light"])
            font1.setItalic(True)
            self.desc.setFont(font1)
            self.desc.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            self.desc.setWordWrap(True)
            self.desc.setText(item["description"])

            self.gridLayout.addWidget(self.desc, 1, 0, 1, 4)

            self.names_itm = QLabel(self.frame)
            self.names_itm.setObjectName(u"names_itm")
            self.names_itm.setMaximumSize(QSize(16777215, 20))
            font2 = QFont()
            font2.setFamilies([u"Segoe UI Black"])
            font2.setPointSize(10)
            font2.setBold(True)
            self.names_itm.setFont(font2)
            self.names_itm.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            self.names_itm.setText(item["name"])

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
            if item["discount"] != 0:
                self.itm_price.setText(f"Rp {format(discount_price(price=item['price'], discount=item['discount']), ',')}")
            else:
                self.itm_price.setText(f"Rp {format(item['price'], ',')}")

            self.gridLayout_2.addWidget(self.itm_price, 0, 1, 1, 1)

            self.discount_itm = QLabel(self.frame_2)
            self.discount_itm.setObjectName(u"discount_itm")
            self.discount_itm.setMaximumSize(QSize(200, 16777215))
            font3 = QFont()
            font3.setItalic(True)
            font3.setStrikeOut(True)
            self.discount_itm.setFont(font3)
            self.discount_itm.setStyleSheet(u"color: rgb(255, 0, 0);")
            if item["discount"] != 0:
                self.discount_itm.setText(f"Rp {format(item['price'], ',')}")
            else:
                self.discount_itm.hide()

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
            self.Buy_button.clicked.connect(lambda _, item=item: BuyItem(item=item))

            self.horizontalLayout.addWidget(self.Buy_button)

            self.del_btn = QPushButton(self.centralwidget)
            self.del_btn.setObjectName(u"del_btn")
            self.del_btn.setMinimumSize(QSize(130, 130))
            self.del_btn.setMaximumSize(QSize(130, 130))
            self.del_btn.setFont(font4)
            self.del_btn.setStyleSheet(u"background-color: rgb(237, 41, 89);\n"
                            "color: rgb(255, 255, 255);\n"
                            "border-radius: 10px;")
            
            self.del_btn.clicked.connect(lambda: remove_from_cart(user_id=user_ID, product_id=item["id"]))

            self.horizontalLayout.addWidget(self.del_btn)
            
            # Set the item widget for the list item
            self.ui.chart_list.addItem(self.list_item)
            self.ui.chart_list.setItemWidget(self.list_item, self.centralwidget)


    def closeEvent(self, event: CloseEvent):
        console.log("User chart window closed!")

if __name__ == "__main__":
    app = QApplication([])
    window = UsrLoginWindow()
    window.show()
    app.exec()