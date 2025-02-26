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