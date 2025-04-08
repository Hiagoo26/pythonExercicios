#Dobro, triplo e raiz quadrada
n = int(input('Insira um numero: '))
dobro = n * 2
triplo = n * 3
raizq = n ** (1 / 2)
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(n, dobro, triplo, raizq))
#ou sem precisar de 3 variaveis: dobro, triplo e raizq
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(n, (n * 2), (n * 3), (
        n ** (1 / 2))))  #na potencia pode ser pow(n, (1/2))
