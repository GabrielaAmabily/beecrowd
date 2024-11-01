N = int(input())  # tamanho da sequência
V = [0] * N

# Ler os números da sequência
for i in range(N):
    V[i] = int(input())

# Inicializar o contador e o último número marcado
quantMax = 0
ultimo_marcado = None #nenhum

for i in range(N):
    if V[i] != ultimo_marcado:
        quantMax += 1  
        ultimo_marcado = V[i]  

print(quantMax)  