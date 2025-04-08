#trabalho
import random
a1 = input('Qual o nome: ')
a2 = input('Qual o nome: ')
a3 = input('Qual o nome: ')
a4 = input('Qual o nome: ')
nomes = [a1, a2, a3, a4]
random.shuffle(nomes)
print('A ordem de apresentação é: {}' .format(nomes))
