#Multiplus de 3
soma = 0
for n in range(0 ,500 + 1):
    if n % 2 != 0 and n % 3 == 0:
       soma += n
print(soma)
