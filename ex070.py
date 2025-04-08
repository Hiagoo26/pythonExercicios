#Estatísticas em produtos
produto = str(input('Insira o nome do produto: '))
rs = float(input('Insira o valor: R$ '))
total = rs
mil = 0
if rs >= 1000:
    mil += 1
pbarato = produto
brs = rs
while True:
    continuar = str(input('Quer continuar S/N: ')).strip().upper()
    if continuar == 'N':
        break
    produto = str(input('Insira o nome do produto: '))
    rs = float(input('Insira o valor: R$ '))
    if rs >= 1000:
        mil += 1
    if rs < brs:
        pbarato = produto
        brs = rs
    total += rs
print(f'O valor foi de {total:.2f} \nForam {mil} produtos que custaram 1000R$ ou mais\nO produto mais barato foi {pbarato} ')
    
