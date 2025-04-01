#treinando utilização de subrotinas em python

def ler_notas() -> float:
    while True:
        try:
            nota = float(input("Digite uma nota da prova: \n"))
            return nota
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")

def media_notas(nota1: float, nota2: float) -> float:
    return (nota1 + nota2) / 2
    
def main() -> None:
    print("Calculadora de médias: ")
    
    nota1 = ler_notas()
    nota2 = ler_notas()
    
    resultado = media_notas(nota1, nota2)
    
    print(f"A média das notas é: {resultado}")

if __name__ == "__main__":
    main()
