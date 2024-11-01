import math

n = int(input())
contador = 0
lista = []

for d in range(1, int(math.sqrt(n)) + 1):
    if n % d == 0:
        lista.append(d)  
        if d != n // d:  
            lista.append(n // d)
        contador += 2 if d != n // d else 1 

if contador == 2:
    print(1)
    print(n)
else:
    lista.sort()
    for divisor in lista:
        print(divisor)
