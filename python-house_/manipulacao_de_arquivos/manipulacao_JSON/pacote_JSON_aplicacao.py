import json

dictionary = { 'nome' : 'Larissa Ferreira',
        'linguagem' : 'python',
        'similar' : ['c', 'VBA', 'C#'],
        'matricula' : '1234567'
        }

# criando um arquivo json
with open('C:/Users/Pichau/.vscode/python/python-s_house/python-house_/manipulacao_de_arquivos/manipulacao_JSON/dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dictionary))

# leitura de arquivos json
with open ('C:/Users/Pichau/.vscode/python/python-s_house/python-house_/manipulacao_de_arquivos/manipulacao_JSON/dados.json', 'r') as arquivo:
    leitura = arquivo.read()
    dados = json.loads(leitura) # carrega o conteudo do arquivo no formato JSON

print(dados['nome']) # imprimindo o valor utilizando a chave como índice