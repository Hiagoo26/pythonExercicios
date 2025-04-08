#Progreção aritimetica
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
for n in range(p, d + r, r):
    print(n)