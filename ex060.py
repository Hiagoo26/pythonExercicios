#Calculo fatorial
#import math

#n = int(input('Digite um numero: '))
#r = math.factorial(n)
#print(r)

n = int(input('Digite um numero para calcular o fatorial: '))
multi = 1 
while n > 0:
    multi *= n
    n -= 1
print(multi)