#Analisador de triangulo 2.0
linha1 = float(input('Qual o comprimento da primeira linha: '))
linha2 = float(input('Qual o comprimento da segunda linha: '))
linha3 = float(input('Qual o comprimento da terceira linha: '))
if linha1 == linha2 == linha3:
    print('O triangulo é Equilátero! pois todos os lados são iguais! ')
elif linha1 != linha2 == linha3 or linha3 != linha1 == linha2 or linha2 != linha3 == linha1:
    print('O triangulo é Isósceles! pois tem 2 lados iguais!')
else:
    print('O triangulo é Escaleno! pois os 3 lados são diferentes!')