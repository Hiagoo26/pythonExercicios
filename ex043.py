#IMC
peso = float(input('Qual seu peso?'))
altura = float(input('Qual sua altura?'))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Peso abaixo: {:.2f}' .format(imc))
elif imc < 25:
    print('Peso ideal: {:.2f}' .format(imc))
elif imc < 30:
    print('Sobrepeso: {:.2f}' .format(imc))
elif imc < 40:
    print('Obesidade: {:.2f}' .format(imc))
else:
    print('Obesidade mórbida: {:.2f}' .format(imc))