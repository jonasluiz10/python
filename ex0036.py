ano = 12
print('Emprestimo ')
casa = float(input('Qual o valor da casa que voçê deseja adquirir: '))
sal = float(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos voçê deseja quitar o imovel? '))
prest = casa / (anos*ano)
print('A prestação será de R${} '.format(prest))
if prest >= ((sal/100)*30):
    print('Emprestimo negado')
else:
    print('Emprestimo Aprovado')

