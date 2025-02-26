import random

print ("1- Nível Fácil")
print ("2- Nível Médio")
print ("3- Nível Difícil")

opcao = int(input("Digite a opção desejada:"))

if (opcao == 1):
    print("Você escolheu o Nível Fácil")
    numero_max = 10
    limite_tentativas = 5
elif (opcao == 2):
    print("Você escolheu o Nível Médio")
    numero_max = 20
    limite_tentativas = 8
elif (opcao == 3):
    print("Você escolheu o Nível Difícil")
    numero_max = 50
    limite_tentativas = 3
else:
    print("Opção inválida")
    exit()

sorteio = random.randint(1, numero_max)

print("### JOGO DA ADIVINHAÇÃO ###")
print("Adivinhe o número que estou pensando, de 1 a ", numero_max)
tentativa = 1

while (limite_tentativas >= tentativa):
    print("Tentativa", tentativa)
    chute = int(input("Digite o seu chute:"))
    if (chute == sorteio):
        print("Parabéns, você acertou!")
        break
    elif (chute > sorteio):
        print("Chute um número menor!")
    elif (chute < sorteio):
        print("Chute um número maior!")
    tentativa = tentativa + 1

print("O número sorteado era: ##", sorteio)
print("### FIM DO JOGO ###")