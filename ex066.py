#Mesma coisa do 64
n =int(input('Digite um numero: '))
contador = 0
soma = 0
while True:
    if n == 999:
        break
    soma += n
    n = int(input('Digite outro numero: '))
    contador += 1
print(f'Foram digitados {contador} numeros e a soma total é {soma}')