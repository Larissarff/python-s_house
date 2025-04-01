# CALCULADORA

# fazendo uma função para cada procedimento
def somar(a: float, b: float) -> float:
  return a + b         # return não recisa de =

def subtrair(a: float, b: float) -> float:
  return a - b

def multiplicar(a: float, b: float) -> float:
  return a * b

def dividir(a: float, b: float) -> float:
  if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
  return a / b

# iniciando a main
def main() -> None:
  print("Bem vindo á calculadora!")
  
  print("Escolha sua operação: ")
  print(" Digite 1 para somar")
  print(" Digite 2 para subtrair")
  print(" Digite 3 para multiplicar")
  print(" Digite 4 para dividir")
  
  escolha = (input("Escolha o numero que deseja:"))

  try:
    escolha = int(escolha)
    if escolha not in [1,2,3,4]:
    print("Escolha inválida")
    return

    a = float(input("Digite o primeiro numero: "))  # ATENTAR AOS PARÊNTESES
    b = float(input("Digite o segundo numero: "))

    if escolha == 1:
       resultado = somar(a,b)
       print(f"Resultado da soma é: {resultado}")
    elif escolha == 2:
       resultado = subtrair(a,b)
       print(f"Resultado da subtração é: {resultado}")
    elif escolha == 3:                                   # sempre colocar ':' após if e elif
       resultado = multiplicar(a,b)
       print(f"Resultado da multiplicação é: {resultado}")
    elif escolha == 4:
       try:
         resultado = dividir(a,b)
         print(f"Resultado da divisão é: {resultado}")
       except ValueError as e:
         print(e)

  except ValueError:
    print("Entrada inválida. Por favor, insira números válidos.")

if __name__ == "__main__":
main()
