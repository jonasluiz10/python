from random import shuffle
al1 = str(input('digite o nome do primeiro aluno: '))
al2 = str(input('digite o nome do segundo aluno: '))
al3 = str(input('digite o nome do terceiro aluno: '))
al4 = str(input('digite o nome do quarto aluno: '))
lista = [al1, al2, al3, al4]
shuffle(lista)
print('a ordem de apresentação dos trabalhos será assim ')
print(lista)