#Menu
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('[1] para somar \n[2] para multiplicar \n[3] para saber o maior \n[4] para digitar novos numeros\n[5]sair ')
opção = int(input('Digite a opção: '))
while opção != 5:
    if opção == 1:
        soma = n1 + n2
        print('Total = {}' .format(soma))
    if opção == 2:
        multi = n1 * n2
        print('Total = {}' .format(multi))
    if opção == 3:
        if n1 > n2:
            print('O numero {} é maior que o {}' .format(n1, n2))
        else:
            print('O numero {} é maior que o {}' .format(n2,n1))
    if opção == 4:
        n1 = int(input('Digite outro numero então: '))
        n2 = int(input('Digite mais outro numero: '))
    opção = int(input('Digite outra opção: '))
print('Fechado!')