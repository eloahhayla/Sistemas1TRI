custos = [500, 324, 100, 500]
ganhos = [2400, 5]

def somatoria(lista):
    contador = 0
    soma = 0
    while (contador < len(lista)):
        soma = soma + lista[contador]
        contador = contador + 1
    return soma

somacusto = somatoria(custos)
print ("Soma dos custos:" , somacusto)

somaganhos = somatoria(ganhos)
print ("Soma dos ganhos:" , somaganhos)

print ("Saldo final:" , somaganhos - somacusto)