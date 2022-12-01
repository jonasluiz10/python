carro  = float(input('digite a velocidade do carro: '))
print('O veiculo está a {} km/h '.format(carro))
multa = float(carro - 80)*7.00

if carro >= 81:
    print('Você foi multado! Sua multa é de R${:.2f} '.format(multa))
else:
    print('Voçê está dentro da velocidade permitida, boa viagem! ')
