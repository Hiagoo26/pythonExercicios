#Jogo de adivinhar 1.0
import random
from time import sleep
print('Vou escolher um numero de 0 a 5!')
aleatorio = int(input('Escolha um numero de 0 a 5: '))
num = random.randrange(0, 5)
#sleep(3)
if num == aleatorio:
    print('Você acertou!')
else:
    print('Você errou!')