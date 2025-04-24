'''
JSON = Java Script Object Notation

o conteudo é organizado em formato de dicionario, com pares chave -> valor
'''

# fomato do dicionario:
dictionary = { 'nome' : 'Larissa Ferreira',
        'linguagem' : 'python',
        'similar' : ['c', 'VBA', 'C#'],
        'matricula' : '1234567'
        }

# para exibir um conteudo de um dicionario:

for k,v in dictionary.items():
    print(k,v)

import json

# json.dumps converte o dicionario em um arquivo json
print(json.dumps(dictionary))