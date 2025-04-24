'''
Um arquivo CSV se caracteriza por ter seus dados separados por virgulas
'''
# importando csv 
import csv

# criando o csv numeros
# quando o caminho não é encontrado, ele cria o arquivo. 
with open('C:/Users/Pichau/.vscode/python/python-s_house/python-house_/manipulacao_de_arquivos/manipulacao_CSV/numeros.csv', 'w') as arquivo:
    # cria o objeto de gravação, onde ficará o conteudo do arquivo csv para manipulação
    writer = csv.writer(arquivo)

    # grava no arquivo, write row = escreve na linha
    writer.writerow(('nota1', 'nota2', 'nota3'))
    writer.writerow((63,87,92))
    writer.writerow((61,79,76))
    writer.writerow((72,64,91))

# leitura dos arquivos
with open('C:/Users/Pichau/.vscode/python/python-s_house/python-house_/manipulacao_de_arquivos/manipulacao_CSV/numeros.csv', 'r', 
          encoding='utf8', # tipo de codificação do arquivo
          newline = '\r\n') as arquivo:
    conteudo = csv.reader(arquivo)

    for x in conteudo:
        # cada elemento do objeto é impresso. cada linha = um objeto
        print(x)
        # o documento csv é tratado como uma lista, separada por colchetes, o que se torna de facil manipulação
