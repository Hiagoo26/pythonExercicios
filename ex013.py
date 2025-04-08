#Aumento de salario
salario = float(input('Insira seu salario: R$'))
aumento = 15 / 100 * salario #ou pode se fazer salario + (15 / 100 * salario)
total = salario + aumento
print('Seu aumento salarial é de 15% com isso seu salario sera de: R${:.2f}'.format(total))
