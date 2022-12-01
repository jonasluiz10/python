sal = float(input('digite o valor do salário: '))
if sal >= 1250:
    aum = ((sal / 100)*10) + sal
else:
    aum = ((sal / 100) * 15) + sal
print('Seu novo salário é de R$ {:.2f} '.format(aum))

