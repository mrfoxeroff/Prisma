from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QTableWidgetItem, \
    QHeaderView
from PyQt5.QtGui import QPixmap
import sys
import sqlite3
from py_files.changing import Ui_Change
from py_files.prisma import Ui_MainWindow
from py_files.log import Ui_log
from py_files.reg import Ui_reg
from py_files.profile import Ui_PerArea
from py_files.restaurant import Ui_RestMenu
from py_files.menu import Ui_Menu
from py_files.films import Ui_Films
from py_files.cinema import Ui_Cinema
from py_files.tickets import Ui_Places
from py_files.admin_panel import Ui_EditAdmin
from py_files.rest_hist import Ui_RestHist
from py_files.cin_hist import Ui_CinHist
from py_files.full_cin_hist import Ui_FullCinHist
from py_files.full_rest_hist import Ui_FullRestHist
from py_files.change_user_base import Ui_ChangeUserBase
from py_files.users_database import Ui_UserBase
from py_files.change_user_data import Ui_ChangeUser
from py_files.add_food import Ui_AddFood
from py_files.delete_food import Ui_DeleteFood
from py_files.method import Ui_Choice


class IncorrectUsername(Exception):
    pass


class IncorrectEmail(Exception):
    pass


class IncorrectPass(Exception):
    pass


class IncorrectValue(Exception):
    pass


class LoginError(Exception):
    pass


class FoodNotFound(Exception):
    pass


class PlaceIsBusy(Exception):
    pass


class Project(Ui_MainWindow, QMainWindow):  # главное окно
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for i in [self.registr, self.login, self.cinema, self.restaurant, self.name, self.name_2,
                  self.target, self.asking]:
            i.hide()

        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()
        self.users_data = self.cur.execute("""SELECT * FROM users""").fetchall()
        self.food_data = self.cur.execute("""SELECT * FROM menu""").fetchall()

        self.profile_data = []
        self.username = ''
        self.username_to_change = ''
        self.registration = Registration(self)
        self.log = Login(self)
        self.rest = Restaurant(self)
        self.cin = Cinema(self)
        self.cinema.clicked.connect(self.cinema_open)
        self.per_area.clicked.connect(self.options)
        self.service.clicked.connect(self.options)
        self.info.clicked.connect(self.options)
        self.login.clicked.connect(self.logging)
        self.registr.clicked.connect(self.regis)
        self.restaurant.clicked.connect(self.restaurant_open)

    def options(self):
        if self.service.isChecked() is True:
            self.restaurant.show()
            self.cinema.show()
        else:
            self.restaurant.hide()
            self.cinema.hide()

        if self.per_area.isChecked() is True:
            self.registr.show()
            self.login.show()
        else:
            self.registr.hide()
            self.login.hide()

        if self.info.isChecked() is True:
            for i in [self.name, self.name_2, self.target, self.asking]:
                i.show()
        else:
            for i in [self.name, self.name_2, self.target, self.asking]:
                i.hide()

    def logging(self):
        self.log.show()

    def regis(self):
        self.registration.show()

    def restaurant_open(self):
        self.rest.show()

    def cinema_open(self):
        self.cin.show()


class Login(QDialog, Ui_log):  # вход в базу данных
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)
        self.first_form = data[0]

        self.flag1 = False

        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()
        self.users_data = []

        self.login_btn.clicked.connect(self.logging)

    def logging(self):
        self.users_data = self.cur.execute("""SELECT * FROM users""").fetchall()
        try:
            for i in self.users_data:
                if i[1] == str(self.username_login.text()) and \
                        i[2] == str(self.password_login.text()):
                    self.flag1 = True
                    if str(self.username_login.text()) == 'admin' and \
                            str(self.password_login.text()) == 'admin':
                        self.first_form.username = i
                    else:
                        self.first_form.username = i
                    break
                else:
                    self.flag1 = False
            if self.flag1 is False:
                raise LoginError
            else:
                self.error.setText('Успешный вход')
                self.first_form.pro = Profile(self, self.first_form)
                self.first_form.admin = AdminPanel(self, self.first_form)
                if self.username_login.text() == 'admin' and \
                        self.password_login.text() == 'admin':
                    self.first_form.admin.show()
                else:
                    self.first_form.pro.show()
                if self.first_form.username == '':
                    self.first_form.user_label.setText('Пользователь: не выбран')
                else:
                    self.first_form.user_label.setText(f'Пользователь: '
                                                       f'{self.first_form.username[1]}')
                self.close()
        except LoginError:
            self.error.setText('Неверное имя пользователя или пароль\nпопробуйте перезайти')


