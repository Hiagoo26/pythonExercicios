#Pintando parede
largura = float(input('Qual a largura da sua parede: '))
altura = float(input('Qual a altura da sua parede: '))
area = altura * largura
litrosTinta = area / 2
print('Para um area de {}m² será preciso de {}l de tinta.' .format(area, litrosTinta))
