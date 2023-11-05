import math
# (2.40,0.02)

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import math

def equation(x):
    return 2 * x - math.log(x) - 4

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
    b=3
    n=1000
    dx=(b-a)/n

    a_temp = float(from_entry.get())
    if(a_temp >0 ):
        a= a_temp
    b = float(to_entry.get())
    n = int(iterations_entry.get())

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

iterations_label = tk.Label(app, text="Iterations:")
iterations_label.grid(row=2, column=0)
iterations_entry = tk.Entry(app)
iterations_entry.grid(row=2, column=1)

plot_button = tk.Button(app, text="Plot", command=on_plot_button_click)
plot_button.grid(row=3, columnspan=2)

app.mainloop()






