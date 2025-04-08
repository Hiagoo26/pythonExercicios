#Classificando Atletas
from datetime import date
ano = int(input('Em que ano você nasceu: '))
anohj = date.today().year
categoria = anohj - ano
if categoria <= 9:
    print('Categoria mirim!')
elif categoria <= 14:
    print('Categoria infantil!')
elif categoria <= 19:
    print('Categoria junior!')
elif categoria == 20:
    print('Categoria sênior!')
else:
    print('Categoria master!')
