import numpy as np
import matplotlib.pyplot as plt

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def fibonacci_search(f, a, b, epsilon):
    L = b - a
    fib_sequence = fibonacci(100)  
    N = next(i for i, v in enumerate(fib_sequence) if v >= L / epsilon) - 1
    x = np.linspace(a, b, 400)
    plt.figure(figsize=(8, 6))
    plt.plot(x, f(x), label='f(x)', color='pink')
    y = a + (fib_sequence[N - 2] / fib_sequence[N]) * (b - a)
    z = a + (fib_sequence[N - 1] / fib_sequence[N]) * (b - a)
    x_p, y_p = [y, z], [f(y), f(z)]
    for k in range(1, N - 2):
        if f(y) > f(z):
            a = y
            y = z
            z = a + (fib_sequence[N - k - 1] / fib_sequence[N - k]) * (b - a)
        else:
            b = z
            z = y
            y = a + (fib_sequence[N - k - 2] / fib_sequence[N - k]) * (b - a)
        x_p.append((a + b) / 2)
        y_p.append(f((a + b) / 2))
    
    plt.scatter(x_p, y_p, color='black', label='Точки сходимости')
    plt.scatter((a + b) / 2, f((a + b) / 2), color='green', s=100, label='Точка минимума')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Метод Фибоначчи')
    plt.legend()
    plt.grid(True)
    plt.show()

    return (a + b) / 2

def f(x):
    return x**2 + 4*x + 5

a, b = -4, 6
epsilon = 1e-15

min_point = fibonacci_search(f, a, b, epsilon)
print(f"Минимум функции находится в точке: {min_point:.5f}, значение функции в этой точке: {f(min_point):.5f}")