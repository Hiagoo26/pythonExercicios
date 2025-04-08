#Tupla aleatoria com maior e menor
import random
num = tuple(random.randrange(0, 10) for i in range(5))
print(num)
print('Maior:', max(num))
print('Menor:', min(num))