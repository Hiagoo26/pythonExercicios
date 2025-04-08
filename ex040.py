#Média
mediaum = float(input('Insira sua nota: '))
mediadois = float(input('Insira sua segunda nota: '))
média = (mediaum + mediadois) / 2
if média >= 7.0:
    print('Você passou! sua media foi {}' .format(média))
elif média >= 5.0:
    print('Você ficou de recuperação! sua media foi {}' .format(média))
else:
    print('Você foi reprovado! sua media foi {}' .format(média))