class Profile(QWidget, Ui_PerArea):  # профиль
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()
        self.users_data = self.cur.execute("""SELECT * FROM users""").fetchall()

        self.main_form = data

        self.pixmap = QPixmap('goose.jpg')
        self.pict.setPixmap(self.pixmap)

        if len(data) >= 2:
            self.edit = Edit(self, self.main_form)
            self.name.setText(self.main_form[1].username[1])
            self.name.resize(self.name.sizeHint())

        self.restaurant = Restaurant_history(self, self.main_form)
        self.cinema = CinHist(self, self.main_form)

        self.edit_profile.clicked.connect(self.editing)
        self.rest_hist.clicked.connect(self.restaurant_history)
        self.cin_hist.clicked.connect(self.cinema_history)

    def editing(self):
        self.edit.show()

    def restaurant_history(self):
        self.restaurant.show()

    def cinema_history(self):
        self.cinema.show()


class AdminPanel(QWidget, Ui_EditAdmin):  # админ панель
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.main_form = data
        self.restaurant = Restaurant_history(self, self.main_form)
        self.cinema = CinHist(self, self.main_form)
        self.full_cin = FullCinHist(self, self.main_form)
        self.full_rest = FullRestHist(self, self.main_form)
        self.edit_user_base = ChangeUserBase(self, self.main_form)
        self.food_edit = Methods(self, self.main_form)

        self.pixmap = QPixmap('goose.jpg')
        self.pict.setPixmap(self.pixmap)

        self.rest_hist.clicked.connect(self.show_rest_hist)
        self.cin_hist.clicked.connect(self.show_cin_hist)
        self.full_films.clicked.connect(self.show_full_cin)
        self.full_food.clicked.connect(self.show_full_rest)
        self.edit_base.clicked.connect(self.change_base)
        self.edit_foods.clicked.connect(self.show_methods)

    def show_rest_hist(self):
        self.restaurant.show()

    def show_cin_hist(self):
        self.cinema.show()

    def show_full_cin(self):
        self.full_cin.show()

    def show_full_rest(self):
        self.full_rest.show()

    def change_base(self):
        self.edit_user_base.show()

    def show_methods(self):
        self.food_edit.show()


class Restaurant_history(QWidget, Ui_RestHist):  # история ресторана
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.main_form = data
        self.food_data = []

        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()
        if bool(self.main_form) is True:
            self.food_data = self.cur.execute("""SELECT your_order, \
                    total_price FROM orders WHERE username = ?""",
                                              (str(self.main_form[1][1].username[1]),)).fetchall()

        self.menu.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.menu.verticalHeader().setDefaultSectionSize(20)
        self.menu.horizontalHeader().setDefaultSectionSize(40)
        self.menu.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        self.menu.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.Stretch)
        self.menu.setSortingEnabled(True)

        for i, row in enumerate(self.food_data):
            self.menu.setRowCount(
                self.menu.rowCount() + 1)
            for j, elem in enumerate(row):
                self.menu.setItem(
                    i, j, QTableWidgetItem(str(elem)))


class FullRestHist(QWidget, Ui_FullRestHist):  # полная история заказов (админ)
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.main_form = data
        self.food_data = []

        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()
        if bool(self.main_form) is True:
            self.food_data = self.cur.execute("""SELECT * FROM orders""").fetchall()

        self.menu.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.menu.verticalHeader().setDefaultSectionSize(20)
        self.menu.horizontalHeader().setDefaultSectionSize(40)
        self.menu.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        self.menu.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        self.menu.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.Stretch)
        self.menu.setSortingEnabled(True)

        for i, row in enumerate(self.food_data):
            self.menu.setRowCount(
                self.menu.rowCount() + 1)
            for j, elem in enumerate(row):
                self.menu.setItem(
                    i, j, QTableWidgetItem(str(elem)))


