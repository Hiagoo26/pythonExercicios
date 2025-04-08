#Maior e menor
n = int(input('Insira um numero: '))
r = 'S'
maior = n
menor = n
soma = n
contador = 1
while r == 'S':
    n = int(input('Insira outro numero: '))
    r = str(input('Quer continuar? S/N: ')).upper()
    soma += n
    contador += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
media = soma / contador
print('A media é de {:.2f}, o maior é {} e o menor é {}' .format(media, maior, menor))
