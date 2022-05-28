print("""Temos as seguintes funcionalidades:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")

funcao = 0

while funcao != 5:
    num1 = int(input('Digite o 1° número: '))
    num2 = int(input('Digite o 2° número: '))

    funcao = int(input('Escolha um das funcionalidades: '))

    if funcao == 1:
        print(f'A soma entre {num1} e {num2} é {num1 + num2}')
    elif funcao == 2:
        print(f'A multiplicação entre {num1} e {num2} é {num1 * num2}')
    elif funcao == 3:
        if num1 > num2:
            print(f'O maior entre {num1} e {num2} é {num1}')
        elif num2 > num1:
            print(f'O maior entre {num1} e {num2} é {num2} ')
        else:
            print('Os dois valores são iguais!')
    elif funcao == 4:
        print('Vamos reiniciar!')
    else:
        print('Digite valores válidos!')                                
print('Fim do programa!')