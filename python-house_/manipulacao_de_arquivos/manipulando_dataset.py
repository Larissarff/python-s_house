# dados retirados do site https://data.cityofchicago.org/

f = open('"C:\\Users\\06011175\\larissa\\pythons_house\\python-s_house\\python-house_\\manipulacao_de_arquivos\\arquivos\\salarios.csv', 'r') # r habilitando leitura
# lembrando que o caminho muda conforme a posição da sua pasta

data = f.read() # lendo o arquivo

rows = data.split('\n') # separando as linhas com base no delimitador

full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

print(full_data)