def acima_da_media(notas, media=5):
    return sum(1 for nota in notas if nota > media)

print(acima_da_media([3, 7, 5, 8, 4, 6, 9, 2]))