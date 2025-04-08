#Conversor de Bases
num = int(input('Insira um numero: '))
print('Escolha entre 1,2 ou 3 para conversão \n'
      '1 = Binario \n'
      '2 = Octal \n'
      '3 = Hexa')
Base = int(input('Qual a Base: '))
if Base == 1:
    print('O numero {} em binario é: {}' .format(num, bin(num)[2:]))
elif Base == 2:
    print('O numero {} em octal é: {}' .format(num, oct(num)[2:]))
elif Base == 3:
    print('O numero {} em hexadecimal é: {}' .format(num, hex(num)[2:]))
else:
    print('Confira as opções e tente novamente!')