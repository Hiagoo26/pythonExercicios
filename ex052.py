#Numeros primos
n = int(input('Insira um numero: '))
for i in range(1, n):
    if n % i != 0:
        print('{} é primo' .format(n))
    else:
        print('{} não é primo' .format(n))


