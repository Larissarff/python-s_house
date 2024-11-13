from typing import Union

def is_kaprekar(number: int) -> int:
    str_num : str = str(number)  # tratando de int para string pra separação
    tamanho : int = len(str_num)  # mapeando tamanho

    # Loop para dividir o número em duas partes
    for i in range(1, tamanho):
        # Arrumar um jeito de dividir no meio numero da string, se for ímpar, vai +1 pra esquerda

        If tamanho % 2 == 0:
            str_num.Split() = left_part # dividir no meio exato e distribuir metade para cada variavel ???

        Else:
            # dividir no meio sendo +1 pra esquerda

        # left_part : int = Parte da esquerda
        # right_part : int = Parte da direita

        # Conversão de tipo para int novamente
        # left_part = passando de string pra int denovo
        # right_part = passando de string pra int denovo

        # Soma variáveis
        combined_sum : int = left_part + right_part

        # Verificação se o quadrado da soma é igual ao número original
        squared_sum = combined_sum * combined_sum
        if squared_sum == number:
            return 1

    return 0  # Retorna 0 caso contrário, se nenhuma condição for satisfeita


def main() -> None:

    while True:
        print("\tBem-vindo à verificação de Números de Kaprekar \n")

        try:
            N: int = int(input("Digite um número (no intervalo de 1 a 100.000.000): "))
            if 1 <= N <= 100000000:
                print(is_kaprekar(N))
            else:
                print("O número está fora do intervalo (1 a 100.000.000)")
        except ValueError:
            print("Insira um número inteiro!")


if __name__ == "__main__":
    main()
