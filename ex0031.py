viagem = float(input('digite a distâcia da viagem: '))
print('a distancia da sua viagem é de {}km '.format(viagem))
pass200 = 0.50*viagem

if viagem <= 200:
    passagem = 0.50 * viagem
else:
    passagem = 0.45 * viagem
print('passagem cobrada será de R$ {:.2f} '.format(passagem))
