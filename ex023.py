#4 numeros separados:
fournum = int(input('Insira um numero de 0 a 9999: '))
num = fournum // 1 % 10
print('Unidade: {}' .format(num))
print('Dezena: {}' .format(fournum // 10 % 10))
print('Centena: {}' .format(fournum // 100 % 10))
print('Milhar: {}' .format(fournum // 1000 % 10 ))

