#Gerenciador de pagamentos
produto = float(input('Insira o valor: '))
print('à vista: 1, à vista cartão: 2, 2x: 3, 3x ou mais: 4')
escolha = int(input('Escolha a forma de pagamento: '))
if escolha == 1:
    desc1 = produto * 10/100
    print('Vai ficar {}' .format(produto - desc1))
elif escolha == 2:
    desc2 = produto * 5/100
    print('Vai ficar: {}' .format(produto - desc2))
elif escolha == 3:
    print('O valor é normal: {} divido em duas parcelas é: {} ' .format(produto, produto / 2))
else:
    parcelas = int(input('Quantas parcelas?'))
    juros = 20/100 * produto
    print('O valor vai ficar {} com cada parcela sendo {}' .format(produto + juros, (produto + juros) / parcelas))