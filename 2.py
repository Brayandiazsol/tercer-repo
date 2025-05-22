#imprimir los primeros 20 números primos
def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

contador = 0
numero = 2
while contador < 20:
    if es_primo(numero):
        print(numero, end=" ")
        contador += 1
    numero += 1
print()