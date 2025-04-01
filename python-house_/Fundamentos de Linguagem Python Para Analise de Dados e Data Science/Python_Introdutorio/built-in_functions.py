'''

as funções built-in, ou nativas, são funções integradas no núcleo da linguagem,
prontamente disponíveis para uso em qualquer programa, sem a necessidade de importação de módulos

'''

abs(-89) # abs() retorna o valor absoluto de um numero ou equação
abs(78-89)

bool(0) # retorna false
bool(1) # retorna true

int(4.5) # retorna a parte inteira, nesse caso, 4

str(13) # retorna em formato string, nesse caso, '13'

# exemplo de aplicação:

idade = int(input("Informe a sua idade: \n")) # Se não houvesse mudança de tipo da variavel, a comparação seria impossível
if idade > 12: 
    print("Não pode entrar no brinquedo! ")
else:
    print("Pode entrar no brinquedo! ")


len([12,13,14,15]) # função len() retorna o tamanho do array, lista, quantidade de caracteres de string, coleção a ser analisada

array = [1, 2, 3]
max(array) # retorna o maior valor, nesse caso, 3
min(array) # retorna o menor valor, nesse caso, 1

sum(array) # soma os valores do array, nesse caso, retorna 6