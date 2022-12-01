print('{:=^40}'.format('lojas Pague fácil '))
preco = float(input('preço das compras'))
print('''Escolha a forma de pagamento
[1] Dinheiro/Cheque
[2] avista no cartão
[3] 2x no cartão
[4] 3 ou mais vezes no cartão''')
opcao = int(input('digite sua opção: '))
if opcao == 1:
    total = preco - (preco/100)*10
elif opcao == 2:
    total = preco - (preco/100)*5
elif opcao == 3:
    total = preco
    parcela = total/2
    print('Sua compra será parcelada em 2x de {:.2f} sem juros '.format(parcela))
elif opcao == 4:
    total = preco + (preco/100)*20
    div = int(input('Em quantas vezes você quer parcelar? '))
    parcela4 = (total/div)
    print('Sua compra será parcelada em {}x de R${:.2f} '.format(div, parcela4))
else:
    total = preco
    print('Opção invalida... Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(preco, total))

