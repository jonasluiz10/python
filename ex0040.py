print('Calculo da média de um aluno ')
nota1 = float(input('digite a primeira nota!: '))
nota2 = float(input('digite a segunda nota!: '))
media = (nota1 + nota2)/2
if media < 5:
    print('Sua média foi {:.2f} Você está Reprovado! '.format(media))
elif media >=5 and media < 7:
    print('Sua média foi de {:.2f} Você está de Recuperação! '.format(media))
else:
    print('Sua média foi de {:.2f} Você está Aprovado! '.format(media))