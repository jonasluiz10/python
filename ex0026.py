frase = str(input('digite uma frase')).strip()
fr = frase.lower().count('a')
print(fr)
print('A primeira letra aparece na posição {}'.format(frase.find('a')+1))
print('A última letra aparece na posição {}'.format(frase.rfind('a')+1))


