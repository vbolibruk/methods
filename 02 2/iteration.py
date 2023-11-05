import math
# (2.40,0.02)

import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
import numpy as np
import math
ODZ  = [-1.999999999, -0.0000000001 ,0.0000000001, 1000 ]
def equation(x):
    return math.log10(x + 2) / x
def find_integration_boundariesa(a):
    global ODZ
    numbers = [-1.999999999, -0.0000000001 ,0.0000000001, 1000 ]
    between_numbers = []
    closest_number = None
    if numbers[0] <= a <= numbers[-1]:
        # Знаходимо числа, між якими знаходиться a
        
        i = 0
        while numbers[i] < a:
            i += 1
        between_numbers.append(numbers[i - 1])
        if i < len(numbers):
            between_numbers.append(numbers[i])
    else:
        # Знаходимо найближче число з масиву
        closest_number = min(numbers, key=lambda x: abs(x - a))
    if len(between_numbers):
        return [a,between_numbers[1]]
    
    return closest_number

def find_integration_boundariesb(a):
    global ODZ
    numbers = [-1.999, -0.001 ,0.001, 1000 ]
    between_numbers = []
    closest_number = None
    if numbers[0] <= a <= numbers[-1]:
        # Знаходимо числа, між якими знаходиться a
        
        i = 0
        while numbers[i] < a:
            i += 1
        between_numbers.append(numbers[i - 1])
        if i < len(numbers):
            between_numbers.append(numbers[i-1])
        
    else:
        # Знаходимо найближче число з масиву
        closest_number = min(numbers, key=lambda x: abs(x - a))
    if len(between_numbers):
        between_numbers.sort()
        return [between_numbers[0],a]
    
    return closest_number



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
    a=0.001
    b=2
    n=1000
    dx=(b-a)/n

    n =  int(color_var.get())
    a = float(from_entry.get())
    b = float(to_entry.get())
    a = find_integration_boundariesa(a)
    b = find_integration_boundariesb(b)
    inter_for_first_a =0
    inter_for_first_b =0
    one_iter = 0
    integral_sum = 0
    if(len(a) and len(b)):
        n = n/2
        inter_for_first_a = (a[0]+a[1])/n
        inter_for_first_b = (b[0]+b[1])/n
        for number in range(a[0], a[1], inter_for_first_a):
            integral_sum = equation(number)
        for number in range(b[0], b[1], inter_for_first_b):
            print(number)
    else:
        one_iter = (a+b)/n





    for i in range(n):
        if equation(a+i*dx)*equation(a+i*dx+dx)<0:
            answer = (a+i*dx+a+i*dx+dx)/2
            print(f"answ {answer},iterationEpoch {i}") 
            break
    plot_graph(0.000001, 20, answer , a, b)
        



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





