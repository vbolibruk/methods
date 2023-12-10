import math
# (2.40,0.02)

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import math
import random


ODZ  = [-1.999999999, -0.0000000001 ,0.0000000001, 1000 ]

numbers =[-1.999, -0.001 ,0.001, 1000 ]
prev_number = 0

def check_number_in_range(n):
    global numbers
    global prev_number
    bound = 0
    prev_number = n

    if(prev_number<=0):
        bound =-0.001
    else:
        bound =0.001
    # Получаем минимальное значение из списка
    min_num = min(numbers)
    max_num = max(numbers)
    # Проверяем, находится ли число в заданном диапазоне
    if(n<0):
        if n < min_num:
            return min_num
        elif numbers[0] <= n <= numbers[-1]:
            return n
        else:
            return bound
    elif(n>0):
        if n > max_num:
            return max_num
        elif numbers[0] <= n <= numbers[-1]:
            return n
        else:
            return bound
    elif(n==0):
        return bound
    

import math

def f(x):
    try:
        return math.log10(x + 2) / x
    except ValueError:
        return float('nan')

def integrate_rectangular(a, b, n=1000):
    """Вычисление интеграла функции f на интервале [a, b] с использованием метода прямоугольников."""
    
    # Если границы включают неопределенные точки, сместите их немного.
    if a == 0 or a == -2:
        a += 1e-10
    if b == 0 or b == -2:
        b -= 1e-10
    
    h = (b - a) / n
    integral = 0
    
    for i in range(n):
        # Вычисляем значение в начале интервала для текущего прямоугольника
        x_value = a + i * h
        integral += f(x_value) * h
    
    return integral

def integrate_trapezoidal(a, b, n=1000):
    """Вычисление интеграла функции f на интервале [a, b] с использованием метода трапеций."""
    
    # Если границы включают неопределенные точки, сместите их немного.
    if a == 0 or a == -2:
        a += 1e-10
    if b == 0 or b == -2:
        b -= 1e-10
    
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        x_value = a + i * h
        integral += f(x_value)
    
    integral *= h

    return integral

def integrate_monte_carlo(a, b, samples=1000):
    """Вычисление интеграла функции f на интервале [a, b] с использованием метода Монте-Карло."""
    
    sum_of_samples = 0
    for _ in range(samples):
        # Генерируем случайное число в интервале [a, b]
        random_point = a + (b - a) * random.random()
        # Добавляем значение функции в этой точке к сумме
        sum_of_samples += f(random_point)

    # Усредняем сумму и умножаем на длину интервала
    average = sum_of_samples / samples
    integral = average * (b - a)

    return integral

def plot_graph(from_x, to_x):
    x_values = np.linspace(from_x, to_x, 1000)
    
    # Filter out -2 and 0 from x_values
    x_values = x_values[(x_values != -2) & (x_values != 0)]
    
    y_values = [f(x) for x in x_values]

    plt.figure(figsize=(12, 6))
    plt.plot(x_values, y_values, label="Equation: math.log10(x + 2) / x")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.title("Graph of the Equation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
def display_results_in_table(a, b, integral_result , type):
    global tree
    # Create a new window for the table

    # Initialize treeview for the table

    # Insert integration results into the table
    tree.insert("", "end", values=(a, b, integral_result,type))
def on_plot_button_click():
    a=-2
    b=-1
    n=1000
    n =  int(color_var.get())
    a = float(from_entry.get())
    b = float(to_entry.get())
    function_dropdown2 = function_dropdown.get()
    print(function_dropdown2)

    if(function_dropdown2 == "прямокутників"):
        area = integrate_rectangular(a, b)
        
        print(f"Площадь под графиком: {area}")
    if(function_dropdown2 == "трапецій"):
        area = integrate_trapezoidal(a, b)
        
        print(f"Площадь под графиком: {area}")


    if(function_dropdown2 == "Монте-Карло"):
        area = integrate_monte_carlo(a, b)
        
        print(f"Площадь под графиком: {area}")


    display_results_in_table(a, b, area, function_dropdown2)



    # for i in range(n):
    #     if equation(a+i*dx)*equation(a+i*dx+dx)<0:
    #         answer = (a+i*dx+a+i*dx+dx)/2
    #         print(f"answ {answer},iterationEpoch {i}") 
    #         break
    plot_graph(-10, 3)
        
# Create the main application window
app = tk.Tk()
app.title("Equation Plotter")

# Create and place widgets
from_label = tk.Label(app, text="From:")
from_label.grid(row=0, column=0)
from_entry = tk.Entry(app)
from_entry.grid(row=0, column=1)
from_entry.insert(-2, "-2")

to_label = tk.Label(app, text="To:")
to_label.grid(row=1, column=0)
to_entry = tk.Entry(app)
to_entry.grid(row=1, column=1)
to_entry.insert(-1, "-1")

plot_button = tk.Button(app, text="Plot", command=on_plot_button_click)
plot_button.grid(row=3, columnspan=2)

# Dropdown for selecting a function
function_label = tk.Label(app, text="метод:")
function_label.grid(row=4, column=0)
functions = ["прямокутників", "трапецій", "Монте-Карло"]
function_var = tk.StringVar(value=functions[0])
function_dropdown = ttk.Combobox(app, textvariable=function_var, values=functions)
function_dropdown.grid(row=4, column=1)

# Dropdown for selecting a color
color_label = tk.Label(app, text="N:")
color_label.grid(row=5, column=0)
colors = [10, 20, 50,100,1000]
color_var = tk.StringVar(value=colors[0])
color_dropdown = ttk.Combobox(app, textvariable=color_var, values=colors)
color_dropdown.grid(row=5, column=1)
table_window = tk.Toplevel()
table_window.title('Integration Results')
tree = ttk.Treeview(table_window, columns=('A', 'B', 'Result', 'type'), show='headings')
tree.heading('A', text='From (A)')
tree.heading('B', text='To (B)')
tree.heading('Result', text='Integration Result')
tree.heading('type', text='Integration type')

tree.pack(pady=20)

app.mainloop()
