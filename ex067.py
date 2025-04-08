#Tabuda 3.0
while True:
    n = int(input('Digite outro numero para eu fazer a tabuada: '))
    if n < 0:
        break
    for i in range(10):
        print(n * (i + 1))
print('Acabou!')




 