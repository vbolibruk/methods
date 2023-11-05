import math
# (2.40,0.02)

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import math


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
    

def equation(x):
    return math.log10(x + 2) / x


def plot_graph(from_x, to_x, answer , a,b):
    x_values = np.linspace(from_x, to_x, 1000)
    y_values = [equation(x) for x in x_values]

    plt.figure(figsize=(12, 6))
    plt.plot(x_values, y_values, label="Equation: 2 * x - ln(x) - 4 = 0")
    plt.plot(answer, 0, 'ro', label=f'Answer for range  from {a} to {b} is {answer})')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.title("Graph of the Equation and Iterations")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

def on_plot_button_click():
    a=-1
    b=-0.5
    n=10000
    n = int(color_var.get())
    a = float(from_entry.get())
    b = float(to_entry.get())

    if(a<0):
        a = check_number_in_range(a)
    elif(a>0):
        a= check_number_in_range(a)
        
    if(b<0):
        b = check_number_in_range(b)
    elif(b>0):
        b = check_number_in_range(b)
        inter_for_first_a =0
    integral_sum = 0
   
    if(True):
        # n = n/2
        step = abs(a+b)/n
        # inter_for_first_b = (b[0]+b[1])/n
        a1 = 0
        b1 = 0
        print(f"a {a},b {b}",{step}) 
        x = a
        while x < b:
            f1 = equation(x)
            f2 = equation(x + step)
            print(x,equation(x))
            area = step * abs(f2 - f1)
            integral_sum += area
    
            x += step


    print(integral_sum)



    # for i in range(n):
    #     if equation(a+i*dx)*equation(a+i*dx+dx)<0:
    #         answer = (a+i*dx+a+i*dx+dx)/2
    #         print(f"answ {answer},iterationEpoch {i}") 
    #         break
    # plot_graph(0.000001, 20, answer , a, b)
        



# Create the main application window
app = tk.Tk()
app.title("Equation Plotter")

# Create and place widgets
from_label = tk.Label(app, text="From:")
from_label.grid(row=0, column=0)
from_entry = tk.Entry(app)
from_entry.grid(row=0, column=1)

to_label = tk.Label(app, text="To:")
to_label.grid(row=1, column=0)
to_entry = tk.Entry(app)
to_entry.grid(row=1, column=1)

# iterations_label = tk.Label(app, text="Iterations:")
# iterations_label.grid(row=2, column=0)
# iterations_entry = tk.Entry(app)
# iterations_entry.grid(row=2, column=1)

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

app.mainloop()
        # n = n/2
        inter_for_first_a = (a+b)/n
        # inter_for_first_b = (b[0]+b[1])/n
        a1 = 0
        b1 = 0

        if(a<b):
            a, b = b, a
        print(f"a {a},b {b}",{inter_for_first_a}) 
        for index, number in enumerate(np.arange(a, b, inter_for_first_a)):
            print(index,number,equation(number))
            b1 = equation(number)
            if(number + inter_for_first_a) > b:

                b2 = equation(number + inter_for_first_a)
                area =  inter_for_first_a * abs(b2 - b1)
                integral_sum = integral_sum + area
            else:
                print(integral_sum)
    print(integral_sum)
