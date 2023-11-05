import math

def f(x):
    if x == 0 or x == -2:
        return 0
    return math.log10(x + 2) / x

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

# Пример использования:
a = -2
b = -1
area = integrate_rectangular(a, b)
print(f"Площадь под графиком: {area}")
