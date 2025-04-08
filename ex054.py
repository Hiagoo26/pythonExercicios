#Grupo da Maioridade
from datetime import date
ano = date.today().year
for i in range(1,8):
    p = int(input('Qual o ano: '))
    if  ano - i < 18:
        print('Essa pessoa é menor de idade')
    else:
        print('Essa pessoa é maior de idade')
