# dados retirados do site https://data.cityofchicago.org/

f = open('C:\\Users\\Pichau\\Downloads\\Python\\pythons_house\\python-s_house-1\\python-house_\\manipulacao_de_arquivos\\arquivos\\salarios.csv', 'r') # r habilitando leitura
# lembrando que o caminho muda conforme a posição da sua pasta na sua máquina

data = f.read() # lendo o arquivo

rows = data.split('\n') # separando as linhas com base no delimitador

full_data = []

for row in rows:
    # coloca cada palavra da lista como uma nova lista,
    #  gerando uma lista de listas
    split_row = row.split(",")
    # separando por virgulas, separa nome de sobrenome, indevidamente
    full_data.append(split_row)

# print(full_data) # - imprime todo o conteudo de full_data 

# contando quantas linhas tem no arquivo
count = 0
for row in full_data:
    count += 1

print(count)

# contando o numero de colunas
for row in rows: # mapear primeiro a primeira linha do arquivo, o cabeçalho da tabela
    slpit_row = row.split(",") # separa os nomes das colunas presentes no cabeçalho por vírgulas
    full_data.append(split_row)
    first_row = full_data[0] # começa contando de zero 
    
count_2 = 0

for column in first_row: 
    count_2 += 1

print(count_2)