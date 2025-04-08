#Analisador de Textos
nomecom = str(input('Digite seu nome completo:')).strip()
print(nomecom.upper())
print(nomecom.casefold()) #ou lower() tem os 2 jeitos
print(len(nomecom) - nomecom.count(' '))
totalPN = nomecom.split()[0]
print(len(totalPN))
print(nomecom.find(' '))
