arvore_exemplo = {
    "Avô":    ["Pai", "Tio"],
    "Pai":    ["Filho1", "Filho2"],
    "Tio":    ["Primo"],
    "Filho1": [],
    "Filho2": [],
    "Primo":  [],
}

def descendentes(arvore, raiz):
    filhos = arvore.get(raiz, [])
    return filhos + [d for filho in filhos for d in descendentes(arvore, filho)]

print(descendentes(arvore_exemplo, "Avô"))