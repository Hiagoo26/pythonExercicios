#cateto e hipotenusa
import math #ou from math import hypot
catOposto = float(input('Qual o comprimento do cateto oposto: '))
catAdjacente = float(input('Qual o comprimento do cateto adjacente: '))
total = math.hypot(catOposto,catAdjacente)
# outra forma: total = (catOposto ** 2 + catAdjacente ** 2) ** (1/2)
print('A hipotenusa é {:.2f}' .format(total))