class CinHist(QWidget, Ui_CinHist):  # история кинотеатра
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.main_form = data
        self.cin_data = []

        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()
        if bool(self.main_form) is True:
            self.cin_data = self.cur.execute("""SELECT film, places, total_price \
            FROM cinema WHERE name = ?""",
                                             (str(self.main_form[1][1].username[1]),)).fetchall()
        self.orders.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.orders.verticalHeader().setDefaultSectionSize(20)
        self.orders.horizontalHeader().setDefaultSectionSize(40)
        self.orders.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        self.orders.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        self.orders.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.Stretch)
        self.orders.setSortingEnabled(True)

        for i, row in enumerate(self.cin_data):
            self.orders.setRowCount(
                self.orders.rowCount() + 1)
            for j, elem in enumerate(row):
                self.orders.setItem(
                    i, j, QTableWidgetItem(str(elem)))


class FullCinHist(QWidget, Ui_FullCinHist):  # вся история кинтоеатра (админ)
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.main_form = data
        self.cin_data = []

        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()
        if bool(self.main_form) is True:
            self.cin_data = self.cur.execute("""SELECT * FROM cinema""").fetchall()
        self.orders.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.orders.verticalHeader().setDefaultSectionSize(20)
        self.orders.horizontalHeader().setDefaultSectionSize(40)
        self.orders.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        self.orders.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        self.orders.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        self.orders.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.Stretch)
        self.orders.setSortingEnabled(True)

        for i, row in enumerate(self.cin_data):
            self.orders.setRowCount(
                self.orders.rowCount() + 1)
            for j, elem in enumerate(row):
                self.orders.setItem(
                    i, j, QTableWidgetItem(str(elem)))


class Edit(QWidget, Ui_Change):  # редактировать профиль
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()
        self.users_data = []

        self.main_form = data

        if len(self.main_form) >= 2:
            self.name.setText(self.main_form[1][1].username[1])
            self.password.setText(self.main_form[1][1].username[2])
            self.email.setText(self.main_form[1][1].username[3])
            self.profile = self.cur.execute("""SELECT * FROM users 
            WHERE id = ?""", (self.main_form[1][1].username[0],)).fetchone()

        self.change.clicked.connect(self.edit)

    def edit(self):
        self.users_data = self.cur.execute("""SELECT * FROM users""").fetchall()
        try:
            for i in self.users_data:
                if i == self.profile:
                    continue
                if self.name.text() == i[1]:
                    raise IncorrectUsername
            if '@' not in self.email.text():
                raise IncorrectEmail
            if '.' not in self.email.text():
                raise IncorrectEmail
            self.cur.execute("""UPDATE users SET username = ? WHERE id = ?""", (self.name.text(),
                                                                                self.profile[0]))
            self.cur.execute("""UPDATE users SET password = ? WHERE id = ?""",
                             (self.password.text(),
                              self.profile[0]))
            self.cur.execute("""UPDATE users SET email = ? WHERE id = ?""", (self.email.text(),
                                                                             self.profile[0]))
            self.con.commit()
            self.result.setText('Успешная смена данных')
            self.main_form[1][1].username = self.profile
            self.main_form[1][1].users_data = self.cur.execute("""SELECT * FROM users""").fetchall()
            self.close()
        except IncorrectUsername:
            self.result.setText('Данное имя пользователя уже занято')
        except IncorrectEmail:
            self.result.setText('Неверный формат email')
        except sqlite3.IntegrityError:
            self.error.setText('Данный email уже есть\n в базе данных')


class ChangeUserBase(QWidget, Ui_ChangeUserBase):  # изменить базу данных о пользователях (админ)
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.main_form = data

        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()
        self.userdata = self.cur.execute("""SELECT * FROM users WHERE username = ?""",
                                         (self.name.text(),)).fetchone()
        self.users_data = self.cur.execute("""SELECT * FROM users""").fetchall()

        self.fl = False
        self.user_name = self.name.text()
        self.change_user_data = ''

        self.users_database = ''

        self.all_users.clicked.connect(self.show_user_base)
        self.delete_2.clicked.connect(self.delete_user)
        self.update_user.clicked.connect(self.updating)

    def updating(self):
        try:
            if self.name.text() == '' or self.name.text() is None:
                raise TypeError
            self.change_user_data = ChangeUserData(self, self.name.text(), self.main_form)
            self.change_user_data.show()
        except TypeError:
            self.error.setText('Такого пользователя\nне существует')

    def show_user_base(self):
        self.users_data = self.cur.execute("""SELECT * FROM users""").fetchall()
        self.users_database = UsersBase(self)
        self.users_database.show()

    def delete_user(self):
        try:
            for i in self.users_data:
                if self.name.text() == i[1]:
                    self.fl = True
                    break
                else:
                    self.fl = False
            if self.fl is False:
                raise NameError
            self.cur.execute("""DELETE FROM users WHERE username = ?""", (self.name.text(),))
            self.con.commit()
            self.main_form[1][0].users_data = self.cur.execute("""SELECT * FROM users""")
            self.error.setText('Пользователь успешно\nудалён')
        except NameError:
            self.error.setText('Пользователь не\nнайден')

    def closeEvent(self, event):
        self.name.clear()
        self.error.clear()


