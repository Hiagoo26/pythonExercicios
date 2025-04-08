#Adivinhação 2.0 (já teve 1)
import random
print('Vou escolher um numero entre 0 e 10, ADIVINHE!')
num = random.randrange(0, 10)
r = int(input('Escolha um numero: '))
if r > num:
     print('Quase! Tente um numero menor')
else:
     print('Tente um numero maior!')
contador = 0
while r != num:
    r = int(input('ERROUUUU, tente denovo: '))
    if r > num:
        print('Quase! Tente um numero menor')
    else:
        print('Tente um numero maior!')
    contador += 1
    
print('Parabens o numero é {} !!! Você acertou após {} tentativas!' .format(num ,contador))


#Tem como fazer uma variavel com false, e fazer while not ai se o jogador aceitar essa variavel fica TRUE
#Acho q é ate mais facil do jeito que eu fiz
#Adicionei um if e else pra ajudar o jogador