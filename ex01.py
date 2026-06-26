def ler_inteiros():
    linha = input("Digite números inteiros separados por espaço: ")
    return [int(x) for x in linha.split()]

print(ler_inteiros())