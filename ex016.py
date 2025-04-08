#quebra numero
from math import trunc
num = float(input('Digite um numero: '))
total = trunc(num)
print('O numero {} tem a parte inteira {}' .format(num, total))

### Outra forma

num = float(input('Digite um numero: '))
print('O valor digitado foi {} e a parte inteira é {}' .format(num, int(num)))