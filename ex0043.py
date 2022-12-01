
print('Caluco IMC ')
alt = float(input('Por favor me diga a sua altura: '))
peso = float(input('Por favor me diga a seu peso: '))
imc = peso/(alt ** 2)
print('{:.2f} '.format(imc))
if imc < 18.5:
    print('Abaixo do peso ')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal ')
elif imc >= 25 and imc < 30:
    print('Sobrepeso ')
elif imc >= 30 and imc < 40:
    print('Obesidade ')
else:
    print('Obesidade Mórbida ')
