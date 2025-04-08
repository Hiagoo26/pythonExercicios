#Conversor de moeda
din = float(input('Insira a quantidade de dinheiro que você tem em sua carteira: R$'))
dolar = din / 5.66
euro = din / 6.12
won = din / 0.0041
print('Com essa quantidade R${} você pode comprar US${:.2f} dolares ou pode comprar €{:.2f} euros'.format(din, dolar, euro))
print('E tambem você pode comprar  ₩{:.2f}' .format(won))