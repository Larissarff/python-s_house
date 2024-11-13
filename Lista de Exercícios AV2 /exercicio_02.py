from typing import Union

def is_kaprekar(number: int) -> int:
  
    str_num : str = str(number) # tratando de int para string pra separação
    length : str = len(str_num) # mapeando tamanho
  
   for i in range(1, length):
    # Divisão do numero
    left_str = str_num[:i] if str_num[:i] != "" else "0"
    right_str = str_num[i:] if str_num[i:] != "" else "0"
    
    # Conversão de tipo para int novamente
    left_part = int(left_str) if left_str.isdigit() else 0
    right_part = int(right_str) if right_str.isdigit() else 0
    
    # Soma variáveis
    combined_sum = left_part + right_part
    
    # Verificação da multiplicação dos quadrados retornando no numero original
    squared_sum = combined_sum * combined_sum
    if squared_sum == number:
        result = 1 
        return result  
  return 0 

def main() -> None:

  print("\tBem vindo a verificação de Números de Kaprekar \n")
   
    try:
        N: int = int(input("Digite um número (no intervalo de 1 á 100.000.000): "))
        if 1 <= N <= 100000000:
            print(is_kaprekar(N))
        else:
            print("O número está fora do intervalo (1 á 100.000.000)")
    except ValueError:
        print("Insira um número inteiro!")


if __name__ == "__main__":
    main()
