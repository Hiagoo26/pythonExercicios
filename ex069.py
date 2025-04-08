#Analise de dados de um grupo

idade = int(input('Digite a idade: '))
sexo = str(input('Digite o sexo (M/F): ')).strip().upper()
while sexo != 'Mm' and 'Ff':
    print('Sexo invalido tente denovo')
    sexo = str(input('Digite o sexo (M/F): '))
maioridade = 0
homens = 0
mulhermenorvinte = 0
if idade >= 18:
        maioridade += 1
if sexo == 'M':
        homens += 1
if sexo == 'F' and idade < 20:
        mulhermenorvinte += 1
while True:
    continuar = str(input('Quer continuar? (S/N): ')).upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        idade = int(input('Digite outra idade: '))
        sexo = str(input('Digite outro sexo (M/F): ')).upper()
        while sexo != 'Mm' and 'Ff':
            print('Sexo invalido tente denovo')
        if idade >= 18:
            maioridade += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulhermenorvinte += 1
    else:
        print('Você escolheu uma opção invalida, tente denovo!')
print(f'A quantidade de pessoas com mais de 18 anos é {maioridade}\n A quantidade de homens é de {homens}\n A quantidade de mulheres com menos de 20 anos é {mulhermenorvinte}')
        
