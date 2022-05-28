termo = float(input('Informe o 1° termo da PA:  '))
razão = int(input('Informe a razão da PA: '))
print(f'{termo}:.0f', end=' -> ')
for c in range(0,10):
      termo += razão
      print(f'{termo:.0f}',end=' -> ')
print('ACABOU')