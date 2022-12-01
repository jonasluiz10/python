num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para Binário
[2] converter para OCTAL 
[3] CONVERTER PARA HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O número {} convertido para Binário é igual a {} '.format(num, bin(num) [2:]))
elif opção == 2:
    print ('O número {} covertido para  Octal é igual a {} '.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para hexadecimal é igual a {} '.format(num, hex(num)[2:]))
else:
    print('Opção invalida! ')
