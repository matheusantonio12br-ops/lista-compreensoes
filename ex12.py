def extrair_letras(palavras):
    return [letra for palavra in palavras for letra in palavra]

print(extrair_letras(["python", "java"]))