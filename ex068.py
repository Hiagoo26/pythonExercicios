#Par ou impar
import random

print('Vamos jogar par ou impar! ')
v = 0
while True:
    nj = int(input('Digite um numero: '))
    ip = str(input('P ou I: ')).strip().lower()

    nc = random.randint(0, 10)
    t = nj + nc
    r = 'par' if t % 2 == 0 else 'impar'
    print(t)

    if (r == 'par' and ip == 'p') or (r == 'impar' and ip == 'i'):
        print('Você ganhou! Vamos denovo! ')
        v += 1
    else:
        print('Ganhei, HAHAHAHAHA')
        break
print (f'Uau, você ganhou {v} vezes antes de perder! ')

    