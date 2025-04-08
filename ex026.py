#26 o melhor, primeira e ultima recorencia de uma string
frase = str(input('Insira uma frase:')).strip().lower()
cores = {'roxo':'\033[35m', 'vermelho': '\033[41m'}
print('A letra A aparece: {}{}{} ' .format(cores ['roxo'],frase.count('a'),'\033[m'))
print('A letra A aparece pela primeira vez na posição: {}{}{}' .format(cores ['roxo'],frase.find('a') + 1,'\033[m'))
print('A ultima letra A aparece na posição: {}{}{}' .format(cores ['roxo'],frase.rfind('a')+1,'\033[m'))
print('\033[1;35;40mEU TE AMO NATALY')