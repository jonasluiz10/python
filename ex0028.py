from time import sleep
numero = int(input('Digite um numero: '))
from random import choice
lista  = [0, 1, 2, 3, 4, 5]
escolhido = choice(lista)
print('PROCESSANDO...')
sleep(1)
if numero == escolhido:
    print('você acertou Parabéns! ')
else:
    print('Você errou! quem sabe na próxima vez. ')