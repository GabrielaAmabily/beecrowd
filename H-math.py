N = input() 
N = list(map(int,N.split()))

pri0 = int(N[0] /100)
seg0 = int((N[0] /10) - (10 * pri0))
ter0 = int(N[0] - (10 * int((N[0]/10))))
soma0 = pri0 + seg0 + ter0


pri1 = int(N[1] /100)
seg1 = int((N[1] /10) - (10 * pri1))
ter1 = int(N[1] - (10 * int((N[1]/10))))
soma1 = pri1 + seg1 + ter1

if soma0 > soma1:
    print(soma0)
else:
    print(soma1)

#python tinha pronto
#soma = sum(int(digito) for in n)