from urllib.request import urlopen
import json

# extraindo o conteudo com o link da web, lendo e armazenando na variavel response pelo modo de leitura
response = urlopen("https://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')

dados = json.loads(response)[0] # passa para formato json
# indice [0] retorna apenas o primeiro valor

# criando um arquivo json com o conteudo
with open('C:/Users/Pichau/.vscode/python/python-s_house/python-house_/manipulacao_de_arquivos/manipulacao_JSON/extracao_de_dados_da_web_com_JSON/arquivo.json', 'w') as arquivo:
    arquivo.write(json.dumps(dados))

# com base nos indices printados, buscarei filtrar informações

print('Título: ', dados['title'])
print('URL: ', dados['url'])
print('Duração: ', dados['duration'])
print('Número de Visualizações: ', dados['stats_number_of_plays'])

# Copiarei o conteudo para dados do tipo txt
arquivo_fonte = 'C:/Users/Pichau/.vscode/python/python-s_house/python-house_/manipulacao_de_arquivos/manipulacao_JSON/extracao_de_dados_da_web_com_JSON/arquivo.json'
arquivo_destino = 'C:/Users/Pichau/.vscode/python/python-s_house/python-house_/manipulacao_de_arquivos/manipulacao_JSON/extracao_de_dados_da_web_com_JSON/arquivo.txt'

with open(arquivo_fonte, 'r') as infile:
    text = infile.read()

    with open (arquivo_destino, 'w') as outfile:
        outfile.write(text)