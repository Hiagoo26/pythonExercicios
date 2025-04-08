#Soma de pares
soma = 0
n = (26, 11, 16, 9, 25, 13)
for i in n:
    if i % 2 == 0:
        soma += i
print(soma)