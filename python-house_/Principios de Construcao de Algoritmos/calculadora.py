def somar(a: float, b: float) -> float:   # estrutura com o retorno e depois os dois pontos!
    return a + b

def subtrair(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividir(a: float, b: float) -> float:
    return a / b
    

def main()-> None:  # -> retornar o que deseja

    print("Bem vindo á calculadora!")

    operacao = input("Selecione a operação que deseja \n +, -, *, /") # não esquecer o input

    num1 = (float(input("Digite o primeiro numero: "))) #  variável = (tipo do dado(input(texto que pede a entrada do dado)))
    num2 = (float(input("Digite o segundo numero: ")))

    try:
        if operacao == '+':                   # if sem precisar de ()
            resultado = somar(num1,num2)

        elif operacao == '-':
            resultado = subtrair(num1, num2)

        elif operacao == '*':
            resultado = multiplicar(num1, num2)
        
        elif operacao == '/':
            if num2 == 0:
                print("Numero inválido, selecione um numero diferente de 0 para divisão!")
                return
            else:
                resultado = dividir(num1, num2)
        else:
            print("Dado inválido!")
            return
        
        print(f"Resultado da sua operação é {resultado}")

    except Exception as e:           #  try é para tratamento de exceções (erros), enquanto switch (em C) é para seleção condicional entre várias opções.
        print(f"Ocorreu um erro: {e}")
    
if __name__ == '__main__':
    main()
