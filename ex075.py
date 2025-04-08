#Análise de dados

num = tuple(int(input('Digite um numero:')) for i in range(4))
print(num)

print(num.count(9))#quantos 9 tem
print(num.index(3))#primeira posição do 3

par = [i for i in num if i % 2 == 0] #Lista q armazena numeros pares
print(par)#Lista de pares