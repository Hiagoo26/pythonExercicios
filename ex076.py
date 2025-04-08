#Lista de preço
produtos = ('Carro', 15.00, 'Boneca', 10.50, 'Uno', 25.50 )
print('Lista de Brinquedos')
for i in range(0, len(produtos), 2):
    print(produtos[i] + f' R${produtos[i+1]:.2f}')