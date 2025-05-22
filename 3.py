#lista de N números aleatorios
import random

N = 10
lista = []
contador = 0
while contador < N:
    lista.append(random.randint(1, 100))
    contador += 1

mayor = lista[0]
i = 1
while i < N:
    if lista[i] > mayor:
        mayor = lista[i]
    i += 1

print("Lista:", lista)
print("El mayor número es:", mayor)