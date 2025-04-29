#numeros aleatorios
import random

mayor = 0

for _ in range(10):
    numero = random.randint(1, 100)
    print("Número generado:", numero)
    if numero > mayor:
        mayor = numero

print("El mayor número es:", mayor)