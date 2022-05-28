n = int(input('Digite o número do qual gostaria de saber a tabuada:  '))
l = int(input('Digite até que linha gostaria de ter essa tabuada:  '))

for c in range(0,l+1):
    print("\n{ } x { } = { }".format(n,c,n*c))
    c = c+1
print(c)