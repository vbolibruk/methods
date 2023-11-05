import math
# Set the step size
step = 0.001

# Set the range limits
lower_limit = -10
upper_limit = 10

# Встановимо функцію і обмежимо знаменник
def odz(x):
    if x != 0 and x + 2 > 0:
        return math.log10(x + 2) / x
    else:
        return None

# Знайдемо область визначення
domain = [x * step for x in range(int(lower_limit/step), int(upper_limit/step) + 1) if f(x * step) is not None]


# Виведемо область визначення
print("Область визначення:", domain)
