from datetime import date
menores = 0
maiores = 0
ano = date.today().year
for r in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {r}ª pessoa: '))
    if ano - nascimento < 21:
        menores += 1
    else:
        maiores += 1
print(f'Do total de 7 pessoas, {menores} são menores de idade, e {maiores} são maiores de idade.')