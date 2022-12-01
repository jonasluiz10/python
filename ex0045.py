from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('-=' *11)
print('Computador jogou {}'.format(itens[pc]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' *11)
if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('jogador VENCE')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada invalida!')
elif pc == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('jogador VENCE')
    else:
        print('Jogada invalida!')
elif pc == 2:
    if jogador == 0:
        print('jogador VENCE')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida!')
