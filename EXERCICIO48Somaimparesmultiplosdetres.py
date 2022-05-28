a = int(input('\033[1:30mPrimeiro Valor: \033[m'))
b = int(input('\033[1:30mSegundo Valor: \033[m'))
s = 0
contador = 0
for n in range (a,b+1):
    if n % 2 != 0 and n % 3 == 0:
        contador += 1
        s += n
print('\033[1:34mA Soma de {} valores impares multiplos de 3 de {} até {} é: {}\033[m'.format(contador,a,b,s))