import math

# Função para gerar uma lista de números primos até um limite n
def crivo_de_eratostenes(n):
    
    eh_primo = [True] * (n + 1)
    eh_primo[0] = False
    eh_primo[1] = False
    
    # Mapeia os numeros compostos
    for i in range(2, int(math.sqrt(n)) + 1):
        if eh_primo[i]:
            for j in range(i * i, n + 1, i):
                eh_primo[j] = False
    
    # Cria uma lista com todos os números que são primos
    primos = []
    for i in range(2, n + 1):
        if eh_primo[i]:
            primos.append(i)
    
    return primos

# Função para verificar a Conjectura de Goldbach
def conjectura_de_goldbach(P):
    
    if P < 4 or P % 2 != 0:
        return -1
    
    # Gera a lista de números primos até P
    primos = crivo_de_eratostenes(P)
    
    # Testa todas as combinações possíveis de dois números primos
    for p1 in primos:
        for p2 in primos:
            if p1 + p2 == P:  # Verifica se a soma é igual a P
                return (min(p1, p2), max(p1, p2))  # Retorna os valores em ordem crescente
    

    return -1
