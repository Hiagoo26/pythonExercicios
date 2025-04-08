#Brasileirão
colocação = ('Corinthians', 'Internacional', 'Ceará SC', 'Fortaleza', 'Botafogo',
             'Flamengo', 'Palmeiras', 'Juventude', 'Fluminense', 'Grêmio', 'Vasco da Gama',
             'Cruzeiro', 'Bahia', 'São Paulo', 'Bragantino', 'Santos', 'Mirassol',
             'Sport Recife', 'Atlético-MG', 'Vítoria')

print('\033[4;32mOs 5 primeiros: \033[m')
for i in range(0, len(colocação)):
    if i <= 4:
        print(colocação[i])

print('\033[4;31mOs 4 ultimos: \033[m')
for f in range(0, len(colocação)):
    if f >= 16:
        print(colocação[f])

print('\033[4mOrdem Alfabética: \033[m')
print(sorted(colocação))

print('\033[4;35m Posição do Corinthians: \033[m')
print(colocação.index('Corinthians') + 1)
