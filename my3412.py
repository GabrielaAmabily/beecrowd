N = int(input())

for i in range(N):
    nome = input()
    notas = input()

    notas = list(map(float,notas.split()))
    notas.sort(reverse=True)
    tamanho = len(notas)
    
    if tamanho == 1:
        media = notas[0] /2 
    elif tamanho == 1 or tamanho ==2:
        media = (notas[0] + notas[1]) /2
    elif tamanho == 3 or tamanho == 4:
        media= (notas [0] + notas [1] + notas [2])/3
    
    print(f"{nome}: {media:.1f}")