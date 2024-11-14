from typing import Union

def is_kaprekar(number: int) -> int:
    string_number : str = str(number)
    tamanho_numero : int = len(string_number)
    tamanho_metade: int = tamanho_numero // 2

    inicio : str = string_number[:tamanho_metade]
    final : str = string_number[tamanho_metade:]

    inicio_int : int = int(inicio)
    final_int : int = int(final)

    soma_numero : int = inicio_int + final_int
    sqr_soma : int = soma_numero ** 2

    if sqr_soma == number:
        return 1

    return 0
      # Retorna 0 caso contrário, se nenhuma condição for satisfeita

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
