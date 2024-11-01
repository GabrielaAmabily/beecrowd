N = int(input()) #intervalos no tacografo
distancia = 0

for i in range(N):
    TV= input()
    TV = list(map(int,TV.split()))
    
    distancia = distancia + (TV[0] * TV[1])
    
print(distancia)