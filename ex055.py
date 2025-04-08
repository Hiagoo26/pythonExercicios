#Maior e menor da sêquencia
maior = 0
menor = 0
for i in range (1, 6):
    peso = float(input('Insira o peso: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior é: {}' .format(maior))
print('O menor é: {}' .format(menor))

