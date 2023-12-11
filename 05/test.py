import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 2*x

def f_prime(x):
    return 3*x**2 + 2

def f_prime2(x):
    return 6*x

def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_diff(f, x, h):
    return (f(x) - f(x - h)) / h

def central_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

x_val = 1
delta_x_values = [0.5, 0.2, 0.1, 0.01, 0.001]

results = []

for delta_x in delta_x_values:
    value = f(x_val)
    analytical = f_prime(x_val)
    forward = forward_diff(f, x_val, delta_x)
    backward = backward_diff(f, x_val, delta_x)
    central = central_diff(f, x_val, delta_x)
    
    results.append({
        'Δx': delta_x,
        'y(x)': value,
        'Analytical': analytical,
        'Forward Difference': forward,
        'Backward Difference': backward,
        'Central Difference': central
    })

print("Δx\ty(x)\tAnalytical\tForward\t\tBackward\tCentral")
for result in results:
    print(f"{result['Δx']}\t{result['y(x)']}\t{result['Analytical']}\t\t{result['Forward Difference']}\t{result['Backward Difference']}\t{result['Central Difference']}")


# Choose the interval
start = 0  # start of the interval
end = 20    # end of the interval
num_points = 20  # number of points at which to calculate the derivative

# Create an array of x-values from start to end
x_values = np.linspace(start, end, num_points)

# Calculate the derivative at each point
f_simple = f(x_values)
derivatives_f_prime = f_prime(x_values)
derivatives_f_prime2 = f_prime2(x_values)


plt.figure(figsize=(20, 8))

# Графік функції
plt.subplot(131)
plt.plot(x_values, f_simple, label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Графік першої похідної
plt.subplot(132)
plt.plot(x_values, derivatives_f_prime, label="f'(x)")
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.legend()

# Графік другої похідної
plt.subplot(133)
plt.plot(x_values, derivatives_f_prime2, label="f''(x)")
plt.xlabel('x')
plt.ylabel("f''(x)")
plt.legend()

# Виведення точок екстремуму та перегину
extremum_points = x_values[np.where(derivatives_f_prime2 == 0)]  # Точки, де друга похідна дорівнює нулю
inflection_points = x_values[np.where(derivatives_f_prime == 0)]  # Точки, де перша похідна дорівнює нулю


print(extremum_points,inflection_points)
plt.scatter(extremum_points, f(extremum_points), color='red', marker='o', label='Extremum Points')
plt.scatter(inflection_points, f(inflection_points), color='green', marker='x', label='Inflection Points')
plt.legend()

plt.tight_layout()
plt.show()
