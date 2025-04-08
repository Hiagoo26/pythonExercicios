#Fibonacci
n = int(input('Ate qual numero da sequencia de Fibonacci você quer ver: '))
numant = 0
numsup = 1
contador = 0
while contador < n:
    print(numant)
    prox = numant + numsup
    numant = numsup
    numsup = prox
    contador += 1