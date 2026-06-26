def palavras_longas(nomes):
    return [nome for nome in nomes if len(nome) > 5]

print(palavras_longas(["Ana", "Carlos", "Beatriz", "Jo", "Fernando", "Bia"]))