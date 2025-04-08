#Progreção 3.0
p = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
d = 0 
termos = 10
while d < termos:
    termo = p + d * r
    print(termo)
    d += 1
tq = int(input('Você deseja que mostre mais termos? Se sim quantos: '))
while tq > 0:
    termos += tq
    while d < termos:
        termo = p + d * r
        d += 1 
        print(termo)      
    tq = int(input('Você deseja que mostre mais termos? Se sim, quantos: ')) 
print('Fechado')





