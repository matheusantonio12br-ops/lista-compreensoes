def contar_vogais(texto):
    return sum(1 for c in texto.lower() if c in "aeiouáéíóúàèìòùãõâêîôûü")

print(contar_vogais("Hello World"))