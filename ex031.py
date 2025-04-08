#custo viagem
distancia = int(input('Qual a distancia em Km da sua viagem? '))
if distancia <= 200:
    preço1 = float(distancia * 0.50)
    print('O total cobrado sera de {}R$' .format(preço1))
else:
    preço2 = float(distancia * 0.45)
    print(('O total cobrado sera de {:.2f}R$' .format(preço2)))