class Methods(QWidget, Ui_Choice):  # удалить или добавить блюдо (админ)
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.main_form = data

        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()
        self.food_data = []

        self.delete = ''
        self.add_food = ''

        self.delete_2.clicked.connect(self.show_delete)
        self.add.clicked.connect(self.show_add)

    def show_delete(self):
        self.food_data = self.cur.execute("""SELECT * FROM menu""").fetchall()
        self.delete = DeleteFood(self)
        self.delete.show()

    def show_add(self):
        self.food_data = self.cur.execute("""SELECT * FROM menu""").fetchall()
        self.add_food = AddFood(self)
        self.add_food.show()


class DeleteFood(QWidget, Ui_DeleteFood):  # удалить блюдо из меню ресторана (админ)
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.main_form = data
        self.restaurant = ''
        self.fl = False
        self.food_data = []

        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()

        self.menu.clicked.connect(self.show_menu)
        self.delete_2.clicked.connect(self.delete_food)

    def delete_food(self):
        try:
            for i in self.main_form[0].food_data:
                if i[0] == str(self.name.text()).capitalize():
                    self.fl = True
                    break
                else:
                    self.fl = False
            if self.fl is False:
                raise NameError
            self.cur.execute("""DELETE FROM menu WHERE name = ?""",
                             (str(self.name.text()).capitalize(),))
            self.result.setText('Блюдо удалено')
            self.con.commit()
            self.main_form[0].food_data = self.cur.execute("""SELECT * FROM menu""").fetchall()
        except NameError:
            self.result.setText('Такого блюда нету')

    def show_menu(self):
        self.food_data = self.cur.execute("""SELECT * FROM menu""").fetchall()
        self.restaurant = Menu(self, self.main_form)
        self.restaurant.show()


class AddFood(QWidget, Ui_AddFood):  # добавить блюдо в меню ресторана (админ)
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.main_form = data
        self.fl = False
        self.restaurant = ''

        self.con = sqlite3.connect("prisma.db")
        self.cur = self.con.cursor()

        self.types = self.main_form[0].cur.execute("""SELECT name FROM types""").fetchall()
        for i in self.types:
            self.type.addItem(i[0])

        self.add.clicked.connect(self.add_food)
        self.menu.clicked.connect(self.show_menu)

    def add_food(self):
        try:
            for i in self.main_form[0].food_data:
                if i[0] == self.name.text().capitalize():
                    self.fl = True
                    break
                else:
                    self.fl = False
            if self.name.text() == '':
                raise TypeError
            if self.fl is True:
                raise NameError
            self.cur.execute("""INSERT INTO menu VALUES(?, ?, ?)""",
                             (self.name.text().capitalize(), self.type.currentText(),
                              self.price.value()))
            self.con.commit()
            self.result.setText('Блюдо успешно добавлено')
            self.main_form[0].food_data = self.cur.execute("""SELECT * FROM menu""").fetchall()
        except NameError:
            self.result.setText('Такое блюдо уже есть\nв меню')
        except TypeError:
            self.result.setText('Введите название блюда')

    def show_menu(self):
        self.restaurant = Menu(self, self.main_form)
        self.restaurant.show()

    def closeEvent(self, event):
        self.name.clear()
        self.result.clear()


