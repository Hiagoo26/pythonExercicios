#Detector de palindromo
frase = str(input('Digite uma frase: '))
palavra = frase.split()
j = ''.join(palavra)
invertido = ''
for i in range(len(j) -1, -1, -1):
    invertido += j[i]
print(invertido)
if invertido == j:
    print('É um palindromo')
else:
    print('Não é palindromo')

