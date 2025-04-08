#Aluguel carro
aluguelDiaria = int(input('Quantos dia de aluguel: '))
kmRodados = float(input('Quantos Km rodados: '))
diaria = 60 * aluguelDiaria
km = 0.15 * kmRodados
total = diaria + km
print('O Total de dias foi de {}, o total de km foi de {}, então preço do aluguel é de R${:.2f}' .format(aluguelDiaria, kmRodados, total))

