#Sorteio item
import random

a1 = input('Qual o nome do 1º aluno: ')
a2 = input('Qual o nome do 2º aluno: ')
a3 = input('Qual o nome do 3º aluno: ')
a4 = input('Qual o nome do 4º aluno: ')
nomes = [a1, a2, a3, a4]
qual = random.choice(nomes)
print('O aluno escolhido foi: {} ' .format(qual))