class ChangeUserData(QWidget, Ui_ChangeUser):  # изменить данные о пользователе (админ)
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.main_from = data
        self.userdata = ()

        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()
        if self.main_from[1] != '' and self.main_from[1] is not None:
            self.user_data = self.cur.execute("""
                           SELECT * FROM users WHERE username = ?""",
                                              (self.main_from[1],)).fetchone()
        if bool(self.main_from) is True:
            self.name.setText(self.user_data[1])
            self.password.setText(self.user_data[2])
            self.email.setText(self.user_data[3])

        self.change.clicked.connect(self.edit)

    def edit(self):
        self.userdata = self.cur.execute("""SELECT * FROM users WHERE username = ?""",
                                         (self.main_from[1],)).fetchone()
        try:
            for i in self.main_from[2][1][0].users_data:
                if i[1] == self.name.text() and i[2] == self.password.text() and i[3] == \
                        self.email.text():
                    continue
                if i[1] == self.name.text():
                    continue
                if i[3] == self.email.text():
                    continue
                if self.name.text() == i[1]:
                    raise IncorrectUsername
            if '@' not in self.email.text():
                raise IncorrectEmail
            if '.' not in self.email.text():
                raise IncorrectEmail
            self.cur.execute("""UPDATE users SET username = ? WHERE username = ?""",
                             (self.name.text(), self.main_from[1]))
            self.cur.execute("""UPDATE users SET password = ? WHERE username = ?""",
                             (self.password.text(), self.main_from[1]))
            self.cur.execute("""UPDATE users SET email = ? WHERE username = ?""",
                             (self.email.text(), self.main_from[1]))
            self.con.commit()
            self.main_from[2][1][0].users_data = self.cur.execute(
                """SELECT * FROM users""").fetchall()
            self.main_from[0].error.setText('Успешная смена\nданных')
            self.close()
        except IncorrectEmail:
            self.result.setText('Неверный формат email')
        except sqlite3.IntegrityError:
            self.result.setText('Данный email или имя\n пользователяуже есть\n в базе данных')


class UsersBase(QWidget, Ui_UserBase):  # база данных о пользователях (админ)
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.main_form = data

        self.users.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.users.verticalHeader().setDefaultSectionSize(20)
        self.users.horizontalHeader().setDefaultSectionSize(40)
        self.users.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.Fixed)
        self.users.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        self.users.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        self.users.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.Stretch)

        for i, row in enumerate(self.main_form[0].users_data):
            self.users.setRowCount(
                self.users.rowCount() + 1)
            for j, elem in enumerate(row):
                self.users.setItem(
                    i, j, QTableWidgetItem(str(elem)))


class Registration(QWidget, Ui_reg):  # регистрация
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.main_form = data[0]

        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()
        self.users_data = []
        self.fl = False
        self.fl2 = False

        self.register_btn.clicked.connect(self.registration)

    def registration(self):
        self.users_data = self.cur.execute("""SELECT * FROM users""").fetchall()
        try:
            for i in self.username.text():
                if i.isdigit() is False:
                    self.fl = True
                    break
                else:
                    self.fl = False
            for i in self.password.text():
                if i.isdigit() is False:
                    self.fl2 = True
                    break
                else:
                    self.fl2 = False
            if len(self.password.text()) < 8:
                raise IncorrectValue
            for i in self.users_data:
                if str(self.username.text()) == i[1]:
                    raise IncorrectUsername
                elif str(self.email.text()) == i[3]:
                    raise IncorrectEmail
            if str(self.password.text()) != str(self.password_correct.text()):
                raise IncorrectPass
            if '@' not in str(self.email.text()):
                raise IncorrectEmail
            if '.' not in str(self.email.text()):
                raise IncorrectEmail
            if self.fl is False:
                raise ValueError
            if self.fl2 is False:
                raise IncorrectValue
            self.cur.execute("""INSERT INTO users(username, password, email) VALUES(?, ?, ?)""",
                             (str(self.username.text()),
                              str(self.password.text()), str(self.email.text())))
            print((self.username.text(),
                   self.password.text(), self.email.text()))
            self.con.commit()
            self.main_form.users_data = self.cur.execute("""SELECT * FROM users""")
            self.close()
        except IncorrectUsername:
            self.error.setText('Данное имя пользователя уже занято')
        except IncorrectValue:
            self.error.setText('Неправильный формат пароля')
        except ValueError:
            self.error.setText('Неправильный формат имя пользователя')
        except IncorrectEmail:
            self.error.setText('Неверный формат email или он уже\nесть в базе данных')
        except IncorrectPass:
            self.error.setText('Пароли не совпадают')

    def closeEvent(self, event):
        self.main_form.users_data = \
            self.main_form.cur.execute("""SELECT * FROM users""").fetchall()
        for j in [self.username, self.password, self.password_correct, self.email]:
            j.clear()


