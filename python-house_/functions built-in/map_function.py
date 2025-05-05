'''
Função map() é uma função que aplica uma determinada função a cada elemento de uma estrutura de dados
'''
def power(x : int) -> int:
    return x ** 2

numbers = [1, 2, 3, 4, 5]

# a função map relaciona o método power com a lista numbers e aplica a todos os elementos em numbers, retornando uma lista com os quadrados dos numeros
# importnte converter para lista, pois em python 3 a função map retorna um interator
square_numbers = list(map(power, numbers))

# map utilizando função lambda
temperaturas = [0, 12, 22, 45, 50]

print(list(map(lambda x: (5.0/9) * (x - 32), temperaturas)))