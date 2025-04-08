#Conversor de medidas
metro = float(input('Insira a quantidade de metros: '))
km = float(metro / 1000)
hm = float(metro / 100 )
dam = float(metro / 10)
cm = int(metro * 100)
mm = int(metro * 1000)
print('{} tem {}cm e {}mm\nTem {}km \nTem {}hm\nTem {}dam'.format(metro, cm, mm, km, hm, dam))
#Outra maneira é fazer o calculo no print no format: (metro, metro * 100, metro * 1000, metro / 1000, metro / 100, metro / 10