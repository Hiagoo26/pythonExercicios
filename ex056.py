#Analisador completo
somai = 0
mediai = 0
mais20 = 0
for i in range(1,6):
    nome = str(input('Qual seu nome: '))
    idade = int(input('Qual sua idade: '))
    print('0 = Feminino, 1 = Masculino:')
    sexo = int(input('Qual seu sexo: '))
    somai += idade
    if i == 1 and sexo == 1:
        velho = idade
        velhon = nome
    if sexo == 1 and idade > velho:
        velho = idade
        velhon = nome
    if sexo == 0 and idade < 20:
        mais20 += 1

mediai = somai / 5
print('A media de idade do grupo é de {:.1f} anos' .format(mediai)) 
print('O Homem mais velho é {}' .format(velhon))
print('A quantidade de mulheres com menos de 20 anos é {}' .format(mais20))
