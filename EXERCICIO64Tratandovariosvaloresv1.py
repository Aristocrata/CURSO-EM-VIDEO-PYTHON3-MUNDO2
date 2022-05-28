num = soma = 0
digit = -1
while not num == 999:
    soma += num
    digit += 1
    num = int(input('Digite um número quaquer [Enter 999 to stop]: '))
print(f'Você digitou {digit} números e a soma entre eles é {soma}')