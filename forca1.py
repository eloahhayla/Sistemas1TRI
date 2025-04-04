palavra = "escola"
limite_tentativas = len(palavra) + 5

letras_acertadas = ["_" for _ in palavra]

contador = 1
while contador <= limite_tentativas:
    print(" ".join(letras_acertadas))
    print(f"Tentativas: {contador}/{limite_tentativas}")

    if "_" not in letras_acertadas:  # Se todas as letras forem descobertas, encerra o jogo
        print("Parabéns! Você acertou todas as letras!")
        break

    chute = input("Digite uma letra: ")

    if chute in palavra:  # Apenas verifica se a letra está na palavra antes de atualizar
        for indice, letra in enumerate(palavra):
            if chute == letra:
                letras_acertadas[indice] = chute

    contador += 1

if "_" in letras_acertadas:  # Se o limite for atingido e a palavra não estiver completa
    print("Fim de jogo! Você não acertou todas as letras.")