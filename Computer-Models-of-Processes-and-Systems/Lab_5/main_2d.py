import numpy as np
import matplotlib.pyplot as plt

def solution1():
    x = np.linspace(-10, 10, 2000)
    x = x[np.abs(x + 2) > 1e-6]
    y = np.abs(x + 4.0 / (x + 2.0))

    plt.figure(figsize=(9, 5))
    plt.plot(x, y, 'b-', linewidth=1.8, label=r'y = abs(x + 4 \ (x + 2))')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(0, 15)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

def solution2():
    x = np.linspace(-2, 2, 1000)
    y1 = x * np.sin(x)
    y2 = 1.0 / (3.0 * x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y1, 'b-', linewidth=1.5, label=r'y1 = x*sin(x)')
    plt.plot(x, y2, 'r--', linewidth=1.5, label=r'y2 = 1/3x')
    plt.title('Вариант 5. Задание 2: y₁ = x*sin(x),  y₂ = 1/3x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

def solution3():
    a, l = 4, 1
    phi = np.linspace(0, 2 * np.pi, 1000)
    ro = a * phi - l
    mask = ro >= 0
    phi_plot = phi[mask]
    ro_plot = ro[mask]

    plt.figure(figsize=(7, 7))
    ax = plt.subplot(111, projection='polar')
    ax.plot(phi_plot, ro_plot, 'b-', linewidth=1.5)
    ax.grid(True, linestyle='--', alpha=0.6)
    plt.show()

def solution4():
    x = np.linspace(-2, 2, 4000)
    x = x[np.abs(x) > 1e-8]

    mask_left = x < 0
    mask_right = x >= 0

    f = np.empty_like(x)
    f[mask_left] = np.sqrt(1.0 + x[mask_left] ** 2) / (2.0 * np.abs(x[mask_left]))
    f[mask_right] = 2.0 + np.cos(x[mask_right]) ** 3

    plt.figure(figsize=(9, 5))
    plt.plot(x[mask_left], f[mask_left], 'b-', linewidth=1.8,
             label=r'f(x)= (sqrt(1 + x^2) / (2 * |x|)); x<0')
    plt.plot(x[mask_right], f[mask_right], 'r-', linewidth=1.8,
             label=r'f(x)= 1 / (2 * cos(x)^3); x >= 0')
    plt.axvline(0, color='black', linestyle='--', linewidth=1,
                label='x = 0 (граница)')
    plt.xlabel('x');
    plt.ylabel('f(x)')
    plt.ylim(0, 6)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

def solution5():
    t = np.linspace(0, 2 * np.pi, 2000)
    r_t = t + np.sin(t) ** 2
    phi_t = 3 * t ** 2 + t

    x5 = r_t * np.cos(phi_t)
    y5 = r_t * np.sin(phi_t)

    plt.figure(figsize=(8, 8))
    plt.plot(x5, y5, 'b-', linewidth=1.2)
    plt.xlabel('x');
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.axis('equal')
    plt.show()

solution1()
solution2()
solution3()
solution4()
solution5()
