#Primeiro e ultimo nome
nome = str(input('Insira o seu nome completo: ')).strip()
nomes = nome.split()
print('Primeiro nome: {}' .format(nomes[0]))
print('Último nome: {}' .format(nomes[len(nomes) -1]))
