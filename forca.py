palavra = "escola"
limite_tentativas = len(palavra) + 5

letras_acertadas = []
for letra in palavra:
    letras_acertadas.append("_")

contador = 1
while(contador <= limite_tentativas):
    print(letras_acertadas)
    print("Tentativas: ", contador, "/", limite_tentativas)
    chute = input("Digite a letra: ")
    
    indice = 0

    for letra in palavra:
        if chute == letra:
            letras_acertadas[indice] = chute
        indice = indice + 1

    contador = contador + 1

if "_" in letras_acertadas:  # Caso as tentativas acabem e a palavra não tenha sido totalmente descoberta
    print("Fim de jogo! Você não acertou todas as letras.")