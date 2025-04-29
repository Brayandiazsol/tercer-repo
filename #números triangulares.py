#números triangulares
N = 10  
triangulares = []
n = 1
while len(triangulares) < N:
    triangular = n * (n + 1) // 2
    triangulares.append(triangular)
    n += 1
print("Primeros N números triangulares:", triangulares)