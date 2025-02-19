import random
sorteio = random.randint (1, 10)
chute = "5"
print( "### Seja muito bem vinda! ###")
print("Adivinhe o número secreto de 1 a 10")
chute = int (input("Digite um número aqui: "))
print ("Chute", chute)

limite_tentativas = 3
tentativa = 1
while (limite_tentativas >= tentativa):
    print ("Tentativa", tentativa)
    chute = int (input ("Digite seu chute: "))
    if (chute == sorteio):
        print ("Parabéns,você acertou!")
    elif (chute > sorteio):
        print ("Chute um número menor!")
    elif (chute < sorteio):
        print ("Chute um número maior!")
    tentativa = tentativa + 1