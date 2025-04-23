palavras = []
arquivo = open("anime.txt", "r")
for linha in arquivo:
    palavras.append(linha.strip())

print(palavras)