class Restaurant(QWidget, Ui_RestMenu):  # ресторан
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.fl = False
        self.fl2 = False
        self.count = 0
        self.your_order = []
        self.total_price = 0
        self.price_of_food = 0
        self.main_form = data
        self.profile = ''

        self.con = sqlite3.connect('prisma.db')
        self.cur = self.con.cursor()
        self.food_data = self.main_form[0].food_data
        self.menu = ''

        self.do_order.clicked.connect(self.test_order)
        self.show_menu.clicked.connect(self.show_menu_)
        self.add_food_btn.clicked.connect(self.add_food_)
        self.clear_order.clicked.connect(self.clearing)

    def show_menu_(self):
        self.food_data = self.main_form[0].food_data
        self.menu = Menu(self, self.main_form)
        self.menu.show()

    def clearing(self):
        self.your_order.clear()
        self.your_food.clear()
        self.total_price = 0
        self.total.setText('Итого:')

    def add_food_(self):
        try:
            for i in self.food_data:
                if self.add_food.text().lower().capitalize() != i[0]:
                    self.fl2 = False
                elif self.add_food.text().lower().capitalize() == i[0]:
                    self.fl2 = True
                    break
            if self.fl2 is False:
                raise FoodNotFound
            self.your_food.addItem(
                f'{self.add_food.text().capitalize()} {self.count_of_food.value()}')
            self.price_of_food = self.cur.execute("""SELECT price FROM menu WHERE name = ?""",
                                                  (self.add_food.text().capitalize(),)).fetchone()
            self.your_order.append((self.add_food.text().capitalize(), self.count_of_food.value(),
                                    self.price_of_food[0]))
            self.total_price += self.count_of_food.value() * int(self.price_of_food[0])
        except FoodNotFound:
            self.error.setText('Такого блюда нету в меню')
        self.total.setText(f'Итого: {self.total_price}')

    def test_order(self):
        try:
            for i in self.address.text():
                self.count += 1
                if i.isdigit() is True and (self.count == 1 or self.count == 2):
                    self.fl = True
                    break
                else:
                    self.fl = False
            if self.fl is True:
                raise ValueError
            if '@' not in self.email.text():
                raise IncorrectEmail
            if '.' not in self.email.text():
                raise IncorrectEmail
            self.ordering()
        except ValueError:
            self.error.setText('Неправильный формат\nадреса')
        except IncorrectEmail:
            self.error.setText('Неверный формат\nemail')

    def ordering(self):
        self.error.setText('Заказ выполнен успешно,\n ожидайте)')
        self.your_food.clear()
        if self.main_form[0].username == '':
            self.cur.execute("""INSERT INTO orders VALUES(?, ?, ?)""",
                             (self.email.text(), str(self.your_order),
                              self.total_price))
        else:
            self.cur.execute("""INSERT INTO orders VALUES(?, ?, ?)""",
                             (str(self.main_form[0].username[1]), str(self.your_order),
                              self.total_price))
        self.your_order.clear()
        self.total_price = 0
        self.total.setText('Итого:')
        self.con.commit()

    def closeEvent(self, event):
        self.add_food.clear()
        self.total.setText('Итого:')
        self.email.clear()
        self.address.clear()
        self.error.clear()
        self.count_of_food.setValue(1)


