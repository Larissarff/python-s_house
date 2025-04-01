import math 

def num_primo(num):
    if (num % 2) == 0 and num > 2:
        print(" Esse numero não é primo")

    for i in range(3, int(math.sqrt(num)) + 1, 2):  
        # incrementando a logica com a biblioteca math
        if (num % i) == 0:
            return "Esse numero não é primo"
        else:
            return "Esse numero é primo"

num_primo(29) # exemplo de aplicação 

# -----------------------------------------------------------------------------------------------------------------------------

def lowercase(text):
    return text.lower()

texto = 'este Texto DevEria Ser tOdo em LowErCase'

texto_lowercase = lowercase(texto)

print(texto_lowercase) # este texto deveria ser todo em lowercase

# -----------------------------------------------------------------------------------------------------------------------------

# Slpit : função que separa uma coleção, lista, array ou string com base em um ponto deseparação

def split_space(text):
    return text.split(" ")

texto_2 = "Esta função é bem útil para separar grandes volumes de dados"

texto_separado = split_space(texto_2)

print(texto_separado) # ['Esta', 'função', 'é', 'bem', 'útil', 'para', 'separar', 'grandes', 'volumes', 'de', 'dados']

# fazendo split dos dados:

def split_string_por_letras(text):
    texto = text.upper()

    for letra in texto: # para cada letra percorrida, sera impresso 
        print(letra)

texto_por_letra = split_string_por_letras(texto_2)
print(texto_por_letra)

''' retorna:
E
S
T
A
 
F
U
N
Ç
Ã
O
 
É
 
B
E
M
 
Ú
T
I
L
 
P
A
R
A
 
S
E
P
A
R
A
R
 
G
R
A
N
D
E
S
 
V
O
L
U
M
E
S
 
D
E
 
D
A
D
O
S
'''

# lambda function : uma função omitida, feita direta em uma linha apenas

numero1 = 2
numero2 = 4

soma = lambda num1,num2 : num1+num2 

print(soma(numero1, numero2))