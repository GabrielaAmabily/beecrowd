N = int(input())
result = 1

for i in range(N):
    result = result * (N - i)
    
print(result)