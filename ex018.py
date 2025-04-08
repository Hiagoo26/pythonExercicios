#seno, cosseno e tangente
import math

angulo = int(input('Insira o ângulo: '))
totalSen = math.sin(math.radians(angulo))
totalCos = math.cos(math.radians(angulo))
totalTan = math.tan(math.radians(angulo))
print('O seno do angulo {} é de {:.2f}\nO cosseno é {:.2f}\nE a tangente é {:.2f}'.format(angulo, totalSen, totalCos, totalTan))
