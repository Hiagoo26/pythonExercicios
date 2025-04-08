#Validação de dados
s = str(input('Digite seu sexo: ')).upper()
while s != 'M' and s != 'F':
       s = str(input('Digite um valido: ')).upper()
print('Validado')

#While sexo not in 'MmFf'