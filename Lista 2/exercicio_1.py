import math


# Função para gerar números primos até 'n' usando o Crivo de Eratóstenes
def crivo_de_eratostenes(n):
    # Inicializa uma lista onde True significa que o número é primo
    eh_primo = [True] * (n + 1)
    eh_primo[0] = eh_primo[1] = False  # 0 e 1 não são primos

    # Algoritmo do Crivo de Eratóstenes
    for i in range(2, int(math.sqrt(n)) + 1):
        if eh_primo[i]:
            for j in range(i * i, n + 1, i):
                eh_primo[j] = False

    # Retorna a lista de primos encontrados
    primos = [i for i in range(2, n + 1) if eh_primo[i]]
    return primos


# Função para encontrar dois primos cuja soma seja igual a P
def conjectura_de_goldbach(P):
    if P < 4 or P % 2 != 0:
        return -1  # A conjectura só é válida para números pares maiores ou iguais a 4

    # Gerar lista de primos até P
    primos = crivo_de_eratostenes(P)

    # Procurar dois primos cuja soma seja igual a P
    for p1 in primos:
        p2 = P - p1
        if p2 in primos:
            # Retorna os primos em ordem crescente
            return (min(p1, p2), max(p1, p2))

    return -1  # Caso não encontre nenhuma combinação válida


# Exemplo de uso:
P = int(input("Digite um número par P: "))
resultado = conjectura_de_goldbach(P)
if resultado == -1:
    print("A conjectura de Goldbach falhou!")
else:
    print(f"Dois números primos cuja soma é {P}: {resultado[0]} e {resultado[1]}")
