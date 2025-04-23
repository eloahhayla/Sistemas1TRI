import random

# Carrega palavras diretamente dos arquivos
def carregar_palavras(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return [linha.strip() for linha in arquivo]

# Mapear temas aos arquivos
temas = {
    "animais": "animal.txt",
    "animes": "anime.txt",
    "jogos": "jogo.txt"
}

# Escolha do tema
print("Escolha um tema: animais, animes, jogos")
tema = input("Digite o tema: ").lower()

if tema not in temas:
    print("Tema inválido!")
    exit()

palavras = carregar_palavras(temas[tema])
palavra = random.choice(palavras)
letras_acertadas = ["_" for _ in palavra]
tentativas = len(palavra) + 5

# Jogo principal
for tentativa in range(1, tentativas + 1):
    print(letras_acertadas)
    print(f"Tentativa: {tentativa}/{tentativas}")
    letra = input("Digite uma letra: ").lower()

    if letra in palavra:
        for i, l in enumerate(palavra):
            if letra == l:
                letras_acertadas[i] = letra

    if "_" not in letras_acertadas:
        print("Você venceu! ٩(ˊᗜˋ*)و")
        print("Palavra:", "".join(letras_acertadas))
        break

if "_" in letras_acertadas:
    print("Você perdeu! ૮(˶╥︿╥)ა")
    print("A palavra era:", palavra)