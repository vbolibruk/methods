import sys
import math

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont, QIntValidator, QDoubleValidator, QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, \
QHBoxLayout, QPushButton, QLineEdit, QLabel, QComboBox,QMessageBox, \
QTableWidget, QTableWidgetItem, QFileDialog, QToolBar, QTextEdit   # QAction
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Calculator:
    @staticmethod
    def calculate(x, y, method):
        l1 = "y = a*x + b"
        l2 = "у = ах^2 + b"
        l3 = "у = а*е^(bх)"
        l4 = "у = b + a/х"
        l5 = "у = а*х^b"
        l6 = "Lagrange Polynomial"
        l7 = "sqrt(а*x + b)"
        l8 = "у = 1/(b + a*х)"
        if method == l1:
            regression = LinearRegression(x, y)
            parameters = regression.line_parameters()
            return parameters
        elif method == l2:
            regression = SquearedEquation(x, y)
            parameters = regression.line_parameters()    
            return parameters
        elif method == l3:
            regression = ExponentEquation(x, y)
            parameters = regression.line_parameters()    
            return parameters
        elif method == l4:
            regression = HyperbolEquation(x, y)
            parameters = regression.line_parameters()    
            return parameters
        elif method == l5:
           regression = PowerEquation(x, y)
           parameters = regression.line_parameters()    
           return parameters
        elif method == l6:
            regression = LagrangePolynomial(x, y)
            parameters = regression.line_parameters()    
            return parameters
        elif method == l7:
            regression = SqrtEquation(x, y)
            parameters = regression.line_parameters()    
            return parameters
        elif method == l8:
            regression = Hyperbol2Equation(x, y)
            parameters = regression.line_parameters()    
            return parameters
        else:
            pass # if other method needed
        
        return None

class LeastSquareMethod:
    def __init__(self, x, y):
        self.param_dict = {}
        self.x = x
        self.y = y
        self.n = x.shape[0]

    def calculate_coefficients(self):
        x = self.x
        y = self.y
        sum_xy = (x*y).sum()
        sum_x = x.sum()
        sum_y = y.sum()
        sum_x2 = (x*x).sum()
        n = x.shape[0]

        #coefficients
        print(sum_xy,sum_x,sum_y,sum_x2,n)
        a = (n*sum_xy - sum_x*sum_y)/(n*sum_x2 - sum_x**2)
        b = (sum_y - a*sum_x)/n
        return [a,b]

    def line_equation(self, a, b, x):
        return a*x + b

    def line_parameters(self):
        a,b = self.calculate_coefficients()
        self.param_dict['a'] = a
        self.param_dict['b'] = b
        self.param_dict['line_function'] = self.line_equation
        self.param_dict['line_label'] = f'{a:.4f}*x + {b:.4f}'
        return self.param_dict


class LinearRegression(LeastSquareMethod):
    def __init__(self, x, y):
        super().__init__(x, y)

    def line_equation(self, a, b, xi):
        return a*xi + b


    def line_parameters(self):
        super().line_parameters()
        a = self.param_dict['a']
        b = self.param_dict['b']
        self.param_dict['line_label'] = f'{a:.4f}*x + {b:.4f}'
        return self.param_dict

class SquearedEquation(LeastSquareMethod):
    def __init__(self, x, y):
        x = x*x
        super().__init__(x, y)

    def line_equation(self, a, b, x):
        return a*x*x + b

    def line_parameters(self):
        print("\n")
        print(self.x,self.y)
        super().line_parameters()
        print(self.param_dict)
        print("\n")
        print("11111111")


        self.x = pd.Series([0, 1, 1.5, 2.5, 3, 4.5, 5, 6])
        self.x = self.x*self.x
        self.y = pd.Series([0, 67, 101, 168, 202, 310, 334, 404])
        print("\n")
        print(self.x,self.y)
        super().line_parameters()
        print(self.param_dict)
        print("2222222")

        a = self.param_dict['a']
        b = self.param_dict['b']
        self.param_dict['line_label'] = f'{a:.4f}*x^2 + {b:.4f}'
        return self.param_dict

