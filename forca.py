import random

# Configuração inicial das variáveis
palavras = ["cacau", "estojo", "professor", "cachorro", "militar", "toby", "pingo"]
palavra = random.choice(palavras)
limite_tentativas = len(palavra) + 5
acertou = False # Ainda não ganhou
enforcou = False # Ainda não perdeu

# Seleciona palavra aleatória
letras_acertadas = []
for letra in palavra:
    letras_acertadas.append("_") # Preenche com "_"

contador = 1
while(not acertou and not enforcou): # Loop do jogo
    print(letras_acertadas) # Mostra progresso
    print("Tentativas: ", contador, "/", limite_tentativas)
    chute = input("Digite a letra: ") # Solicita chute
    
    indice = 0

    for letra in palavra:
        if chute == letra:
            letras_acertadas[indice] = chute # Atualiza acertos
        indice = indice + 1

    if contador == limite_tentativas:
        enforcou = True # Jogador perdeu
        print("Você perdeu ૮(˶╥︿╥)ა \n A palavra era: ", palavra)


    if letras_acertadas.count("_") == 0:
        acertou = True # Jogador venceu
        print("Parabéns, você encontrou a palavra secreta! ٩(ˊᗜˋ*)و")
        print(letras_acertadas)



    contador = contador + 1 # Incrementa tentativas