from scipy.integrate import quad
import math
from math import e

a = -6
b = -5.99
pi = math.pi

def integrando(x):
    return (((e**((-1 / 2) * (x ** 2))) / ((2 * pi) ** (1 / 2))))

# _ Es el error entre el valor

with open('Impresion_Integral.txt', 'w') as archivo:
    archivo.write('Resultados de la integral\n')
    while(b <= 6.01): 
        resultado, _ = quad(integrando, a, b)
        archivo.write(str(resultado))
        archivo.write("\n")
        b += 0.01
print("Se han imprimido los resultados correctamente en el archivo!")

b = -5.99

"""
while(b <= 6.01):
        resultado, _ = quad(integrando, a, b)
        print(f"{resultado}\n")
        b += 0.01
"""