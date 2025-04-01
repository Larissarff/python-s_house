# UM PROGRAMA BÁSICO QUE FAÇA A DIVISÃO DE DOIS NUMEROS 

def main() -> None:
    num1: int = int(input("Digite o primeiro número: "))
    num2: int = int(input("Digite o segundo número: "))

    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.") # print sem formatação
        # quando se imprime apenas uma string, sem variáveis
    else:
        resultado: float = num1 / num2
        print(f"Resultado: {resultado}") # print com formatação.
        # print que gera valores de variáveis dentro desse {}

if __name__ == "__main__":
    main()
