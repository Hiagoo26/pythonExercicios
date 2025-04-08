#Conversor de Temperaturas
celcius = float(input('Informe a temperatura = ºC: '))
faren = celcius * 1.8 + 32  #Ou ((9*celcius)/5) + 32 ou fazer sem os ()
print('A quantidade de ºC{} em Fahrenheit é {:.1f}'.format(celcius, faren))
