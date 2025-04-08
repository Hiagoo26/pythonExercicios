#Tratamento de vários valores v1.0
n = int(input('Digite um numero: '))
contador = 0
soma = 0
while n != 999:
    soma += n
    n = int(input('Digite outro numero: '))
    contador += 1
print('Você digitou {} numeros, e a soma de numeros digitados é de {}' .format(contador, soma))