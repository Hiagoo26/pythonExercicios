#Alistamento Militar
from datetime import date
ano = int(input('Em que ano você nasceu: '))
anohj = date.today().year
alist = anohj - ano
max = 18 - alist
min = alist - 18
if alist < 18:
    print('Você ainda não precisa se alistar! Pois ainda tem {} anos, faltam {} anos'  .format(alist, max))
    anoalif = anohj + max
    print('Seu alistamento será em {}' .format(anoalif))
elif alist == 18:
    print('Você precisa se alistar! Pois tem {} anos!' .format(alist))
else:
    print('Ja passou da hora de você se alistar!!! Pois já tem {} anos! ja se passaram {} anos e você ainda não foi' .format(alist, min))
    anolip = anohj - min
    print('Seu alistamento foi em {}' .format(anolip))


