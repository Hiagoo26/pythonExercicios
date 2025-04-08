#Desconto
produto = float(input('Insira o valor do produto: R$ '))
conta = 5 / 100 * produto  #ou produto - (5 / 100 * produto)
desconto = produto - conta
print('O valor do produto com 5% de desconto é: R${:.2f} '.format(desconto))