class ExponentEquation(LeastSquareMethod):
    def __init__(self, x, y):
        y = np.log(y)
        super().__init__(x, y)

    def line_equation(self, a, b, x):
        # b = math.exp(b)
        return a*np.exp(b*x)


    def line_parameters(self):
        a,b = super().calculate_coefficients()
        self.param_dict['a'] = math.exp(b)
        self.param_dict['b'] = a
        k = self.param_dict['a']
        z = self.param_dict['b']
        self.param_dict['line_label'] = f'{k:.4f}e^{z:.4f}x'
        self.param_dict['line_function'] = self.line_equation
        return self.param_dict

class HyperbolEquation(LeastSquareMethod):
    def __init__(self, x, y):
        x = x[x != 0]
        x = 1/x
        y = y[x != 0]
        super().__init__(x, y)

    def line_equation(self, a, b, x):
        return b+a/x


    def line_parameters(self):
        super().line_parameters()
        a = self.param_dict['a']
        b = self.param_dict['b']
        self.param_dict['line_label'] = f'{b:.4f}+{a:.4f}/x'
        return self.param_dict

class Hyperbol2Equation(LeastSquareMethod):
    def __init__(self, x, y):
        x = x[y != 0]
        y = y[y != 0]
        y = 1/y
        super().__init__(x, y)

    def line_equation(self, a, b, x):
        return 1/(b+a*x)

    
    def line_parameters(self):
        super().line_parameters()
        a = self.param_dict['a']
        b = self.param_dict['b']
        self.param_dict['line_label'] = f'1/({b:.4f}+{a:.4f}*x)'
        return self.param_dict

class PowerEquation(LeastSquareMethod):
    def __init__(self, x, y):
        x = x[x > 0]
        y = y[x > 0]
        x = np.log(x)
        y = np.log(y)

        super().__init__(x, y)

    def line_equation(self, a, b, xi):
        # return math.exp(b)*(x**a)
        return a*(xi**b)

    def line_parameters(self):
        a,b = super().calculate_coefficients()

        self.param_dict['a'] = math.exp(b)
        self.param_dict['b'] = a
        k = self.param_dict['a']
        z = self.param_dict['b']
        self.param_dict['line_function'] = self.line_equation
        self.param_dict['line_label'] = f'{k:.4f}*x^{z:.4f}'
        return self.param_dict

class SqrtEquation(LeastSquareMethod):
    def __init__(self, x, y):
        y = y*y
        super().__init__(x, y)

    def line_equation(self, a, b, x):
        return np.sqrt(a*x + b)

   
    def line_parameters(self):
        super().line_parameters()
        a = self.param_dict['a']
        b = self.param_dict['b']
        self.param_dict['line_label'] = f'sqrt({a:.4f}*x+{b:.4f})'
        return self.param_dict


class LagrangePolynomial(LeastSquareMethod):
    def __init__(self, x, y):
        super().__init__(x, y)

    #y(x) = y0*L0(x) + y1*L2(x) +...+ yn*Ln(x)

    #L0(x) = (x-x1)*(x-x2)*...*(x-xn)/(x0-x1)*(x0-x2)*...*(x0-xn)


    def li(self, i, x):
        numerator = 1
        denominator = 1
        for j in range(self.n):
            if j != i:
                numerator = numerator*(x - (self.x).iloc[j])
                denominator = denominator*( (self.x).iloc[i] - (self.x).iloc[j])
        l_i = numerator/denominator
        return l_i

    def line_equation(self, a, b, x):
        y = 0
        for i in range(self.n):
            y += (self.y).iloc[i]*self.li(i, x)
        return y

    def line_parameters(self):
        a, b = 0, 0
        self.param_dict['a'] = a
        self.param_dict['b'] = b
        self.param_dict['line_function'] = self.line_equation
        self.param_dict['line_label'] = ""
        return self.param_dict

class MNKApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MNK calculation")
        self.setWindowIcon(QIcon("images/char.png"))
        self.setGeometry(100, 100, 800, 600)
        self.setMaximumSize(800, 600)

        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        #main (vertical) layout
        self.main_layout = QVBoxLayout()

        #top part's layout: title
        label_title = QLabel("Least square method")
        font = QFont()
        # font.setBold(False)
        # font.setFamily("Segoe UI")
        font.setPointSize(18)
        label_title.setFont(font)
        label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(label_title)

        #middle part's layout
        self.bottom_layout = QHBoxLayout()

        # left part of bottom layout where input fields
        self.left_layout = QVBoxLayout()

        self.label_method = QLabel("Select method:")
        self.left_layout.addWidget(self.label_method)

        #fields for method selection
        l1 = "y = a*x + b"
        l2 = "у = ах^2 + b"
        l3 = "у = а*е^(bх)"
        l4 = "у = b + a/х"
        l5 = "у = а*х^b"
        l6 = "Lagrange Polynomial"
        l7 = "sqrt(а*x + b)"
        l8 = "у = 1/(b + a*х)"
        self.method_combo = QComboBox()
        self.method_combo.addItem(l1)
        self.method_combo.addItem(l2)
        self.method_combo.addItem(l3)
        self.method_combo.addItem(l4)
        self.method_combo.addItem(l5)
        self.method_combo.addItem(l6)
        self.method_combo.addItem(l7)
        self.method_combo.addItem(l8)

        self.left_layout.addWidget(self.method_combo)

        #botton to draw plot
        self.plot_button = QPushButton("Download data")
        self.plot_button.clicked.connect(self.load_data)
        self.left_layout.addWidget(self.plot_button)

        #botton for calculation
        self.calculate_button = QPushButton("Calculate line")
        self.calculate_button.clicked.connect(self.calculate_line)
        self.left_layout.addWidget(self.calculate_button)

        # # #field for result
        # self.label_parameters = QLabel("Parameters of line:")
        # self.left_layout.addWidget(self.label_parameters)

        #put left layout inside middle layout
        self.bottom_layout.addLayout(self.left_layout) 

        self.left_layout.setAlignment(Qt.AlignmentFlag.AlignTop) 

        # Right part of window: plot

        #Subclass of a wx.Panel which holds two scrollbars and the actual plotting canvas (self.canvas). 
        #It allows for simple general plotting of data with zoom, labels, and automatic axis scaling
        self.canvas = PlotCanvas(self)
        self.bottom_layout.addWidget(self.canvas)

        #put middle layout inside main layout
        self.main_layout.addLayout(self.bottom_layout)

        #field to show result
        self.result_layout = QVBoxLayout()
        self.nodata_result_layout = QHBoxLayout()
        self.result_label = QLabel("Data:")
        self.nodata_result_layout.addWidget(self.result_label)
        self.result_layout.addLayout(self.nodata_result_layout)

        #data field
        self.table_widget = QTableWidget()
        self.result_layout.addWidget(self.table_widget)
        # self.table_widget.setRowCount(1)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["x", "y"])

        self.main_layout.addLayout(self.result_layout)

        self.centralWidget.setLayout(self.main_layout)

        #toolbar
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        # botton "Save"
        save_action = QAction(QIcon("images/save_file.png"), "Save to file", self)
        save_action.triggered.connect(self.save_to_file)
        self.toolbar.addAction(save_action)

        # botton "Open data"
        # open_action = QAction(QIcon("images/open_file.png"), "Open file", self)
        # open_action.triggered.connect(self.open_file) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # self.toolbar.addAction(open_action)

        # botton "Clear data"
        clear_action = QAction(QIcon("images/clear_table.png"), "Clear data", self)
        clear_action.triggered.connect(self.clear_data)
        self.toolbar.addAction(clear_action)

        #data, results as attributes of app class
        self.df = pd.DataFrame(columns=['x', 'y'])
        self.results = {}

    def result_table(self):
        # remove data from table
        self.table_widget.setRowCount(0)

        # number of rows and columns in QTableWidget
        rows_num = self.df.shape[0]
        col_num = self.df.shape[1]
        self.table_widget.setRowCount(rows_num)
        self.table_widget.setColumnCount(col_num)

        # fill out QTableWidget with data from DataFrame
        for row in range(rows_num):
            for col in range(col_num):
                # iat access a single value for a row/column pair by integer position. 
                # Similar to iloc, in that both provide integer-based lookups.
                # Use iat if you only need to get or set a single value in a DataFrame
                item = QTableWidgetItem(str(self.df.iat[row, col])) 
                self.table_widget.setItem(row, col, item)

        # width of columns depends on its content
        self.table_widget.resizeColumnsToContents()


    def draw_plot(self, x, y, y_calculated = None, line_label=None):
        
        self.canvas.plot(x, y)  #draw plot, x - first column, y - second column

    def draw_line(self, x, y, line_label):
        self.canvas.plot_line(x, y, line_label)

    def calculate_line(self):
        if self.df.shape[0] == 0:
            QMessageBox.warning(self, "Error", "Download data first")
            return

        x = self.df.iloc[:, 0]
        y = self.df.iloc[:, 1]
        method = self.method_combo.currentText()
        parameters = Calculator.calculate(x, y, method)
        if parameters is None:
            self.result_label.setText("None")
        else:
            self.draw_plot(x,y)
            a = parameters['a']
            b = parameters['b']
            line_function = parameters['line_function']
            line_label = parameters['line_label']
            if method == "Lagrange Polynomial":
                x = np.linspace(x.min(), x.max(), x.shape[0]*2)
                x_sort = np.sort(x)
            else:
                x_sort = x.sort_values()
            y_calculated = line_function(a,b,x_sort)
            print(x_sort)
            print(y_calculated)
            line_label = parameters['line_label']
            # self.draw_plot(x,y)
            self.draw_line(x_sort, y_calculated, line_label)
            self.result_label.setText(line_label)
            self.results = parameters['line_function'](parameters['a'], parameters['b'], x)
              
    def save_to_file(self):
        
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save to file", "",
            "CSV Files (*.csv);;All Files (*)")
        if file_name:
            with open(file_name, mode='a', newline='') as file:
                file.write(f'{self.results}')

    def load_data(self):
        # options = QFileDialog.Options()
        # options |= QFileDialog.ReadOnly
        
        try:
            file_name, _ = QFileDialog.getOpenFileName(
                self, "Open file", "",
                "Data Files (*.csv);;Text Files (*.txt);;"
                "All files (*)") #, options=options

            if file_name:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # file_data = file.read()
                    # read data in DataFrame
                    self.df = pd.read_csv(file_name, sep=',', encoding='utf-8',  engine='python')
                    self.result_table()
                    x = self.df.iloc[:, 0]
                    # print(x)
                    # print(type(x))
                    y = self.df.iloc[:, 1]

                    self.draw_plot(x, y)

        except FileNotFoundError:
            self.result_label.setText(f"File '{file_name}' is not found.")
        except Exception as e:
            self.result_label.setText(f"Opening file error: {e}")
    
                
    def clear_data(self):
        """Clear the QTextEdit field."""
        ### Check
        if self.df.shape[0] != 0:
            answer = QMessageBox.question(self, "Clear data", 
                "Do you want to clear data?", 
                QMessageBox.StandardButton.No | \
                QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.Yes)
            if answer == QMessageBox.StandardButton.Yes:
                self.result_label.clear()
                self.table_widget.clearContents()
                self.table_widget.setRowCount(0)
                self.df = self.df.drop(index=self.df.index)
                self.canvas.clear()

#!!
class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig, self.ax = plt.subplots()
        super().__init__(fig)
        self.setParent(parent)

    def plot(self, x, y):
        self.ax.clear()
        self.ax.scatter(x, y, s = 5, color = 'b')
        self.ax.axhline(0, color='black', linewidth=0.6)  #show axis X
        self.ax.axvline(0, color='black', linewidth=0.6)  #show axis Y
        self.ax.grid(True)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.draw()

    def plot_line(self, x_sort, y_calculated, line_label):
        self.ax.plot(x_sort, y_calculated, 'r', label=line_label)
        self.ax.legend()
        self.draw()

    def clear(self):
        self.ax.clear()
        self.draw()

def main():
    app = QApplication(sys.argv)
    window = MNKApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()