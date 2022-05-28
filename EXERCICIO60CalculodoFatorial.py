n = int(input('digite um numero '))
f = 1
print(f'{n}! = ', end='')
while n > 1:
    if n == 0:
        f = 1
    elif n == 1:
        f = 1
    else:
        f = f * n
        n -= 1
print(f'o fatorial é {f}')