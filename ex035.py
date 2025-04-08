#Analisador de triangulo 1.0
linha1 = float(input('Qual o comprimento da primeira linha: '))
linha2 = float(input('Qual o comprimento da segunda linha: '))
linha3 = float(input('Qual o comprimento da terceira linha: '))
if linha1 == linha2 == linha3:
    print('O triangulo se forma de maneira correta! ')
elif linha1 != linha2 == linha3 or linha3 != linha1 == linha2 or linha2 != linha3 == linha1:
    print('O triangulo não se forma pois 1 linha é diferente!')
else:
    print('O triangulo não se forma pois as 3 linhas são diferentes!')