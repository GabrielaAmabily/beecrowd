L1 = input()
L2 = input()

L1 = list(map(int,L1.split()))
L2 = list(map(int,L2.split()))

det = ((L1[0]*L2[1]) - (L1[1] * L2[0]))

print(det)