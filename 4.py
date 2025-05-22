#factorial de un número
numero = 5
factorial = 1
contador = 1
while contador <= numero:
    factorial *= contador
    contador += 1
print("El factorial de", numero, "es:", factorial)