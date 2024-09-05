import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math
from math import e

m = float(input("Ingrese el Valor de Miu: "))
d = -1

while d <= 0:
    d = float(input("Ingrese el Valor de Delta (debe ser mayor que 0): "))
a = float(input("Ingrese el límite inferior: "))
b = float(input("Ingrese el límite superior: "))
pi = math.pi

def integrando(x):
    return (((e**((-1 / 2) * (((x - m) / d) ** 2))) / (d * (2 * pi) ** (1 / 2))))

# Calcular el área bajo la curva de la función entre a y b
resultado, _ = quad(integrando, a, b)
print(f"El área bajo la curva entre {a} y {b} es: {resultado}")

# Visualizar la función graficada entre los límites a y b
x_values = np.linspace(a, b, 1000)  # Generar 1000 puntos entre a y b
y_values = integrando(x_values)  # Evaluar la función en esos puntos

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='Función')
plt.fill_between(x_values, 0, y_values, where=(x_values >= a) & (x_values <= b), alpha=0.3)
plt.title('Función entre los límites dados')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()