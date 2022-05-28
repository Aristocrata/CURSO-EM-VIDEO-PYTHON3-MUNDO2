while True:
    n = int(input("Insira um número para ver sua tabuada. "))
    for c in range(1, 11):
        print(f"{n} x {c} = {n*c}")
    p = str(input("Deseja ver alguma outra tabuada? (Y / N)")).upper().strip()

    if p == "Y":
        pass
    elif p =="N":
        break
    else:
        p = str(input("Dados inváilidos responda: (Y / N)")).upper().strip()