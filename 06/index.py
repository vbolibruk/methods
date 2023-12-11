import numpy as np
import matplotlib.pyplot as plt

# Функція, яка описує диференціальне рівняння
def differential_equation(x, y):
    return (1 - 2 * x) / (y ** 2)

# Метод Ейлера для розв'язання диференціального рівняння
def euler_method(func, y0, x0, h, n):
    x_values = [x0]
    y_values = [y0]

    for i in range(n):
        x_new = x_values[-1] + h
        y_new = y_values[-1] + h * func(x_values[-1], y_values[-1])
        x_values.append(x_new)
        y_values.append(y_new)

    return x_values, y_values

# Метод Рунге-Кутта 4-го порядку для розв'язання диференціального рівняння
def runge_kutta_method(func, y0, x0, h, n):
    x_values = [x0]
    y_values = [y0]

    for i in range(n):
        x_new = x_values[-1] + h
        k1 = h * func(x_values[-1], y_values[-1])
        k2 = h * func(x_values[-1] + h / 2, y_values[-1] + k1 / 2)
        k3 = h * func(x_values[-1] + h / 2, y_values[-1] + k2 / 2)
        k4 = h * func(x_values[-1] + h, y_values[-1] + k3)
        y_new = y_values[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_values.append(x_new)
        y_values.append(y_new)

    return x_values, y_values

# Аналітичний розв'язок
def analytical_solution(x):
    return np.sqrt(1 + x - x**2)

# Початкові умови та інтервал диференціювання
x0 = 0
y0 = 1
h1 = 0.1
h2 = 0.2
n1 = int(2 / h1)
n2 = int(2 / h2)

# Розв'язок за допомогою методу Ейлера
x_euler1, y_euler1 = euler_method(differential_equation, y0, x0, h1, n1)
x_euler2, y_euler2 = euler_method(differential_equation, y0, x0, h2, n2)

# Розв'язок за допомогою методу Рунге-Кутта
x_rk1, y_rk1 = runge_kutta_method(differential_equation, y0, x0, h1, n1)
x_rk2, y_rk2 = runge_kutta_method(differential_equation, y0, x0, h2, n2)

# Аналітичний розв'язок
x_analytical = np.linspace(0, 2, 100)
y_analytical = analytical_solution(x_analytical)

# Побудова графіків
plt.figure(figsize=(10, 6))
plt.plot(x_analytical, y_analytical, label='Аналітичний розв\'язок', color='blue')
plt.plot(x_euler1, y_euler1, label='Ейлер (h=0.1)', linestyle='--', marker='o', color='orange')
plt.plot(x_euler2, y_euler2, label='Ейлер (h=0.2)', linestyle='--', marker='x', color='red')
plt.plot(x_rk1, y_rk1, label='Рунге-Кутта (h=0.1)', linestyle='-.', marker='s', color='green')
plt.plot(x_rk2, y_rk2, label='Рунге-Кутта (h=0.2)', linestyle='-.', marker='^', color='purple')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Порівняння чисельних методів та аналітичного розв\'язку')
plt.show()
