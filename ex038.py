#Comparador de numeros:
num1 = int(input('Insira um numero: '))
num2 = int(input('Insira outro numero: '))

if num1 > num2:
    print('O primeiro numero: {} é maior que o segundo: {}' .format(num1, num2))
elif num2 > num1:
    print('O segundo numero: {} é maior que o primeiro: {}' . format(num2, num1))
else:
    print('Os 2 numeros são iguais')