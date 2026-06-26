def achatar(lst):
    resultado = []
    for item in lst:
        if isinstance(item, list):
            resultado.extend(achatar(item))
        else:
            resultado.append(item)
    return resultado

def achatar_comp(lst):
    return [n for item in lst for n in (achatar_comp(item) if isinstance(item, list) else [item])]

lista = [1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]
print(achatar(lista))
print(achatar_comp(lista))