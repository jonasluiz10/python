print('Alistamento militar ')
print('''qual o seu genero ?
[1] Mulher
[2] Homem''')
opção = int(input('Digite uma opção'))
if opção == 1:
    print('Você não precisa se alistar')
elif opção == 2:
    nasc = int(input('Digite o ano em que voçê nasceu: '))
    idade = 2022 - nasc
    tempo1 = 18 - idade
    tempo2 = idade - 18
    ano = 2022 + tempo1
    ano1 = tempo2 - 2022
    if idade == 18:
        print('Voçê deve se alistar imediatamente! ')
    elif idade < 18:
        print('Voçê ainda não deve se alistar! Faltam {} anos. '.format(tempo1))
        print('você deverá se alistar no ano de {} '.format(ano))
    elif idade > 18:
        print ('Você já deveria ter se alistado! Já se passou {} anos '.format(tempo2))

        print('Você deveria ter se alistado no ano de {} '.format(ano1))
