dias = int(input('quantos dias alugado?: '))
km = float(input('quantos quilometros rodados?: '))
pg = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pg))