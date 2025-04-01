def sum_of_numbers (numbers: list[int]) -> int:
    return sum(numbers)

def main() -> None:
    quantity_of_numbers = int(input("Digite quantos numeros quer somar:\n"))
    
    numbers = []
    
    for i in range(quantity_of_numbers):
        num = int(input(f"Digite o número {i + 1}:\n"))
        numbers.append(num)
    
    total_sum = sum_of_numbers(numbers)
    
    print(f"A soma total dos numeros resulta em: {total_sum}")
    
if __name__ == "__main__":
  main()
