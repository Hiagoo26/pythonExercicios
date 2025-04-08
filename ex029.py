#velocidade
km = int(input('A quantos km por hora você estava andando? '))
if km > 80:
    print('Você foi multado em {}R$' .format((km - 80) * 7))
else:
    print('Você está andando no limite!')
