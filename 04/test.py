import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Задаємо дані (приклади)
x_data = pd.Series([0, 1, 1.5, 2.5, 3, 4.5, 5, 6])
y_data = pd.Series([0, 67, 101, 168, 202, 310, 334, 404])

def func(a, b, x):
    return a * x * x + b

# Функція для обчислення полінома Лагранжа
def lagrange_interpolation(x, y, xi):
    result = 0
    for i in range(len(x)):
        term = y[i]
        for j in range(len(x)):
            if i != j:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term
    return result

def lagrange_polynomial(x, y):
    n = len(x)
    polynomial = ""
    
    for i in range(n):
        term = f"{y[i]:.2f}"
        
        for j in range(n):
            if i != j:
                term += f" * (x - {x[j]:.2f}) / ({x[i] - x[j]:.2f})"
        
        if i < n - 1:
            term += " + "
        
        polynomial += term
    
    return polynomial

polynomial = lagrange_polynomial(x_data, y_data)

print("Поліном Лагранжа:", polynomial)


# Генеруємо точки для апроксимації
x_interp = np.linspace(x_data.min(), x_data.max(), 6)
print(x_interp)
y_interp = [lagrange_interpolation(x_data, y_data, xi) for xi in x_interp]

# Графік оригінальних даних та апроксимації
plt.scatter(x_data, y_data, label='Дані')
plt.plot(x_interp, y_interp, 'r', label='Апроксимація')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Графік функції y = a*x*x + b')
plt.grid(True)
plt.show()
