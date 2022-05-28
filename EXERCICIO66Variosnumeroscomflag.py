v = sm = nv = 0
while v != 999:
    v = int(input("Digite um valor: "))
    if v != 999:
        sm += v
        nv += 1
print(f"O total de valores digitados foi de {nv}")
print(f"E a soma entre eles deu {sm}")