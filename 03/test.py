import matplotlib.pyplot as plt
import pandas as pd
# Задаємо дані (приклади)
x0 = pd.Series([ 0, 1, 1.5, 2.5 ,3 ,4.5 ,5 ,6])
x = pd.Series([ 0, 1, 1.5, 2.5 ,3 ,4.5 ,5 ,6])
y = pd.Series([ 0 ,67 ,101 ,168, 202 ,310 ,334 ,404])
def func(a, b, x):
    return a*x*x +b  

# Инициализация сумм
sum_x_squared = 0
sum_x = 0
sum_y = 0
sum_xy = 0

x = x * x
# Вычисление сумм

sum_xy = (x*y).sum()
sum_x = x.sum()
sum_y = y.sum()
sum_x2 = (x*x).sum()
n = len(x)
print(sum_xy,sum_x,sum_y,sum_x2,n)
#coefficients
a = (n*sum_xy - sum_x*sum_y)/(n*sum_x2 - sum_x**2)
b = (sum_y - a*sum_x)/n


# Виводимо результат
print(f'Коефіцієнт a: {a}')
print(f'Коефіцієнт b: {b}')

# Побудова функції апроксимації

x_sort = x0.sort_values()
y_calculated = func(a,b,x_sort)



# Графік оригінальних даних та апроксимації
plt.scatter(x0, y, label='Дані')
plt.plot(x_sort, y_calculated, 'r', label='Апроксимація')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Графік функції y = a*x*x +b')
plt.grid(True)
plt.show()
