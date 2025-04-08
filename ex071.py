#Simulador de Caixa Eletronico

valor = int(input('Insira o valor que você deseja sacar: '))
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0

while valor >= 50:
    nota50 += 1
    valor -= 50
while valor >+ 20:
    nota20 += 1
    valor -= 20
while valor >= 10:
    nota10 += 1
    valor -= 10
while valor >= 1:
    nota1 += 1
    valor -= 1
print('Notas entregues: ')
if nota50 > 0:
    print(f'Numero de notas de 50: {nota50}')
if nota20 > 0:
    print(f'Numero de notas de 20: {nota20}')
if nota10 > 0:
    print(f'Numero de notas de 10: {nota10}')
if nota1 > 0:
    print(f'Numero de notas de 1: {nota1}')