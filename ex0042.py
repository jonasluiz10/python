seg1 = float(input('Primeiro seguimento: '))
seg2 = float(input('Segundo seguimento: '))
seg3 = float(input('Terceiro seguimento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os seguimentos acima podem formar um triagulo ')
    if seg1 == seg2 == seg3:
        print('EQUILATERO')
    elif seg1 != seg2 != seg3 != seg1:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Os seguimentos acima não podem formar um triagulo ')