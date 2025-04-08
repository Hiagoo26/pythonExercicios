#Aprovando empréstimo
casa = float(input('Qual o valor da casa: R$'))
salario = int(input('Qual o seu salario: R$ '))
ano = int(input('Ate que ano pretende pagar: '))

prestação = casa / (ano * 12)
print('A prestação é de R${:.2f}' .format(prestação))
trinta = salario * 30/100
if prestação < trinta:
    print('O empréstimo foi aprovado!')
else:
    print('O empréstimo não foi aprovado!')

