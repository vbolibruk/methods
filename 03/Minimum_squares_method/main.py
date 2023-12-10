import sys
import csv
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox, QVBoxLayout
from PyQt6.QtGui import QIcon
from Min_Squares_Ui import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator


class Interpolation(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initializeUI()
        np.set_printoptions(precision=3)
        # self.show()
        self.setGeometry(100, 100, 860, 630)

        self.df = pd.DataFrame()
        self.x_name = ''
        self.y_name = ''
        # self.x = pd.Series()
        # self.y = pd.Series()
        # self.y_calc = pd.Series()
        self.x = np.array([])
        self.y = np.array([])
        self.y_calc = np.array([])

    def initializeUI(self):

        self.setWindowTitle("Інтерполяція функцій")

        self.ui.actionOpen.setIcon(QIcon("images/open.svg"))
        self.ui.actionSave.setIcon(QIcon("images/save.svg"))
        self.ui.actionQuit.setIcon(QIcon("images/quit.svg"))


        self.connectActions()

        # Знайти віджет QGraphicsView за ім'ям ("graphicsView")
        self.ui.graphicsView = self.findChild(QWidget, "graphicsView")

        # Створити віджет графіка Matplotlib
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Отримати поточні вісі для побудови графіка
        self.ax = self.figure.add_subplot(111)
        # Встановлення размеру шрифта для поділок на вісях
        self.ax.tick_params(axis='both', labelsize=8)

        layout = QVBoxLayout(self.ui.graphicsView)
        layout.addWidget(self.canvas)

        self.ui.build_button.clicked.connect(self.build_line)


    def connectActions(self):

        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionSave.triggered.connect(self.saveImage)
        self.ui.actionQuit.triggered.connect(self.close)


    def openFile(self):
        data_file, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", 
            "Text Files (*.txt);;Data Files (*.csv);;\
            HTML Files (*.html);;")
        if data_file:
            with open(data_file, "r") as f:
                self.df = pd.read_csv(data_file, sep=',')
                self.getData()
                self.scatter_plot()

        else:
            QMessageBox.information(self, "No File", 
                "No File Selected.", QMessageBox.StandardButton.Ok)

    def getData(self):
        columns = self.df.columns
        col_x = self.ui.x_column_spinBox.value()
        col_y = self.ui.y_column_spinBox.value()
        self.x_name = columns[col_x]
        self.y_name = columns[col_y]
        self.x = self.df[self.x_name].to_numpy()
        self.y = self.df[self.y_name].to_numpy()

    def scatter_plot(self):

        # графік canvas у вікні інтерфейсу

        self.ax.clear()
        self.ax.scatter(self.x, self.y, color='blue', marker='.')
        # self.ax.axhline(0, color='black')
        # self.ax.axvline(0, color='black')
        self.ax.set_xlabel(self.x_name, fontsize=8)
        self.ax.set_ylabel(self.y_name, fontsize=8)
        # Установка количества делений (ticks) на осях
        self.ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        self.ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        self.ax.tick_params(axis='x', labelrotation=20)
        self.ax.grid(True)
        self.canvas.draw()


    def build_line(self):

        method = self.ui.comboBox_methods.currentText()
        approx = self.ui.comboBox_expressions.currentIndex()
        self.getData()
        self.scatter_plot()

        if method == 'Least squares method':
            a, b = self.least_squares(approx)

            expressions = {0: f'y^ = {a:.3f}*x + {b:.3f}', \
                            1: f'y^ = {a:.3f}*x^2 + {b:.3f}', \
                            2: f'y^ = {a:.3f}/x + {b:.3f}', \
                            3: f'y^ = {a:.3f}*ln(x) + {b:.3f}', \
                            4: f'y^ = sqrt({a:.3f}*x + {b:.3f})', \
                            5: f'y^ = sqrt({a:.3f}*x^2 + {b:.3f})', \
                            6: f'y^ = x/({a:.3f}*x + {b:.3f})', \
                            7: f'y^ = exp({a:.3f}*x + {b:.3f})', \
                            8: f'y^ = {b:.3f}*x^{a:.3f}', \
                            9: f'y^ = 1/({a:.3f}*x + {b:.3f})', \
                            10: f'y^ = {b:.3f}*{a:.3f}^x', \
                            11: f'y^ = {b:.3f}*e^{a:.3f}x'}

            # points to build line
            if approx == 0:
                x_min, x_max = self.x.min(), self.x.max()
                x = np.array([x_min, x_max])
                y = np.array([a*x_min+b,a*x_max+b])

            else:
                x = self.x
                y = self.y_calc

            self.plot_line(x, y)
            try:
                # k correlation and determination
                r, det = self.k_correlation(approx)
                print(r,det)
                text_to_set = f'{expressions[approx]}, K correlation: {r: .4f}, R^2: {det: .4f}'
                self.ui.label_function.setText(text_to_set)
            except ValueError as ve:
                self.ui.label_function.setText(f'{expressions[approx]}, {ve}')

        
    # least squares method
    def least_squares(self, approx):

        # індекси точок, що відповідають ОДЗ
        indices = np.arange(len(self.x))

        # врахувати обмеження ОДЗ
        if approx == 2:
            indices = np.where(self.x != 0)
        elif approx == 3:
            indices = np.where(self.x > 0)
        elif approx == 6:
            indices = np.where(np.logical_and(self.x != 0, self.y != 0))
        elif approx in [7, 10, 11]:
            indices = np.where(self.y > 0)
        elif approx == 8:
            indices = np.where(np.logical_and(self.x > 0, self.y > 0))
        if approx == 9:
            indices = np.where(self.y != 0)

        # виключити дані, що не відповідають ОДЗ обраної функції
        self.x = self.x[indices]
        self.y = self.y[indices]
        

        # замінити х та у для отримання лінійного вигляду фукнції
        xy = {0: (self.x, self.y), # linear\
                1: (self.x*self.x, self.y), # polinom 2 pow\
                2: (1/self.x, self.y), # hyperbolic\
                3: (np.log(self.x), self.y), # logariphm\
                4: (self.x, self.y*self.y), # sq root linear\
                5: (self.x*self.x, self.y*self.y), # sq root 2 pow polinom\
                6: (1/self.x, 1/self.y), # x/linear\
                7: (self.x, np.log(self.y)), # exponential with base exp(ax+b)\
                8: (np.log(self.x), np.log(self.y)), # power\
                9: (self.x, 1/self.y), # 1/linear\
                10: (self.x, np.log(self.y)), # exponential b*a^x
                11: (self.x, np.log(self.y))} # exponential a*e^bx
        
        # find parameters for approximation function
        x_ = xy[approx][0]
        y_ = xy[approx][1]
        print(self.x,"here1")
        print(x_,"here2")
        n = len(x_)
        sum_x = x_.sum()
        sum_y = y_.sum()
        a = (n*(x_*y_).sum() - sum_x*sum_y) / (n*(x_*x_).sum() - sum_x*sum_x)
        b = (sum_y - a*sum_x)/n

        # linear regression
        x = self.x

        if approx == 0:
            self.y_calc = a*x+b  # linear
        elif approx == 1:
            self.y_calc = a*x*x+b  # polinom 2 pow
        elif approx == 2:
            self.y_calc = a/x+b  # hyperbolic
        elif approx == 3:
            self.y_calc = a*np.log(x)+b # logariphm
        elif approx == 4:
            self.y_calc = np.sqrt(a*x+b)  # sq root linear
        elif approx == 5:
            self.y_calc = np.sqrt(a*x*x+b)  # sq root pow 2 polinom
        elif approx == 6:
            self.y_calc = x/(b*x+a)  # x/linear, лініарезований вигляд w = zp + k
        elif approx == 7:
            self.y_calc = np.exp(a*x+b)  # exponential with base exp
        elif approx == 8:
            b = math.exp(b)                 # w = ap + lnb => z=exp(lnz)
            self.y_calc = b * np.power(x, a)  # power
        elif approx == 9:
            self.y_calc = 1/(a*x+b)  # 1/linear
        elif approx == 10:
            a = math.exp(a)
            b = np.exp((sum_y - math.log(a)*sum_x)/n)
            self.y_calc = b * np.power(a,x)              # exponential b*a^x
        elif approx == 11:
            b = math.exp(b)                 # w = bp + lna => a=exp(lna), a=b, b=a
            self.y_calc = b * np.exp(a*x)  # exponential a*e^bx


        return (a, b)

    def k_correlation(self, approx):

        correlation = 0
        x = self.x
        y = self.y
        mean_y = np.mean(y)

    #for linear
        if approx == 0:

            n = len(self.x)
            sum_x = x.sum()
            sum_y = y.sum()
            sum_x2 = (x*x).sum()
            sum_y2 = (y*y).sum()
            mean_x = np.mean(x)
            
            nom = (n*(x*y).sum() - sum_x*sum_y)
            denom = np.sqrt((n*sum_x2 - sum_x*sum_x)*(n*sum_y2 - sum_y*sum_y))
            correlation = nom/denom

            # another formula
            # var_x = x - mean_x
            # var_y = y - mean_y
            # correlation2 = (var_x*var_y).sum()/np.sqrt((var_x*var_x).sum()*(var_y*var_y).sum())
        else:
            dif_model = np.power(self.y - self.y_calc, 2).sum()
            dif_mean = np.power(self.y - mean_y, 2).sum()
            print("here")
            correlation = math.sqrt(1 - dif_model/dif_mean)

        det = correlation**2

        return (correlation, det)


    def plot_line(self, x, y):
        method = self.ui.comboBox_methods.currentText()

        idx = np.argsort(x)
        x = x[idx]
        y = y[idx]

        self.ax.set_title(f'{method}')
        self.ax.plot(x, y, color='red')
        self.canvas.draw()

    def saveImage(self):
        pass

 

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Interpolation()
    window.show()
    sys.exit(app.exec())