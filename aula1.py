import random
sorteio = random.randint (1, 10)
chute = "5"
print( "### Seja muito bem vinda! ###")
print("Adivinhe o número secreto de 1 a 10")
chute = int (input("Digite um número aqui: "))
print("Sorteio:", sorteio)
print ("Chute", chute)

if (chute == sorteio):
    print ("Parabéns, você acertou!")
else:
    print ("Está errado.")