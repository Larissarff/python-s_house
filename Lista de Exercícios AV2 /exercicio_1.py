import math

def crivo_de_eratostenes(n):
    
    eh_primo = [True] * (n + 1)
    eh_primo[0] = eh_primo[1] = False  
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if eh_primo[i]:
            for j in range(i * i, n + 1, i):
                eh_primo[j] = False

    # Retorna a lista de primos encontrados
    primos = [i for i in range(2, n + 1) if eh_primo[i]]
    return primos



def conjectura_de_goldbach(P):
    if P < 4 or P % 2 != 0:
        return -1  
 
    primos = crivo_de_eratostenes(P)

    for p1 in primos:
        p2 = P - p1
        if p2 in primos:
            
            return (min(p1, p2), max(p1, p2))

    return -1  
