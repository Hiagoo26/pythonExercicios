#Contador de Vogais
palavras = ('Arroz', 'Frango', 'Salada', 'Ovo')

for i in palavras:
    vogais = 0
    for vogal in i.lower():
        if vogal in 'aeiou':
            vogais += 1
    print(f'{i} = {vogais} vogais')
