#los primeros N números triangulares
N = 10
contador = 1
while contador <= N:
    triangular = (contador * (contador + 1)) // 2
    print(triangular, end=" ")
    contador += 1
print()