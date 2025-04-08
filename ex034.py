#Aumentos multiplos
salario = float(input('Qual seu salario: R$'))
if salario > 1250.00:
    aumento1 = 10/100 * salario
    print('Com o aumento de 10% seu salario sera de: {:.2f}' .format(salario + aumento1))
else:
    aumento2 = 15/100 * salario
    print('Com o aumento de 15% seu salario sera de: {:.2f}' .format(salario + aumento2))