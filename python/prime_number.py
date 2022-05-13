num = int(input())
saida = True

if num == 1:
    saida = False

for i in range(2, int(num**0.5 + 1)):
    if num % i == 0:
        saida = False
        break
        
print(saida)
