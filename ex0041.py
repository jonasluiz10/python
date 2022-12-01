dat = 2022
print('Cofederação nacional de natação')
ano = int(input('Digite o ano em que você nasceu: '))
idade = dat - ano
print('O atleta tem {} anos '.format(idade))
if idade <= 9:
    print ('Categoria Mirim ')
elif idade <= 14:
    print ('Categoria Infantil ')
elif idade <= 19:
    print ('Categoria Junior ')
elif idade <= 25:
    print ('Categoria Senior ')
else:
    print ('Categoria Master ')