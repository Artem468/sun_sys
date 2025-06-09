import sys

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from matplotlib.animation import ArtistAnimation
from scipy.integrate import odeint


class MathModel(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("visual.ui", self)
        self.setWindowTitle("Math model")
        self.setWindowIcon(QIcon(r"data\sun_ico.png"))
        self.setFixedSize(700, 480)
        self.apply_btn.clicked.connect(self.apply_settings)
        self.default_settings_btn.clicked.connect(self.default_settings)

        self.merc_label.setToolTip("1 ПЛАНЕТА ОТ СОЛНЦА<br>ПОКАЗАНА В МОДЕЛИ<br><img src='%s'>" % r"data\merc.jpg")
        self.ven_label.setToolTip("2 ПЛАНЕТА ОТ СОЛНЦА<br>ПОКАЗАНА В МОДЕЛИ<br><img src='%s'>" % r"data\ven.jpg")
        self.earth_label.setToolTip("4 ПЛАНЕТА ОТ СОЛНЦА<br>ПОКАЗАНА В МОДЕЛИ<br><img src='%s'>" % r"data\earth.jpg")
        self.mars_label.setToolTip("5 ПЛАНЕТА ОТ СОЛНЦА<br>ПОКАЗАНА В МОДЕЛИ<br><img src='%s'>" % r"data\mars.jpg")
        self.yup_label.setToolTip("6 ПЛАНЕТА ОТ СОЛНЦА<br>ПОКАЗАНА В МОДЕЛИ<br><img src='%s'>" % r"data\yup.jpg")
        self.saturn_label.setToolTip("7 ПЛАНЕТА ОТ СОЛНЦА<br>ПОКАЗАНА В МОДЕЛИ<br><img src='%s'>" % r"data\saturn.jpg")
        self.uran_label.setToolTip("8 ПЛАНЕТА ОТ СОЛНЦА<br>ПОКАЗАНА В МОДЕЛИ<br><img src='%s'>" % r"data\uran.jpg")
        self.neptun_label.setToolTip("8 ПЛАНЕТА ОТ СОЛНЦА<br>ПОКАЗАНА В МОДЕЛИ<br><img src='%s'>" % r"data\neptun.jpg")
        self.sun_mass_label.setToolTip("СОЛНЦЕ<br>ПОКАЗАНО В МОДЕЛИ<br><img src='%s'>" % r"data\sun.jpg")
        self.count_years_label.setToolTip("ОТВЕЧАЕТ ЗА КОЛИЧЕСТВО ЛЕТ КОТОРЫЕ ПРОЙДУТ В МОДЕЛИ")

    def default_settings(self):
        self.earth_v.setPlainText("29163.97")
        self.uran_v.setPlainText("6499.49")
        self.neptun_v.setPlainText("5275.83")
        self.merc_v.setPlainText("52488.09")
        self.yup_v.setPlainText("12758.24")
        self.saturn_v.setPlainText("9413.95")
        self.ven_v.setPlainText("34255.31")
        self.mars_v.setPlainText("23576.12")
        self.count_years.setPlainText("10")
        self.earth_s.setPlainText("149 * 10 ** 9")
        self.uran_s.setPlainText("3000 * 10 ** 9")
        self.neptun_s.setPlainText("4553 * 10 ** 9")
        self.merc_s.setPlainText("46 * 10 ** 9")
        self.yup_s.setPlainText("778.57 * 10 ** 9")
        self.saturn_s.setPlainText("1430 * 10 ** 9")
        self.ven_s.setPlainText("108 * 10 ** 9")
        self.mars_s.setPlainText("228 * 10 ** 9")
        self.sun_m.setPlainText("1.9 * 10 ** 30")
        self.g_const.setPlainText("6.67 * 10 ** (-11)")

    def apply_settings(self):
        try:
            self.x0_mars = 0.0
            self.v_x0_mars = float(eval(self.mars_v.toPlainText()))
            self.y0_mars = -(float(eval(self.mars_s.toPlainText())))
            self.v_y0_mars = 0.0

            self.x0_ven = -(float(eval(self.ven_s.toPlainText())))
            self.v_x0_ven = 0.0
            self.y0_ven = 0.0
            self.v_y0_ven = -(float(eval(self.ven_v.toPlainText())))

            self.x0_saturn = 0.0
            self.v_x0_saturn = -(float(eval(self.saturn_v.toPlainText())))
            self.y0_saturn = float(eval(self.saturn_s.toPlainText()))
            self.v_y0_saturn = 0.0

            self.x0_yup = 0.0
            self.v_x0_yup = -(float(eval(self.yup_v.toPlainText())))
            self.y0_yup = float(eval(self.yup_s.toPlainText()))
            self.v_y0_yup = 0.0

            self.x0_earth = 0.0
            self.v_x0_earth = -(float(eval(self.earth_v.toPlainText())))
            self.y0_earth = float(eval(self.earth_s.toPlainText()))
            self.v_y0_earth = 0.0

            self.x0_merc = 0.0
            self.v_x0_merc = -(float(eval(self.merc_v.toPlainText())))
            self.y0_merc = float(eval(self.merc_s.toPlainText()))
            self.v_y0_merc = 0.0

            self.x0_neptun = 0.0
            self.v_x0_neptun = -(float(eval(self.neptun_v.toPlainText())))
            self.y0_neptun = float(eval(self.neptun_s.toPlainText()))
            self.v_y0_neptun = 0.0

            self.x0_uran = 0.0
            self.v_x0_uran = -(float(eval(self.uran_v.toPlainText())))
            self.y0_uran = float(eval(self.uran_s.toPlainText()))
            self.v_y0_uran = 0.0

            z0 = (self.x0_mars, self.v_x0_mars, self.y0_mars, self.v_y0_mars,
                  self.x0_ven, self.v_x0_ven, self.y0_ven, self.v_y0_ven,
                  self.x0_saturn, self.v_x0_saturn, self.y0_saturn, self.v_y0_saturn,
                  self.x0_yup, self.v_x0_yup, self.y0_yup, self.v_y0_yup,
                  self.x0_earth, self.v_x0_earth, self.y0_earth, self.v_y0_earth,
                  self.x0_merc, self.v_x0_merc, self.y0_merc, self.v_y0_merc,
                  self.x0_neptun, self.v_x0_neptun, self.y0_neptun, self.v_y0_neptun,
                  self.x0_uran, self.v_x0_uran, self.y0_uran, self.v_y0_uran)

            sun_mass = float(eval(self.sun_m.toPlainText()))
            g_constant = float(eval(self.g_const.toPlainText()))

            self.sec_y = 365 * 24 * 60 * 60
            self.sec_d = 24 * 60 * 60
            self.t = np.arange(0, int(self.count_years.toPlainText()) * self.sec_y, self.sec_d * int(self.count_years.toPlainText()))

            sol = odeint(grav_func, z0, self.t, args=(sun_mass, g_constant))

            fig = plt.figure()
            ax = p3.Axes3D(fig)
            planets = []
            for i in range(0, len(self.t), 1):
                sun, = ax.plot([0], [0], 1, 'yo', ms=10)

                mars_line, = ax.plot(sol[i, 0], sol[i, 2], 1, 'o', color='purple')

                ven_line, = ax.plot(sol[i, 4], sol[i, 6], 1, 'o', color='maroon')

                saturn_line, = ax.plot(sol[i, 8], sol[i, 10], 1, 'o', color='wheat')

                yup_line, = ax.plot(sol[i, 12], sol[i, 14], 1, 'o', color='goldenrod')

                earth_line, = ax.plot(sol[i, 16], sol[i, 18], 1, 'o', color='green')

                merc_line, = ax.plot(sol[i, 20], sol[i, 22], 1, 'o', color='grey')

                neptun_line, = ax.plot(sol[i, 24], sol[i, 26], 1, 'o', color='cadetblue')

                uran_line, = ax.plot(sol[i, 28], sol[i, 30], 1, 'o', color='black')

                planets.append([sun, mars_line, ven_line,
                                saturn_line, yup_line, earth_line,
                                merc_line, neptun_line, uran_line])
            self.ani = ArtistAnimation(fig, planets, interval=10)
            plt.axis('off')
            plt.show()
        except Exception as e:
            print(e)
            msg = QMessageBox()
            msg.setWindowTitle("Внимание")
            msg.setText("Возникла ошибка, проверьте введенные данные на корректность!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()


def grav_func(z, t, sun_mass, G):
    (x_mars, v_x_mars, y_mars, v_y_mars,
     x_ven, v_x_ven, y_ven, v_y_ven,
     x_saturn, v_x_saturn, y_saturn, v_y_saturn,
     x_yup, v_x_yup, y_yup, v_y_yup,
     x_earth, v_x_earth, y_earth, v_y_earth,
     x_merc, v_x_merc, y_merc, v_y_merc,
     x_neptun, v_x_neptun, y_neptun, v_y_neptun,
     x_uran, v_x_uran, y_uran, v_y_uran) = z

    dxdt_mars = v_x_mars
    dv_xdt_mars = -G * sun_mass * x_mars / (x_mars ** 2 + y_mars ** 2) ** 1.5
    dydt_mars = v_y_mars
    dv_ydt_mars = -G * sun_mass * y_mars / (x_mars ** 2 + y_mars ** 2) ** 1.5

    dxdt_ven = v_x_ven
    dv_xdt_ven = -G * sun_mass * x_ven / (x_ven ** 2 + y_ven ** 2) ** 1.5
    dydt_ven = v_y_ven
    dv_ydt_ven = -G * sun_mass * y_ven / (x_ven ** 2 + y_ven ** 2) ** 1.5

    dxdt_saturn = v_x_saturn
    dv_xdt_saturn = -G * sun_mass * x_saturn / (x_saturn ** 2 + y_saturn ** 2) ** 1.5
    dydt_saturn = v_y_saturn
    dv_ydt_saturn = -G * sun_mass * y_saturn / (x_saturn ** 2 + y_saturn ** 2) ** 1.5

    dxdt_yup = v_x_yup
    dv_xdt_yup = -G * sun_mass * x_yup / (x_yup ** 2 + y_yup ** 2) ** 1.5
    dydt_yup = v_y_yup
    dv_ydt_yup = -G * sun_mass * y_yup / (x_yup ** 2 + y_yup ** 2) ** 1.5

    dxdt_earth = v_x_earth
    dv_xdt_earth = -G * sun_mass * x_earth / (x_earth ** 2 + y_earth ** 2) ** 1.5
    dydt_earth = v_y_earth
    dv_ydt_earth = -G * sun_mass * y_earth / (x_earth ** 2 + y_earth ** 2) ** 1.5

    dxdt_merc = v_x_merc
    dv_xdt_merc = -G * sun_mass * x_merc / (x_merc ** 2 + y_merc ** 2) ** 1.5
    dydt_merc = v_y_merc
    dv_ydt_merc = -G * sun_mass * y_merc / (x_merc ** 2 + y_merc ** 2) ** 1.5

    dxdt_neptun = v_x_neptun
    dv_xdt_neptun = -G * sun_mass * x_neptun / (x_neptun ** 2 + y_neptun ** 2) ** 1.5
    dydt_neptun = v_y_neptun
    dv_ydt_neptun = -G * sun_mass * y_neptun / (x_neptun ** 2 + y_neptun ** 2) ** 1.5

    dxdt_uran = v_x_uran
    dv_xdt_uran = -G * sun_mass * x_uran / (x_uran ** 2 + y_uran ** 2) ** 1.5
    dydt_uran = v_y_uran
    dv_ydt_uran = -G * sun_mass * y_uran / (x_uran ** 2 + y_uran ** 2) ** 1.5

    return (dxdt_mars, dv_xdt_mars, dydt_mars, dv_ydt_mars,
            dxdt_ven, dv_xdt_ven, dydt_ven, dv_ydt_ven,
            dxdt_saturn, dv_xdt_saturn, dydt_saturn, dv_ydt_saturn,
            dxdt_yup, dv_xdt_yup, dydt_yup, dv_ydt_yup,
            dxdt_earth, dv_xdt_earth, dydt_earth, dv_ydt_earth,
            dxdt_merc, dv_xdt_merc, dydt_merc, dv_ydt_merc,
            dxdt_neptun, dv_xdt_neptun, dydt_neptun, dv_ydt_neptun,
            dxdt_uran, dv_xdt_uran, dydt_uran, dv_ydt_uran)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MathModel()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
