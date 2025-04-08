#Numero por extenso
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito' , 'nove' ,'dez', 'onze' ,'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenovo', 'vinte')
n = int(input('Insira um numero de 0 a 20: '))
while n < 0 or n > 20:
    n = int(input('Insira um numero entre 0 a 20: '))
    for i in extenso:
        if n == 1:
            print(extenso[i])
        
for i in range(0 , len(extenso)):
   if n == i:
       print(extenso[i])
    
    