class Menu(Ui_Menu, QWidget):  # меню ресторана
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.main_form = data

        self.menu.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.menu.verticalHeader().setDefaultSectionSize(20)
        self.menu.horizontalHeader().setDefaultSectionSize(40)
        self.menu.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        self.menu.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        self.menu.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.Stretch)

        if len(self.main_form) == 2 and len(self.main_form[1]) == 1:
            for i, row in enumerate(self.main_form[1][0].food_data):
                self.menu.setRowCount(
                    self.menu.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.menu.setItem(
                        i, j, QTableWidgetItem(str(elem)))
        self.menu.setSortingEnabled(True)


class Cinema(QWidget, Ui_Cinema):  # кинотеатр
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.fl = False
        self.fl2 = False
        self.fl3 = False
        self.total_count = 0
        self.places = []
        self.main_form = data

        self.con = sqlite3.connect('films.db')
        self.cur = self.con.cursor()
        self.films_data = self.cur.execute("""SELECT title, duration FROM Films""").fetchall()

        self.con2 = sqlite3.connect('prisma.db')
        self.cur2 = self.con2.cursor()

        self.tick = Tickets(self)
        self.films = Films()
        self.films_table.clicked.connect(self.show_films)
        self.pick_place.clicked.connect(self.choose_places)
        self.do_order.clicked.connect(self.ordering)

    def show_films(self):
        self.films.show()

    def choose_places(self):
        self.tick.show()

    def ordering(self):
        try:
            for i in self.first_name.text():
                if i.isdigit() is True:
                    self.fl = True
                    break
                else:
                    continue
            if self.first_name.text() == '':
                self.fl = True
            for j in self.second_name.text():
                if j.isdigit() is True:
                    self.fl = True
                    break
                else:
                    continue
            if self.second_name.text() == '':
                self.fl = True
            for k in self.patronymic.text():
                if k.isdigit() is True:
                    self.fl = True
                    break
            if self.fl is True:
                raise ValueError
            for l in self.films_data:
                if self.film_name.text() == l[0]:
                    self.fl2 = True
                    break
                else:
                    self.fl2 = False
            if self.fl2 is False:
                raise NameError
            self.error.setText('Билеты успешно заказаны')
            if bool(self.places) is False:
                raise PlaceIsBusy
            if bool(self.main_form[0].username) is False:
                self.cur2.execute("""INSERT INTO cinema VALUES(?, ?, ?, ?)""",
                                  (f'{self.first_name.text()} {self.second_name.text()}',
                                   str(self.film_name.text()),
                                   str(self.places), int(self.total_count)))
            else:
                self.cur2.execute("""INSERT INTO cinema VALUES(?, ?, ?, ?)""",
                                  (self.main_form[0].username[1], str(self.film_name.text()),
                                   str(self.places), int(self.total_count)))
            self.con2.commit()
        except ValueError:
            self.error.setText('Неправильный формат\nимени или фамилии')
        except NameError:
            self.error.setText('Такого фильма нету\nв фильмотеке')
        except PlaceIsBusy:
            self.error.setText('Вы не выбрали места')

    def closeEvent(self, event):
        self.film_name.clear()
        self.first_name.clear()
        self.second_name.clear()
        self.patronymic.clear()
        self.error.clear()
        self.places.clear()
        self.total.setText('Итого:')


class Films(QWidget, Ui_Films):  # просмотреть все фильмы
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.con = sqlite3.connect('films.db')
        self.cur = self.con.cursor()
        self.films_data = self.cur.execute("""SELECT title, duration FROM Films""").fetchall()

        self.films.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.films.verticalHeader().setDefaultSectionSize(20)
        self.films.horizontalHeader().setDefaultSectionSize(40)
        self.films.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.Stretch)
        self.films.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents)
        self.films.setSortingEnabled(True)

        for i, row in enumerate(self.films_data):
            self.films.setRowCount(
                self.films.rowCount() + 1)
            for j, elem in enumerate(row):
                self.films.setItem(
                    i, j, QTableWidgetItem(str(elem)))


class Tickets(QWidget, Ui_Places):  # выбор места
    def __init__(self, *data):
        super().__init__()
        self.setupUi(self)

        self.fl = False

        self.main_window = data
        self.order = []

        self.add.clicked.connect(self.add_tickets)
        self.ready.clicked.connect(self.order_ready)

    def add_tickets(self):
        if len(self.order) == 0:
            self.tickets.addItem(f'Ряд '
                                 f'{self.column.currentText()} Место {self.place.currentText()}')
            self.order.append((self.column.currentText(), self.place.currentText()))
        else:
            try:
                for i in self.order:
                    if self.column.currentText() == i[0] and self.place.currentText() == i[1]:
                        self.fl = True
                        break
                    else:
                        self.fl = False
                if self.fl is True:
                    raise PlaceIsBusy
                else:
                    self.tickets.addItem(f'Ряд {self.column.currentText()} '
                                         f'Место {self.place.currentText()}')
                    self.order.append((self.column.currentText(), self.place.currentText()))
                    self.error.clear()
            except PlaceIsBusy:
                self.error.setText('Место уже занято')

    def order_ready(self):
        self.main_window[0].total_count = 0
        self.main_window[0].places = self.order
        if self.main_window[0].format.currentText() == '2D':
            self.main_window[0].total_count += 150 * len(self.main_window[0].places)
        elif self.main_window[0].format.currentText() == '3D':
            self.main_window[0].total_count += 250 * len(self.main_window[0].places)
        self.main_window[0].total.setText(f'Итого: {self.main_window[0].total_count}')
        self.tickets.clear()
        self.error.clear()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pro = Project()
    pro.show()
    sys.exit(app.exec())
