# utilização do WITH dispensa a necessidade de utilizar "arquivo.close", evitando conflitos

with open ('C:/Users/Pichau/Downloads/Python/pythons_house/python-s_house-1/python-house_/manipulacao_de_arquivos/manipulacao_arq_txt/cientista.txt', 'r') as arquivo:
    # traduzindo, "quando, o caminho dado for aberto para leitura, chamarei de arquivo"
    conteudo = arquivo.read()
    # o que foi lido, sera gravado na variavel "conteudo"

print(len(conteudo))
print(conteudo)

with open('C:/Users/Pichau/Downloads/Python/pythons_house/python-s_house-1/python-house_/manipulacao_de_arquivos/manipulacao_arq_txt/cientista.txt', 'w') as arquivo:
    arquivo.write('\n')
    arquivo.write(" Alteração posterior")
    arquivo.write('\n')

with open ('C:/Users/Pichau/Downloads/Python/pythons_house/python-s_house-1/python-house_/manipulacao_de_arquivos/manipulacao_arq_txt/cientista.txt', 'r') as arquivo:
    # abrindo novamente para leitura após a alteração
    conteudo = arquivo.read()

print(conteudo)