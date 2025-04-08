#Qual numero é maior:
A = int(input('Insira um numero: '))
B = int(input('Insira outro numero: '))
C = int(input('Insira um terceiro numero: '))

if A > B and C:
    print('O numero {} é o maior!' .format(A))
elif A < B > C:
    print('O numero {} é o maior!' .format(B))
else:
    print('O numero {} é o maior!' .format(C))

if A < B and C:
    print("O numero {} é o menor!" .format(A))
elif A > B < C:
    print("O numero {} é o menor!" .format(B))
else:
    print("O numero {} é menor!" .format(C))
