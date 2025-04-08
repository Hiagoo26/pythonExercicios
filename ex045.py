#jokenpô
import random
import time
print('Vamos jogar jokenpô!!!')
escolha = int(input('Escolha entre pedra: 1, papel: 2 ou tesoura: 3:'))

ppt = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0,2) + 1
print('JO\n'
      'KEN\n'
      'PÔ')
time.sleep(3)
if escolha == computador:
    print('Deu empate! hehehe')
elif escolha == 1 != computador == 2:
    print('Eu ganhei! HAHAHA pois você jogou pedra e eu papel')
elif escolha == 1 != computador == 3:
    print('Você ganhou, parabens... você jogou pedra e eu tesoura')
elif escolha == 2 != computador == 1:
    print('Você ganhou, parabens... você jogou papel e eu pedra')
elif escolha == 2 != computador == 3:
    print('Eu ganhei! HAHAHA pois você jogou papel e eu tesoura')
elif escolha == 3 != computador == 1:
    print('Eu ganhei! HAHAHA pois você jogou tesoura e eu pedra')
elif escolha == 3 != computador == 2:
    print('Você ganhou, parabens... você jogou tesoura e eu papel')
else:
    print('Você não escolheu nenhum tente denovo!')


