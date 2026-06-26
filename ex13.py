def pares_da_matriz(matriz):
    return [n for linha in matriz for n in linha if n % 2 == 0]

print(pares_da_matriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))