# Escreva um programa que leia uma lista de números inteiros e exiba-os em ordem crescente

def main() -> None:
  quantity_of_numbers = int(input("Digite a quantidade de numeros que deseja incluir na lista: \n"))
  
  lista = []
  
  for i in range(quantity_of_numbers):
      num = int(input(f"Digite o numero {i + 1}: "))
      lista.append(num)

  lista.sort()
    
    # Exibe a lista ordenada
  print("A lista em ordem crescente é:", lista)

if __name__ == '__main__':
 main()
