print(' ===== DESAFIO 036 =====')
c = float(input('Valor da casa: R$'))
s = float(input('Sálario do comprador: R$'))
t = int(input('Quantos anos de financiamento? '))
p = (c / t) / 12
print(f'Parar pagar uma casa de R${c:.2f} em {t} anos a prestação será de R${p:.2f}')
if p <= ((s * 30) / 100):
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')