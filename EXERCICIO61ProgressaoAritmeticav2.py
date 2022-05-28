pt = int(input('Digite o 1° termo: '))
razao = int(input('Digite a razão: '))
c = 10
print(f'10 PRIMEIROS TERMOS:', end=' ')
while c > 0:
    print(f'{pt}', end=' ')
    pt = pt + razao
    c = c - 1