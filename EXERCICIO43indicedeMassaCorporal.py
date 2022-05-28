altura = float(input('Qual é a altura: '))
peso = float(input('Qual é o peso: '))
IMC = peso / (altura)**2
print(f'IMC de {IMC:.1f} ')
if IMC < 18.5:
    print('Abaixo do Peso. ')
elif IMC > 18.5 and IMC < 25:
    print('Peso Ideal. ')
elif IMC > 25 and IMC < 30:
    print('Sobrepeso. ')
elif IMC > 30 and IMC < 40:
    print('Obesidade. ')
else:
    print('Obesidade Mórbida. ')