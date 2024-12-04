import math

# Função para gerar uma lista de números primos até um limite n
def crivo_de_eratostenes(n):
    eh_primo = [True] * (n + 1)
    eh_primo[0] = False
    eh_primo[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if eh_primo[i]:
            for j in range(i * i, n + 1, i):
                eh_primo[j] = False

    return [i for i in range(2, n + 1) if eh_primo[i]]

# Função para verificar a Conjectura de Goldbach
def conjectura_de_goldbach(P):
    if P < 4 or P % 2 != 0:
        return -1

    primos = crivo_de_eratostenes(P)

    for p1 in primos:
        for p2 in primos:
            if p1 + p2 == P:
                return (min(p1, p2), max(p1, p2))

    return -1

# Função interativa
def main():
    print("=== Verificação da Conjectura de Goldbach ===")
    while True:
        try:
            entrada = input("Digite um número par maior ou igual a 4 (ou 'sair' para encerrar): \n").strip().lower()
            if entrada == 'sair':
                print("Encerrando o programa. Até mais!")
                break

            P = int(entrada)

            if P < 4 or P % 2 != 0:
                print("Por favor, insira um número par maior ou igual a 4.")
            else:
                resultado = conjectura_de_goldbach(P)
                if resultado == -1:
                    print(f"A conjectura de Goldbach é *falsa* para {P}.")
                else:
                    print(f"A conjectura de Goldbach é *verdadeira* para {P}.")
                    print(f"Os números primos que somam {P} são: {resultado[0]} e {resultado[1]}\n ")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido ou 'sair'.\n")

# Executa o programa
if __name__ == "__main__":
    main()
